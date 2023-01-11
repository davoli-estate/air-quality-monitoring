import git
import time

# URL of the Github repository
repo_url = 'https://github.com/username/repository.git'

# Local path where the repository will be cloned
local_path = '/path/to/local/folder'

# Periodically check for new commits in the repository
while True:
    try:
        # Clone the repository if it doesn't already exist
        if not os.path.exists(local_path):
            git.Repo.clone_from(repo_url, local_path)
            update_program_on_device(local_path)
        else:
            # Open the repository
            repo = git.Repo(local_path)
            # Check if the latest commit on the remote main branch is the same as the local one
            local_hash = repo.head.commit.hexsha
            remote_hash = repo.remotes.origin.refs.master.commit.hexsha
            # Check if the local and remote hashes are different
            if local_hash != remote_hash:
                # Fetch new commits
                repo.remotes.origin.fetch()
                # Update the program on the Raspberry Pi Pico
                update_program_on_device(local_path)
    except Exception as e:
        # Handle any errors that occur
        print(f'An error occurred: {e}')
    # Wait for a specified period before checking for new commits again
    time.sleep(60) # check for new commits every 60 seconds
