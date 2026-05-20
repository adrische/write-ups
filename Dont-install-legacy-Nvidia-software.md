I have a Nvidia GeForce GTX 1050 Ti which is based on the Pascal architecture that is no longer supported by Nvidia. For example, the up to date version of Nsight Compute is not working for it. So I tried to install an older version of Nsight Compute that still supports my card. This brought an entire rat's tail of required downgrades of dependent software with it.

Originally, I tried to follow
https://forums.developer.nvidia.com/t/bandwidthtest-example-throws-cudaerrorcallrequiresnewerdriver-error-when-launched-via-nv-nsight-cu-cli/278698/10
This didn't work verbatim, and I'll describe how.

I have Ubuntu 22.04.

#### Prerequisites:
* Have possibility to reinstall Ubuntu (e.g., bootable USB stick)
* Save all data
* Have second means of getting help / access to internet
* Be somewhat comfortable with the command line
* Be ready to restart a lot (basically in-between all operations, especially after everything affecting drivers and other Nvidia software)
* Have a lot of time (~ 1 day)
* Be ready to read error logs
* Find out how to go to Grub and BIOS on your machine

#### Helpful commands/programs:
* Kernel version: `uname -r`
* Install kernels with mainline program. Start GUI from command line with `mainline-gtk`
* Make symlinks: `sudo ln -s link/path original/path`, mainly in /usr/local/
* Edit paths in `~/.bashrc`, then `. ~/.bashrc`
* What Nvidia packages are installed: `sudo dpkg -l | grep *nvidia*`
* Apt: `sudo apt update`, `sudo apt autoremove`, `sudo apt install`, `sudo apt remove --purge the_package`
* Add executable: `chmod +x file`
* `nvidia-smi` to check communication of driver with graphics card

#### Kernel downgrade:
* Via program mainline. E.g. kernel 6.8.12-060812-generic (!this one actually did not work for me with Nvidia driver 470! Potentially need an even older kernel if you really want driver 470)
* Set grub boot options to enable default boot from this kernel https://askubuntu.com/questions/216398/set-older-kernel-as-default-grub-entry
* I needed to disable secure boot in BIOS

#### In new kernel:
* Remove all Nvidia packages: `sudo apt remove --purge *nvidia*`
* Add driver repo: https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa
* Install driver first (with same `gcc`, `g++` versions as kernel was built with, likely version 13, i.e., `gcc --version` should return 13): `sudo apt install nvidia-driver-535`

#### Install Nvidia software:
* Need `gcc` and `g++` versions 9: `sudo apt install gcc-9 g++-9`, set up symlinks in `/usr/local/` to `gcc` and `g++`; `gcc --version` should return 9
* Install Nvidia toolkit 11.4 (for Ubuntu 20.04, but ignore), but don't install the driver that comes with it
* Add Cuda to `PATH` and `LD_LIBRARY_PATH` in `~/.bashrc` (will be mentioned at end of toolkit installation), `. ~/.bashrc`
* Nsight Compute 2019.5: Install via separate installation. The installation path cannot have spaces in it.

#### Test everything:
* Restart again
* `nvidia-smi` should work at this point
* Try make cuda samples (`deviceQuery`) (need corresponding samples release 11.4)
* Also try `nvcc` some toy program (needs `gcc` and apparently `g++` again versions 9)
* Try `nv-nsight-cu-cli ./some_toy_program` but `nv-nsight-cu-cli --version` should be 2019.5; if not: add to PATH


#### Things that happened in-between:
* Lost Wi-Fi (fix by booting into different kernel)
* Broke apt / dpkg and needed to reinstall Ubuntu
* Needed to fall back to internal graphics card (i.e., the nouveau fall-back driver was also not working, or at least not selected by default)


#### Upshot: 
I learned a lot, but depending on how you value your time, consider getting a GPU that's still supported https://en.wikipedia.org/wiki/CUDA#GPUs_supported, e.g., 20 series (as of writing).
