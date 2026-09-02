# Strix Halo AI Toolboxes

This is a collection of containerized environments for running GenAI workloads on AMD Ryzen AI MAX+ "Strix Halo" (gfx1151).

## Repositories

*   **[Llama.cpp Toolboxes](https://github.com/kyuz0/amd-strix-halo-toolboxes)** - LLM Inference & Clustering (Vulkan/ROCm)
*   **[ComfyUI Toolboxes](https://github.com/kyuz0/amd-strix-halo-comfyui-toolboxes)** - Image & Video Generation (Flux, Wan, Hunyuan)
*   **[vLLM Toolboxes](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes)** - High-performance Serving & Clustering
*   **[LLM Fine-tuning](https://github.com/kyuz0/amd-strix-halo-llm-finetuning)** - Training & QLoRA
*   **[AI Toolbox Cockpit](https://github.com/kyuz0/ai-toolbox-cockpit)** - TUI control center for managing compatible AI containers, models, and servers
*   **[DwarfStar](https://github.com/kyuz0/strix-halo-ds4-toolbox)** - A small native inference engine optimized first for DeepSeek V4 Flash
*   **[pi-bench](../pi-bench)** - Local coding benchmark repository for SWE-bench Verified Mini


## Recommended Workflow: AI Toolbox Cockpit

**[AI Toolbox Cockpit](https://github.com/kyuz0/ai-toolbox-cockpit)** is the easiest way to manage the supported AI environments. The TUI handles differences between operating systems, container engines, and backend workflows for llama.cpp, DS4, vLLM, and ComfyUI.

```sh
pipx install git+https://github.com/kyuz0/ai-toolbox-cockpit.git
ai-toolbox-cockpit
```

The host configuration below still applies. If you prefer to create and run containers yourself, use the manual Toolbox or Distrobox instructions on the [project website](https://kyuz0.github.io/amd-strix-halo-toolboxes/).

## Host Config

I tested these toolboxes on the following Fedora configuration. Fedora has a very strong and seamless implementation of `toolbox`.

*   **OS**: Fedora 43 (Linux 6.18.9-200)
*   **Kernel Parameters**: `amd_iommu=off amdgpu.gttsize=126976 ttm.pages_limit=32505856` (see per-OS setup below)
*   **Tuning**: `tuned` via `accelerator-performance` profile.

**Ubuntu / Debian / Ryzen AI Halo Users:** The default `toolbox` package on Ubuntu/Debian handles permissions differently than on Fedora, which can break GPU access. We recommend using **Distrobox** instead.

If you are on Ubuntu, Debian, or AMD's Ryzen AI Halo Debian-based distro, you must first set up these specific permissions:

```sh
# Add your user to required GPU groups
sudo usermod -aG video,render $USER

# Ensure the compute device is accessible (persists across reboots)
echo -e 'SUBSYSTEM=="kfd", KERNEL=="kfd", MODE="0666"\nSUBSYSTEM=="drm", KERNEL=="renderD*", MODE="0666"' | sudo tee /etc/udev/rules.d/70-kfd.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

> **Note:** This Distrobox configuration has been tested on **Ubuntu 25.10** with **Mainline Kernel 6.18.7-061807**. To enable mainline kernels on Ubuntu, you can use the [Ubuntu Mainline Kernel Installer](https://github.com/bkw777/mainline).
>
> **Ryzen AI Halo:** AMD's Ryzen AI Halo systems ship with a **Debian-based** distribution. The same Distrobox configuration and GPU permission setup above apply to those systems as well.

### Ryzen AI Halo / Debian Kernel Parameters (systemd-boot)

Ryzen AI Halo (Debian-based) uses **systemd-boot** (not GRUB). Kernel parameters are set differently:

**Memory configuration** — use `amd-ttm` instead of kernel parameters:

```sh
# Install pipx and amd-debug-tools
sudo apt install pipx
pipx ensurepath
pipx install amd-debug-tools

# Set unified memory to ~124 GB (replaces amdgpu.gttsize + ttm.pages_limit)
sudo amd-ttm --set 124
# Reboot when prompted
```

**IOMMU** — set `amd_iommu=off` via systemd-boot's cmdline file:

1. Open the kernel command-line file. `sudoedit` uses your configured editor:

```sh
sudoedit /etc/kernel/cmdline
```

2. Add a space followed by this value to the existing line. Keep every parameter already in the file:

```text
amd_iommu=off
```

3. Save and exit the editor, then rebuild the boot entry and reboot:

```sh
sudo kernel-install add "$(uname -r)" \
  "/boot/vmlinuz-$(uname -r)" \
  "/boot/initrd.img-$(uname -r)"

sudo reboot
```

> **Important:** Preserve the existing contents of `/etc/kernel/cmdline`; it contains the complete kernel command line. Do not edit generated entries in `/boot/loader/entries/` directly.


## Links

*   [Strix Halo Home Lab](https://strixhalo.wiki)
*   [Join the Discord](https://discord.gg/pnPRyucNrG)

## Support

This is a hobby project that takes a lot of time to test and maintain. If you'd like to support my work, you can [buy me a coffee](https://buymeacoffee.com/dcapitella).
