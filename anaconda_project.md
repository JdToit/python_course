Introduction
Anaconda is a distribution, a “package”, of many different Python-related languages used for scientific computing, such as machine learning applications, data science, and large-scale data processing, to name a few. Its goal is to simplify package management and setting up ones environment.  Anaconda was founded by Peter Wang and Travis Oliphant in 2012. Anaconda has over 250 packages pre-installed, and thousands more can be installed. Anaconda can be considered an “all-in-one” package to download. Instead of having to download an IDE, for example Visual Studio Code, and Python itself, and other IDE’s you may need, other resources, tools, more IDE’s, etc., Anaconda installs a large spread of what any Python or R distribution developer may need.
Here is what one can expect once they’ve first installed Anaconda:
 
Pre-requisites 
Anaconda has certain hardware, software, security and network requirements in order to use it. It is important to take note of these, so that you know whether you have all the necessary requirements to properly run “Anaconda”. According to their website:
Its hardware requirements are:
⦁	Python server or virtual machine
⦁	CPU: 2 x 64-bit 2.8 GHz 8.00 GT/s CPUs
⦁	RAM: 32 GB (or 16 GB of 1600 MHz DDR3 RAM)
⦁	Storage: 300 GB. Additional storage space recommended if the repository will be used to store packages built by the customer. An empty repository requires only 2 GB.
⦁	Internet access to download the files from Anaconda.org or a USB or external hard drive containing all the files you need to install it.
Its software requirements are:
⦁	RHEL/CentOS 6.5 to 7.4, Ubuntu 12.04+ (Ubuntu users may need to install cURL.)
⦁	Client environment may be Windows, macOS, or Linux
⦁	MongoDB 2.6 (provided)
⦁	Anaconda Repository license file
⦁	Cron entry to start the repo on reboot
⦁	Linux system accounts (mongod (RHEL) or mongodb (Ubuntu)) (anaconda-server)
Its security requirements are:
⦁	Privileged access or sudo capabilities
⦁	Open HTTP(S) port
⦁	SELinux policy edit privileges (SELinux does not have to be disabled for Anaconda Repository operation) 
⦁	Optional: Ability to make iptables and modifications 
⦁	Optional: SSL certificate 
⦁	One of the following configurations should be used during installation:
⦁	Access to the PC root user with their password
⦁	Access to the PC root user with an SSH keypair
⦁	Passwordless SSH/sudo enabled for a user account
⦁	Password-based SSH and passwordless sudo enabled for a user account

Its network requirements are:
⦁	Inbound HTTP: TCP 8080, 8443 (Anaconda repository) 
⦁	Optional Inbound SSH: TCP 22 (SSH)
⦁	Optional Outbound HTTPS: TCP 443
⦁	Repo.anaconda.com
⦁	anaconda.org
⦁	conda.anaconda.org
⦁	binstar-cio-packages-prod.s3.amazonaws.com
⦁	820451f3d8380952ce654cc6343b423784e82fd202bb87cf87cf.ssl.cf1.rackcdn.com
⦁	Optional Outbound SMTP: TCP 25 (if not using AD/LDAP) email notifications
⦁	Optional Outbound LDAP(s): TCP 389/636 for authentication integration
It has some other requirements, too, which include:
⦁	License file provided to you by Anaconda at the time of purchase
⦁	Installation tokens for binstar and anaconda-server channels provided by Anaconda at the time of purchase. Not applicable for air gapped installs.
⦁	Optional: Your Anaconda.org account credentials. Not applicable for air gapped installs.
These have been the minimum requirements. The recommended hardware for running Anaconda is as follows:
⦁	RAM: 8+ GB
⦁	CPU: 8+ cores
⦁	Storage: 4 GB

Installation
The first step to installing Anaconda is to go it its website and choose a Python graphical installer. One can go to https://www.anaconda.com/products/distribution#windows (if using Windows) and download it there. 
Afterwards, locate your download and double click it to run it. You will then be greeted with the setup:
 
Click on “Next”
Afterwards, read through the license agreement. Should you agree, click on “I Agree”.
 
Click on “Next”
Next, you will have to choose the installation type. “Just Me” is the recommended option. Go ahead and choose that one, if you are going to be the only person using Anaconda on that computer. 
 
Make sure to install it to a place ideal to you.
 
The next step is of particular importance. It will be recommended to you that you should not add Anaconda to your path. If you do this, you will have to use the Anaconda Navigator or the Anaconda Command Prompt whenever you want to use Anaconda. If you want to be able to use Anaconda in your command prompt, make sure to check the box so that Anaconda is added to your path.
 
Go ahead and install Anaconda and complete the setup. Once it’s done, click on “Finish”
 
 

