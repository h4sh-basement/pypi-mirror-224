# Copyright 2020 Georges Racinet <georges.racinet@octobus.net>
#
# This software may be used and distributed according to the terms of the
# GNU General Public License version 2 or any later version.
#
# SPDX-License-Identifier: GPL-2.0-or-later
"""Interaction with Git repos.

It is not expected that the rise of the HGitaly project would remove
all interesting things to do with Git.
"""
from __future__ import absolute_import

try:
    from hgext3rd.hggit.git_handler import GitHandler
except ImportError:  # pragma: no cover (fallback for hg-git < 0.11)
    from hggit.git_handler import GitHandler

from heptapod.gitlab.branch import (
    GITLAB_BRANCH_REF_PREFIX,
    gitlab_branch_ref as git_branch_ref,
    gitlab_branch_from_ref as git_branch_from_ref,
)
from heptapod.gitlab.tag import (
    GITLAB_TAG_REF_PREFIX,
)
from .typed_ref import (
    GITLAB_TYPED_REFS_MISSING,
    gitlab_typed_refs,
)
from mercurial import (
    hg,
)
import os
import re

from .branch import (
    get_default_gitlab_branch,
    set_default_gitlab_branch,
    gitlab_branches,
    gitlab_tags,
    write_gitlab_branches,
    write_gitlab_tags,
)
from .special_ref import (
    special_refs,
    write_special_refs
)
from .keep_around import (
    KEEP_AROUND_REF_PREFIX,
    iter_keep_arounds,
    init_keep_arounds,
)
from .state_maintainer import GitLabStateMaintainer


