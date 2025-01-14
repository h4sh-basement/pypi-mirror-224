# Auterion CLI

Command line utility to interact with Auterion Devices and Apps


**Type `auterion-cli --help` in your command line to get help.**<br/>
For help for a sub-command, type `auterion-cli <subcommand> --help`



### Contents

- [Installation](#installation)
- [Command reference](#command-reference)
- [Example usage - app development](#app-dev-workflow)


## Installation
<a name="installation"></a>

Use pip

```
pip3 install auterion-cli
```

This will install in your local user directory. 

**Note:** Make sure your `~/.local/bin` directory is in the `PATH` to access it.

## Command reference
<a name="command-reference"></a>

### Discover / select devices

"Selecting" a device makes auterion-cli perform all actions against that selected device. 
In case no device is selected, auterion-cli will default to any device reachable on `10.41.1.1`

- `auterion-cli device discover`: Discover reachable auterion devices
- `auterion-cli device select <serial>`: Select a reachable device to connect to
- `auterion-cli device deselect`: De-select any currently selected device

### Device information

- `auterion-cli info`: Get information about the selected device
- `auterion-cli report`: Download diagnostic report from selected device

### App management

- `auterion-cli app list`: List all currently installed apps on the device
- `auterion-cli app start <app name>`: Start a stopped app
- `auterion-cli app stop <app name>`: Stop a running app
- `auterion-cli app restart <app name>`: Restart an app
- `auterion-cli app enable <app name>`: Enable autostart for an app
- `auterion-cli app disable <app name>`: Disable autostart for an app
- `auterion-cli app status <app name>`: Get current status for an app
- `auterion-cli app logs <app name> [-f]`: Display logs for an app. `-f` for live log feed

### Development workflow

- `auterion-cli app init`: Create a new app project
- `auterion-cli app build`: Build the app project in current folder. Creates *.auterionos* file in build folder.
- `auterion-cli app install <file>`: Install the *.auterionos* app file to skynode



## Workflow - App development
<a name="app-dev-workflow"></a>


### Step 1: Bootstrap a new app

In the first step, we instantiate a base template for our app.

```
auterion-cli app init
```

This creates a directory named `app-template-cpp` with a base application structure.
You can open this directory and look and edit the files.

### Step 2: Build the app

Go to the directory where you bootstrapped your app. Run

```
auterion-cli app build
```

To build your app. If this succeeds, it will generate a `.auterionos` file in a `build` sub-directory


### Step 3: Make sure the app-base is installed on your skynode

In case the app build command notified you with a message like this:

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                      │
│  Your app requires app auterion app-base-v0 to be installed on your device.          │
│                                                                                      │
│  Get app-base-v0.auterionos from                                                     │
│  https://github.com/Auterion/app-base/releases/download/v0/app-base-v0.auterionos    │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

You need an *app-base* to be installed on your skynode for your app to run.
To verify that you have the app-base installed, you can run

```
auterion-cli app list
```

In case you don't have the app base installed yet, download it from the link indicted, and install it with 

```
auterion-cli app install <PATH TO>/app-base-v0.auterionos

```



### Step 4: Install your app

You can install your app with 

```
auterion-cli app install build/<YOUR APP>.auterionos
```

This will install the app on your skynode.


### Step 5: Verify that your app is working

To see if your app is installed and running, you can run

```
auterion-cli app list
```


You can get a live feed of the logs of your app with

```
auterion-cli app logs <YOUR APP> -f
```

