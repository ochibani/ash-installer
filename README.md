# ash-installer
Experimental installer for [AshOS](https://github.com/ashos/ashos).


# Prepare
It is very important that scripts in ./src/prep/ be executed (preparing live environment as well as partition/formatting) otherwise there would be error because time is not in sync etc. By default the installer will call these scripts, but if you want to do them manually, just comment the respective lines.


# Partition and format drive
* If installing on a BIOS system, use a dos (MBR) partition table.
* On EFI you can use GPT.
* The EFI partition has to be formatted to FAT32 before running the installer (```mkfs.fat -F32 /dev/<part>```).
* There are prep scripts under `./src/prep/`.

```
lsblk  # Find your drive name
cfdisk /dev/*** # Format drive, make sure to add an EFI partition, if using BIOS leave 2M free space before first partition
mkfs.btrfs /dev/*** # Create a btrfs filesystem, don't skip this step!
```


# Run installer
```
python3 setup.py /dev/<root_partition> /dev/<drive> [/dev/<efi part>] [distro_id] ["distro_name"]# Skip the EFI partition if installing in BIOS mode
```

