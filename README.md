# CS1302 Jupyter

This is the repository for running the CS1302 Jupyter Environment outside a jupyterhub server. 

1. To run the notebooks with temporary storage, click 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ccha23/cs1302jupyter/HEAD?urlpath=git-pull?repo%3Dhttps%3A%2F%2Fgithub.com%2Fccha23%2Fcs1302%26urlpath%3Dlab%2F%2Ftree%2Fcs1302)

2. To run locally on your computer with permanent storage:
  - Install [docker](
https://docs.docker.com/get-started/#download-and-install-docker).
  - Run the docker in a terminal from a working directory of your choice.
    - For Mac/Linux shells:
    ```markdown
    docker run --rm -p 10000:8888 -m 4g \
            -v "${PWD}":/home/jovyan \
            chungc/cs1302:v0.7 \
            start-notebook.sh --NotebookApp.token=''
    ```
    - For Windows PowerShell:
    ```markdown
    docker run --rm -p 10000:8888 -m 4g `
            -v ${PWD}:/home/jovyan `
            chungc/cs1302:v0.5 `
            start-notebook.sh --NotebookApp.token=''  
    ```
    - It may take a couple minutes to run for the first time as it needs to download the docker image. Subsequent run should be fast.
    - Port 10000 specified by `-p` should be free for use. Otherwise, change it to a free port on your computer.
    - The maximum memory limit is set to be 4GB by `-m`. You should set an appropriate value according to the memory available on your computer.
  - Pull the notebooks from this repo in a web browser:  
  <http://localhost:10000/git-pull?repo=https%3A%2F%2Fgithub.com%2Fccha23%2Fcs1302&urlpath=lab%2Ftree%2Fcs1302&branch=main>
    - You can work on the notebooks under the `cs1302` subfolder. Clicking the above link again will automatically pull and merge changes from the repo, without overwritting your changes.
    - To finish, stop the notebook server by pressing `Control-C` in the terminal that runs the docker or close the terminal/PowerShell.
    - To restart, run the docker command again from the same working directory.

3. To run on Visual Studio Code locally
  - Install [Visual Studio Code](https://code.visualstudio.com/) and the extension [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
  - Click `View`->`Command Palette` 
  - Enter `Remote-Containers: Clone Repository in Container Volume...`. There is also a command for using a Named Container Volume instead.
  - Enter the repository url `https://github.com/ccha23/cs1302jupyter.git`
  - You can work on the notebooks in the `cs1302` subfolder and your files will be kept in a persistent docker volume.
  - You can start a jupyter lab server and open it in a browser by opening a terminal (`` Control-Shift-` ``) and run
  ```
  jupyter lab --NotebookApp.token=''
  ```
  - For more details, see the [vscode-remote-try-python](https://github.com/microsoft/vscode-remote-try-python) repository.
