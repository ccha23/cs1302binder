FROM jupyter/scipy-notebook:python-3.8.8

USER root

# Install all OS dependencies for fully functional notebook server
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    gnupg2 apt-transport-https && \
    wget -O - https://xpra.org/gpg.asc | apt-key add - && \
    echo "deb https://xpra.org/ focal main" > /etc/apt/sources.list.d/xpra.list && \
    apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    build-essential \
    curl \
    vim-tiny \
    less \
    git \
    inkscape \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    pandoc \
    pdf2svg \
    # ---- nbconvert dependencies ----
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-plain-generic \
    # ----
    tzdata \
    unzip \
    zip \
    nano-tiny \
    ffmpeg \
    gcc \
    libcairo2-dev \
    libffi-dev \
    libpango1.0-dev \
    pkg-config \
    sshfs \
    # ---- xpra ---- #
    xfce4 \
    gconf2 \
    xfce4-terminal \
    xfce4-clipman \
    xterm \
    xfce4-taskmanager \
    xauth xinit dbus-x11 \
    xpra xpra-html5 \
    x11-utils \
    xfonts-base \
    x11-apps \
    xvfb \
    xubuntu-icon-theme \
    thonny \
    python3-websockify \
    python3-dbus python3-paramiko python3-xdg python3-pyinotify python3-netifaces python3-uinput && \
    update-icon-caches /usr/share/icons/elementary-xfce \
    /usr/share/icons/elementary-xfce-dark /usr/share/icons/elementary-xfce-darker \
    /usr/share/icons/elementary-xfce-darkest && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    # fix https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=908156
    mkdir -p /run/xpra &&\
    mkdir -p /run/user && \
    fix-permissions /run && \
    chown -R ${NB_USER} /run

# setup a minimal texlive installation for manim
COPY texlive-profile.txt /tmp/
ENV PATH=/usr/local/texlive/bin/x86_64-linux:$PATH
RUN wget -O /tmp/install-tl-unx.tar.gz http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    mkdir /tmp/install-tl && \
    tar -xzf /tmp/install-tl-unx.tar.gz -C /tmp/install-tl --strip-components=1 && \
    /tmp/install-tl/install-tl --profile=/tmp/texlive-profile.txt \
    && tlmgr install \
        amsmath babel-english cbfonts-fd cm-super caption ctex doublestroke dvisvgm environ eurosym everysel \
        fancyvrb float fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin \
        mathastext microtype ms oberdiek parskip physics preview ragged2e relsize rsfs \
        setspace standalone tcolorbox tipa ucs upquote qsymbols wasy wasysym xcolor xetex xkeyval adjustbox collectbox titling booktabs enumitem \
    && fix-permissions /usr/local/texlive

# fix https://github.com/jupyter/docker-stacks/issues/815
RUN cat /etc/skel/.bashrc >> /etc/bash.bashrc

RUN TZ=Hongkong && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN VERSION=3.10.2 && \
    curl -fOL https://github.com/cdr/code-server/releases/download/v${VERSION}/code-server_${VERSION}_amd64.deb && \
    dpkg -i code-server_${VERSION}_amd64.deb && \
    rm -rf code-server_${VERSION}_amd64.deb

# Switch back to jovyan
USER ${NB_UID}

COPY fix-nbextensions /usr/local/bin/fix-nbextensions    

# Install Python 3 packages
RUN conda install --quiet --yes \
    'black=21.*' \
    'hide_code=0.6.*' \
    'ipydrawio=1.1.*' \
    'ipydrawio-export=1.1.*' \
    'ipykernel' \
    'jupyter-server-proxy=3.1.*' \  
    'jupyter-vscode-proxy=0.1.*' \
    'jupyterhub=1.4.*' \
    'jupyterlab_code_formatter=1.4.*' \
    'jupyterlab-lsp=3.8.*' \
    'jupyterlab-system-monitor=0.8.*' \
    'jupyterlab-git=0.32.*' \
    # 'jupyterlab-tour=3.1.*' \
    'jupytext=1.11.*' \
    'jupyter_nbextensions_configurator=0.4.*' \
    'jupyter_contrib_nbextensions=0.5.*' \
    'nbgitpuller=0.10.*' \
    'python-lsp-server=1.2.*' \
    'rise=5.7.*' \
    'xeus-python==0.12.*' \
    && \
    fix-nbextensions && \
    jupyter nbextension enable code_prettify/code_prettify --sys-prefix && \
    jupyter nbextension enable init_cell/main --sys-prefix && \
    jupyter nbextension enable scratchpad/main --sys-prefix && \
    jupyter nbextension enable spellchecker/main --sys-prefix && \
    jupyter nbextension enable codefolding/main --sys-prefix && \
    jupyter nbextension enable --section edit codefolding/edit --sys-prefix && \
    pip install --quiet --no-cache-dir \
    'aquirdturtle_collapsible_headings==3.1.*' \
    'manim==0.7.*' \
    'itikz==0.1.*' \
    'jupyter-www-proxy' \
    'mytutor' \
    'jupyter-xprahtml5-proxy' \
    'thonny' \
    # 'ngshare_exchange==0.5.*' \
    # 'git+https://github.com/jupyter/nbgrader.git@cdcba95ee334e667b4438532dd27093b3c4df099' && \
    # jupyter nbextension install --symlink --sys-prefix --py nbgrader && \
    # jupyter nbextension enable --sys-prefix --py nbgrader && \
    # jupyter serverextension enable --sys-prefix --py nbgrader  && \
    # jupyter nbextension disable --sys-prefix formgrader/main --section=tree && \
    # jupyter nbextension disable --sys-prefix course_list/main --section=tree && \
    # jupyter serverextension disable --sys-prefix nbgrader.server_extensions.course_list && \
    && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# fix https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=908156
ENV XDG_RUNTIME_DIR='/run/user/xpra'

# fix http://xpra.org/trac/ticket/2174?cversion=2&cnum_hist=4
ENV XDG_MENU_PREFIX='xfce-'

COPY --chown=${NB_USER}:${NB_GID} condarc "${CONDA_DIR}/.condarc"

# fix https://stackoverflow.com/questions/64770659/fvwm-menu-desktop-hanging-during-menu-creation-and-failing-with-python-exception
COPY Menu.py /usr/lib/python3/dist-packages/xdg/

# customize xpra https://xpra.org/manual.html
COPY xpra_init.py "${CONDA_DIR}/lib/python3.8/site-packages/jupyter_xprahtml5_proxy/__init__.py"

# fix favico.png missing issue: some javascripts running on client side uses absolute path /favicon.png instead of ./favicon.png
# (as they are served under /xprahtml5/ for jupyter-xprahtml5-proxy
COPY js/ /usr/share/xpra/www/js/


WORKDIR "${HOME}"
