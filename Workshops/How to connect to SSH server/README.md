# How to use Arkham or Dunwich server

To connect to ssh server (Arkham or Dunwich), use software (CIAO, Xspec, Sherpa, CASA) or run a Jupyter notebook, follow these steps:

1) Make an account.
2) Connect to the server.
3) Setup shortcut to the server.
4) Setup login without password.
5) Install & use required software.
6) Setup ssh tunnel for Jupyter notebook.

<br>

## 1) Make an account.

If we haven't created you an account yet, contact me (plsek@physics.muni.cz) or JP (jeanpaul.breuer@gmail.com) and we will do so. In order to create an account, you need to pick a `username` and `password`.

<br>

## 2) Connect to the server

To try if everything works, you can connect to the server using ssh protocol. For most linux and MAC operating systems, the ssh client should be preinstalled. If not installed, for linux-based systems, installing openssh library should do the job (`sudo apt install openssh-client`). For Windows users, I highly recommend switching to UNIX based system :-) or installing a Windows Subsystem for Linux ([WSL](https://learn.microsoft.com/en-us/windows/wsl/install)). For pure Windows lovers, the last resort is to use PowerShell or [Putty](https://www.putty.org/).

After your ssh client is installed, you can connect to the Arkham server using the following command:

```
ssh yourusername@arkham.physics.muni.cz
```

and for Dunwich server using: 

```
ssh yourusername@dunwich.physics.muni.cz
```

Note: don't forget to replace `yourusername` with your actual username.

After running the command, you will be asked for your password.

If you wish to also run remote apps with a graphical user interface (GUI), just add an argument `-X` to the command:

```
ssh -X yourusername@arkham.physics.muni.cz
```

Note: only works if [X-server](https://en.wikipedia.org/wiki/X_Window_System) is installed on your system. For Linux and MAC systems, it is usually pre-installed. For Windows, try [VcXsrv](https://sourceforge.net/projects/vcxsrv/).

<br>

## 3) Setup shortcut to the server

So you don't always have to type in the full server address, you can add the following settings into a `config` text file located in `.ssh` folder located in your home directory (if file doesn't exist, create a new file `touch ~/.ssh/config`) on YOUR computer:

```
Host arkham
    HostName arkham.physics.muni.cz
    User yourusername

Host dunwich
    HostName dunwich.physics.muni.cz
    User yourusername
```

Note: don't forget to replace `yourusername` with your actual username.

### Optional enhancement

To simplify things even more, you can add an alias to the `.bashrc` file (all commands in this file are executed when starting a terminal). Open the `.bashrc` file using your favourite text editor and add the following line:

`alias Arkham="ssh -X arkham"`

or 

`alias Dunwich="ssh -X dunwich"`

Now you can connect very simply by calling `Arkham` or `Dunwich` from your terminal (beware of uppercase and lowercase letters).

Note: to apply changes in `.ssh/config` and `.bashrc` files, you need to turn off and on your terminal.

<br>

## 4) Setup login without password

In order to not require to use password on login, do the following steps on YOUR computer:

- First of all, check if there is a `id_rsa.pub` file located in .ssh folder which is in your home folder (`ls ~/.ssh`). If not, generate a new key by running the following command:\
\
`ssh-keygen -t rsa`\
\
After running the command, you will be asked several options which you can all agree with by pressing enter (you can also set no passphrase).

- Next, you should create an .ssh folder in your home directory on Arkham or Dunwich server (nothing happens if directory already exists):\
\
`ssh yourusername@arkham mkdir -p .ssh`

- Now you need to upload the public key (`id_rsa.pub`) to the server:\
\
`cat ~/.ssh/id_rsa.pub | ssh arkham 'cat >> .ssh/authorized_keys'`

After this, you should now be able to connect to Arkham or Dunwich server without the need to type-in your password everytime. For more info, see this [tutorial](http://www.linuxproblem.org/art_9.html).

<br>

## 5) Install & use required software.

Users on Arkham and Dunwich are not given sudo rights. To install required libraries and software using `sudo apt install`, please contact one of the sudoers: Tomáš Plšek (plsek@physics.muni.cz), Jean-Paul Breuer (jeanpaul.breuer@gmail.com) or Filip Hroch (hroch@physics.muni.cz). If possible, users are encouraged to use pre-installed software (CIAO, SPEX, Xspec, CASA) or install programs locally without sudo privileges. 

### CIAO, SPEX, Xspec, CASA

As already mentioned, some of the often used software is already pre-installed (Note: This mostly applies to Arkham, if needed, we can install all the software also onto Dunwich server). If some of the software needs to be updated or is non-functional, please contact one of the above mentioned suders. To use this pre-installed software, you only need to initialize it by running or sourcing corresponding files. 

To use CIAO (version 4.15) run:

```
source /opt/ciao-4.15/bin/ciao.sh
```

To use SPEX (version 3.06) run:
```
export SPEX90=/opt/SPEX-3.06.01-Linux
/opt/SPEX-3.06.01-Linux/bin/spex
```

To use Xspec (version 12.12.1) run:
```
export HEADAS=/opt/heasoft-6.30.1/x86_64-pc-linux-gnu-libc2.31
source ${HEADAS}/headas-init.sh 
```

To use CASA (version 6.1.0) run:
```
/opt/casa/casa-6.1.0-118/bin/casa
```

Alternatively, you can create aliases and add them to your `.bashrc` file (on server side):

```
alias CIAO="source /opt/ciao-4.15/bin/ciao.sh"

export HEADAS=/opt/heasoft-6.30.1/x86_64-pc-linux-gnu-libc2.31
alias heainit="${HEADAS}/headas-init.sh"

export SPEX90=/opt/SPEX-3.06.01-Linux
alias SPEX="/opt/SPEX-3.06.01-Linux/bin/spex"

alias casa="/opt/casa/casa-6.1.0-118/bin/casa"
```

and from now on, you can initialize CIAO, SPEX, Xspec, and CASA by simply calling `CIAO`, `SPEX`, `heainit` or `casa` from your terminal.

Note: Using command `whereis ciao`, you can check what versions of CIAO are currently installed and you can select an older or newer version.

### Python libraries

Required Python packages can be installed using a user-installation of python PIP package (e.g. `pip3 install jupyterlab`). Nevertheless, users are encouraged to rather use [Anaconda](https://www.anaconda.com/) packaging software, that helps to resolve package dependencies and conflicts. To do this, download the installation script and run it in your home directory on the corresponding server (e.g. `bash Anaconda3-2022.10-Linux-x86_64.sh`). After running the installation script, you will be asked several questions, which you can all agree with by pressing enter. After the anaconda software is installed, `base` environment will automatically be activated everytime you start a new terminal. To disable automatic activation of `base` environment run `conda config --set auto_activate_base false`.

To install a new environment with required packages and versions run for example:

```
conda create -n "name_of_environment" python=3.11
```

After the environment is installed, to use it you need to activate it everytime you start a new terminal:
```
conda activate name_of_environment
```

And then you can additionaly install other required libraries:

```
conda install astropy scipy numpy jupyter...
```

By adding `-c name_of_channel` to the install command, you can also specify the channel from which the package will be downloaded. Some packages are not available from the default channel `base`, so they have to be installed from a community repository of packages `conda-forge`:
```
conda install astropy scipy numpy jupyter -c conda-forge
```
Once the `conda-forge` channel is used, all future package updates and installations need to be performed by adding `-c conda-forge` to the install command.

Specific package can be updated using:
```
conda update astropy -c conda-forge
```
and to update all packages at once run:
```
conda update --all -c conda-forge
```

If you want to create your local installation of CIAO using conda, run this command (also see this [tutorial](https://cxc.cfa.harvard.edu/ciao/download/)):
```
conda create -n ciao-4.15 -c https://cxc.cfa.harvard.edu/conda/ciao -c conda-forge ciao sherpa ds9 ciao-contrib caldb_main marx python=3.10
```
<br>

## 6) Setup ssh tunnel for Jupyter notebook

To run a Jupyter notebook or Jupyter-lab remotely on Arkham or Dunwich server and open the notebook on your computer, you need to do these two steps:

#### 1) Connect to the server and run the notebook / lab

This is how you run a jupyter-lab on the Arkham server for PIP3-base installation:

```
ssh arkham "jupyter-lab --no-browser --port=8888"
```
and for conda-based installation:

```
ssh arkham "source ~/anaconda3/bin/activate yourenvironment; jupyter-lab --no-browser --port=8888"
```

Note: don't forget to change `yourenvironment` to your actual environment.

#### 2) Make an ssh-tunnel

Now you need to create an ssh tunnel with the same port:

```
ssh -CNL localhost:8888:localhost:8888 arkham
```

After the tunnel is created, copy-paste the link obtained in step 1) into your web browser.

WARNING: Ports are shared between all users, it is therefore highly recommended to select some personal port e.g. 8892 and only use this one. If you start using some port and on your next login the port is not free, this usualy means your previous session is still running or was not properly exited. On the server side, you can list running sessions using:

```
jupyter server list
```

and stop them using:

```
jupyter server stop 8892
```

### Additional enhancement

The above stated procedure usually requires two running terminals. To simplify things a bit, you can create a function in your `.bashrc` file, which does the following steps:

1) Connects to Arkham server and stops previous notebooks on specified port (only use for your personal port)
2) Runs a Jupyter-lab on specified port
3) Creates an ssh tunnel for that port

```
function jupyter-arkham {
  port=$1
  if [ -z $1 ]; then port=8892; fi
  ssh arkham "source ~/anaconda3/bin/activate yourenvironment ; jupyter server stop ${port}"
  cmd="ssh arkham 'source ~/anaconda3/bin/activate yourenvironment ; jupyter-lab --no-browser --port=$port' & ssh -CNL localhost:$port:localhost:$port arkham"
  echo "Running $cmd"
  eval $cmd
}
```

Note: don't forget to change `yourenvironment` to your actual environment.

After that, you can start a remote Jupyter-lab by simply calling:

```
jupyter-arkham
```

The `jupyter-arkham` function has one optional argument, so alternatively also port can be specified:

```
jupyter-arkham 8892
```

Note: In case you run `jupyter-arkham` function from a terminal, you turn it off (by pressing ctrl+c), and then you run the `jupyter-arkham` again from the same terminal, you can get the an error like this: `bind [127.0.0.1]:8892: Address already in use`, usually meaning that the ssh tunnel was not properly exited. This can be solved by just killing the terminal session and running a new one. Note2: This error message `bind [127.0.0.1]:8892: Address already in use` can also be obtained if there is a local notebook running on your PC and you are trying to run a remote jupyter on the same port. 