class HeptapodGitHandler(GitHandler, GitLabStateMaintainer):

    def __init__(self, *args, **kwargs):
        super(HeptapodGitHandler, self).__init__(*args, **kwargs)

        main_repo = hg.sharedreposource(self.repo)
        if main_repo is None:
            main_repo = self.repo

        self.gitdir = re.sub(br'\.hg$', b'', main_repo.root) + b'.git'
        self.unfiltered_repo = self.repo.unfiltered()
        self._default_git_ref = None

    @property
    def gitlab_refs(self):
        return self.git.refs

    def has_git_repo(self):
        return os.path.exists(self.gitdir)

    def get_default_gitlab_ref(self):
        # HEAD is the source of truth for GitLab default branch
        # For native projects, it's going to be the one stored
        # in Mercurial, returned by get_default_gitlab_branch(), and we are
        # maintaining consistency until we reach the HGitaly2 milestone
        # (i.e., as long as hg-git is used even for native projects)
        res = self._default_git_ref
        if res is None:
            res = self.git.refs.get_symrefs().get(b'HEAD')
            self._default_git_ref = res
        return res

    def ensure_gitlab_default_branch(self):
        """Init GitLab default branch file from Git repository if needed.

        Nothing happens if the file is already present.

        :returns: ``None` if the file was already present. Otherwise,
           new GitLab default branch :class:`bytes`.
        """
        repo = self.repo
        gl_branch = get_default_gitlab_branch(repo)
        if gl_branch is not None:
            return

        self.ui.note(b"Initializing GitLab default branch file "
                     b"for repo at '%s'" % repo.root)

        if self.has_git_repo():
            gl_branch_ref = self.get_default_gitlab_ref()
            gl_branch = git_branch_from_ref(gl_branch_ref)
        else:
            gl_branch = b'master'

        set_default_gitlab_branch(repo, gl_branch)
        return gl_branch

    def set_default_gitlab_ref(self, new_default_ref):
        new_gl_branch = git_branch_from_ref(new_default_ref)
        self.repo.ui.note(
            b"Setting Git HEAD to %s and Hg default "
            b"GitLab branch to %s" % (new_default_ref, new_gl_branch))
        self.git.refs.set_symbolic_ref(b'HEAD', new_default_ref)
        set_default_gitlab_branch(self.repo, new_gl_branch)

        # cache invalidation
        self._default_git_ref = None

    hg_sha_from_gitlab_sha = GitHandler.map_hg_get
    gitlab_sha_from_hg_sha = GitHandler.map_git_get

    def extract_all_gitlab_refs(self):
        """Heptapod version of GitHandler.get_exportable().

        This rewraps :meth:`GitHandler.get_exportable` to add named branches
        and topics to the returned Git refs
        """
        git_refs = super(HeptapodGitHandler, self).get_exportable()
        self.extract_current_gitlab_branches(git_refs)
        return git_refs

    def export_commits(self):
        try:
            self.export_git_objects()
            self.update_gitlab_references()
        finally:
            self.save_map(self.map_file)

    def ensure_gitlab_branches(self):
        """Init GitLab branches state file from Git repository if needed.

        Nothing happens if the file is already present.

        :returns: ``None` if the file was already present. Otherwise,
           new GitLab branches :class:`dict`, same as
           ``gitlab_branches(self.repo)`` would.
        """
        repo = self.repo
        if gitlab_branches(repo) is not GITLAB_TYPED_REFS_MISSING:
            return

        self.ui.note(b"Initializing GitLab branches state file "
                     b"for repo at '%s'" % repo.root)

        if self.has_git_repo():
            gl_branches = self.gitlab_branches_hg_shas(self.git.refs.as_dict())
        else:
            gl_branches = {}
        write_gitlab_branches(repo, gl_branches)
        return gl_branches

    def ensure_gitlab_tags(self):
        """Init GitLab tags state file from Git repository if needed.

        Nothing happens if the file is already present.

        :returns: ``None` if the file was already present. Otherwise,
           new GitLab tags :class:`dict`, same as
           ``gitlab_tags(self.repo)`` would.
        """
        repo = self.repo
        if gitlab_tags(repo) is not GITLAB_TYPED_REFS_MISSING:
            return

        self.ui.note(b"Initializing GitLab tags state file "
                     b"for repo at '%s'" % repo.root)
        if self.has_git_repo():
            gl_tags = self.gitlab_tags_hg_shas(self.git.refs)
        else:
            gl_tags = {}
        write_gitlab_tags(repo, gl_tags)
        return gl_tags

    def ensure_gitlab_special_refs(self):
        """Init GitLab special refs file from Git repository if needed.

        Nothing happens if the file is already present.

        :returns: ``None` if the file was already present. Otherwise,
           new GitLab special refs :class:`dict`, same as
           ``special_refs(self.repo)`` would.
        """
        repo = self.repo
        if special_refs(repo) is not GITLAB_TYPED_REFS_MISSING:
            return

        self.ui.note(b"Initializing GitLab special refs state file "
                     b"for repo at '%s'" % repo.root)

        if self.has_git_repo():
            srefs = self.gitlab_special_refs_hg_shas(self.git.refs)
        else:
            srefs = {}
        write_special_refs(repo, srefs)
        return srefs

    def ensure_gitlab_keep_arounds(self):
        """Init GitLab keep arounds file from Git repository if needed.

        Nothing happens if the file is already present.

        :returns: ``None` if the file was already present. Otherwise,
           new GitLab keep-arounds :class:`set`.
        """
        repo = self.repo
        try:
            if next(iter_keep_arounds(repo)) is not GITLAB_TYPED_REFS_MISSING:
                return
        except StopIteration:
            return

        self.ui.note(b"Initializing GitLab keep-arounds state file "
                     b"for repo at '%s'" % repo.root)

        if self.has_git_repo():
            kas = self.gitlab_keep_arounds(self.git.refs)
        else:
            kas = ()
        init_keep_arounds(repo, kas)
        return kas

    def force_git_refs_from_gitlab_files(self):
        repo = self.repo
        git_refs = self.git.refs
        refs_to_remove = git_refs.keys()
        git_sha = self.gitlab_sha_from_hg_sha

        for type_name, ref_prefix in (
                ('branches', GITLAB_BRANCH_REF_PREFIX),
                ('tags', GITLAB_TAG_REF_PREFIX),
                ('special-refs', b'refs/'),
        ):
            typed_refs = gitlab_typed_refs(repo, type_name)
            if typed_refs is GITLAB_TYPED_REFS_MISSING:
                continue
            for name, hg_sha in typed_refs.items():
                ref = ref_prefix + name
                git_refs[ref] = git_sha(hg_sha)
                refs_to_remove.discard(ref)

        for ka in iter_keep_arounds(repo):
            if ka is GITLAB_TYPED_REFS_MISSING:
                continue
            ka_git = git_sha(ka)
            git_refs[KEEP_AROUND_REF_PREFIX + ka_git] = ka_git
            refs_to_remove.discard(ref)

        for ref in refs_to_remove:
            del git_refs[ref]

        default_gl_branch = get_default_gitlab_branch(self.repo)
        if default_gl_branch is not None:
            # don't use `self.set_default_gitlab_ref` as it writes also
            # the state file in the hg repo (should be idempotent, but let's
            # not risk that)
            self.git.refs.set_symbolic_ref(
                b'HEAD',
                git_branch_ref(default_gl_branch))
