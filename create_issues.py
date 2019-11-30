#!/usr/bin/env python

from redminelib import Redmine


def create_new_issue(
        redmine_url, rest_key, proj_id, issue_sub, track_id, issue_desc):
    redmine = Redmine(redmine_url, key=rest_key)
    create_issue = redmine.issue.create(
        project_id=proj_id,
        subject=issue_sub,
        tracker_id=track_id,
        description=issue_desc,
        status_id=1,
        priority_id=1,
        watcher_user_ids=[1],
        estimated_hours=4,
    )
    return create_issue


def main():
    # Initialization.
    rest_key = "832c994df42cde2a15df8a2a1007aa2a0582863a"
    redmine_url = "http://localhost:8080/"
    proj_id = 1
    issue_sub = "issue_7"
    track_id = 1
    issue_desc = "foo"

    result = create_new_issue(
            redmine_url, rest_key, proj_id, issue_sub, track_id, issue_desc)
    print("==> Issue created: " + str(result))


if __name__ == "__main__":
    main()