Contents
As previously mentioned Anaconda comes with and installs many different things by default. They are: “PyCharm”, “Visual Studio Code”, “QT Console”, “Spyder”, “Glueviz”, “Orange 3”, and “R Studio”. Let’s look at what each of these do:
PyCharm
PyCharm is one of many Integrated Development Environment’s (IDE) that allows Python developers to use many essential tools for Python, web and data science development. According to their website, PyCharm “provides smart code inspections, on-the-fly error highlighting and quick-fixes, along with automated code refactoring’s and rich navigation capabilities”(1).
Here is a picture of what one can expect when using PyCharm:

 
Visual Studio Code
Visual Studio code is described as a free source editor that supports Python with many features such as real-time collaboration. One can customize it in many different ways. It is further described as a good balance between authenticity and accessibility. Furthermore, Visual Studio Code (or “VSCode”), works on every OS (operating system, such as Windows, Linux, and Mac). 
Here is a picture of Visual Studio Code:
 Jupyter QtConsole
QtConsole can best be described as a lightweight application that closely resembles a terminal, but provides many enhancements such as syntax highlighting, graphical calltips, and more. QtConsole is able to save your session as either HTML or XHTML. You also have the option to save PNG images in separate folders. 
Here is a picture of QtConsole:
 
Spyder
Spyder, also known as the “Scientific Python Development Environment”, is a free integrated development environment that is included with Anaconda. It has features such as editing, debugging, testing and more. While it can be used for general Python development, it is best suited for scientific programming. 
Here is a picture of Spyder:
 
Glueviz
“Glueviz”, also known as “Glue”, is one of many Python libraries. Glue is used for exploring relationships among and within datasets. It has many features, which include: Linked Statistical Graphs (such as scatter plots or histograms), flexible linking across data (using logical links to display many sets of data)
Here is a picture of Glueviz:
 
Orange 3
The main functionality of “Orange” is data mining. It is a hierarchically-organized tool. The simpler procedures, such as data filtering, probability assessment and feature scoring, can then be integrated into higher-level algorithms. This makes it easy for programmers using “Orange” to add new functionality at any level and integrate into code that they’ve already written. “Orange” is often used by geographers, as well as people who work in many other sciences. 
Here is a picture of “Orange”:
 
R Studio
“R Studio” is another Integrated Development Environment one can use for Python programming. It is free, as well as open-source. A Python programmer can use “R Studio” to write scripts, import modules, and use Python. “R Studio” also provides code completion for Python scripts, in case you need help remembering. While “R Studio” is actually primarily used for statistical computing and graphics, it can also be used for Python programming.
Here is a picture of “R Studio”:
 

 “Pip” versus “Anaconda”
Let’s take a look at a programming package that is similar, but also quite different to Anaconda: “Pip”.
(Picture of “Pip”)
One of the fundamental differences between “Anaconda” and “Pip” is that “Anaconda” has support for many different programming languages, not just Python.  Different things are put in the respective packages. “Pip” packages only contain Python libraries, such as NumPy, or matplotlib, for example. If you install a library that isn’t from Python, you will get a message that says “out of scope”. “Anaconda” packages include many things including the previously mentioned Python libraries, such as C libraries, and executables such as C compilers. “Anaconda” only relies on the operating system for basic facilities, like the C library that is standard in every Windows operating system.
The clearest advantage for “Anaconda” over “Pip” is how much is included in it. It is much more convenient to have such a vast array of libraries available to the user, all in one package.

Conclusion
“Anaconda” is an incredibly convenient package that makes setting up one’s programming environment quick and painless. It might just be the best Python and R distribution available today. It is free and open-source (meaning the original source code is publicly available. There are many advantages to this, a main one being we can see what the developers did with their program, and didn’t put anything malicious in it). It has over 1500 Python/R data science packages. It makes managing and deploying packages easy. It allows one to use many different integrated development environments one can choose from, depending on necessity and preference. 
Whether a user is a new developer, or one with years of experience, “Anaconda” makes your programming life easier, simpler and more convenient.

Bibliography 
https://towardsdatascience.com/an-overview-of-the-anaconda-distribution-9479ff1859e6
https://www.jetbrains.com/help/pycharm/quick-start-guide.html
https://www.jetbrains.com/pycharm/ (1)
https://code.visualstudio.com/learn/educators/python#:~:text=Visual%20Studio%20Code%20is%20a,way%20you%20like%20to%20teach.
https://qtconsole.readthedocs.io/en/stable/
https://docs.anaconda.com/anaconda/user-guide/tasks/integration/spyder/#:~:text=Spyder%2C%20the%20Scientific%20Python%20Development,%2C%20debugging%2C%20and%20introspection%20features.
https://orangedatamining.com/
https://jmlr.org/papers/volume14/demsar13a/demsar13a.pdf
https://www.rstudio.com/about/
https://docs.anaconda.com/
https://www.datacamp.com/tutorial/installing-anaconda-windows
https://pythonspeed.com/articles/conda-vs-pip/#:~:text=The%20fundamental%20difference%20between%20pip,even%20the%20Python%20interpreter%20itself).


