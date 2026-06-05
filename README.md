# Strix Halo AI Toolboxes

This is a collection of containerized environments for running GenAI workloads on AMD Ryzen AI MAX+ "Strix Halo" (gfx1151).

## Repositories

*   **[Llama.cpp Toolboxes](https://github.com/kyuz0/amd-strix-halo-toolboxes)** - LLM Inference & Clustering (Vulkan/ROCm)
*   **[ComfyUI Toolboxes](https://github.com/kyuz0/amd-strix-halo-comfyui-toolboxes)** - Image & Video Generation (Flux, Wan, Hunyuan)
*   **[vLLM Toolboxes](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes)** - High-performance Serving & Clustering
*   **[LLM Fine-tuning](https://github.com/kyuz0/amd-strix-halo-llm-finetuning)** - Training & QLoRA
*   **[Llama Cockpit](https://github.com/kyuz0/llama-toolboxes-cockpit)** - TUI control center for managing Llama.cpp toolboxes and models
*   **[DwarfStar](https://github.com/kyuz0/strix-halo-ds4-toolbox)** - A small native inference engine optimized first for DeepSeek V4 Flash
*   **[pi-bench](../pi-bench)** - Local coding benchmark repository for SWE-bench Verified Mini


## Host Config

I tested these toolboxes on the following Fedora configuration. Fedora has a very strong and seamless implementation of `toolbox`.

*   **OS**: Fedora 43 (Linux 6.18.9-200)
*   **Kernel Parameters**: `iommu=pt amdgpu.gttsize=126976 ttm.pages_limit=32505856`
*   **Tuning**: `tuned` via `accelerator-performance` profile.

**Ubuntu Users:** The default `toolbox` package on Ubuntu handles permissions differently than on Fedora, which can break GPU access. We recommend using **Distrobox** instead. 

If you are on Ubuntu, you must first set up these specific permissions:

```sh
# Add your user to required GPU groups
sudo usermod -aG video,render $USER

# Ensure the compute device is accessible (persists across reboots)
echo -e 'SUBSYSTEM=="kfd", KERNEL=="kfd", MODE="0666"\nSUBSYSTEM=="drm", KERNEL=="renderD*", MODE="0666"' | sudo tee /etc/udev/rules.d/70-kfd.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```

> **Note:** This Distrobox configuration has been tested on **Ubuntu 25.10** with **Mainline Kernel 6.18.7-061807**. To enable mainline kernels on Ubuntu, you can use the [Ubuntu Mainline Kernel Installer](https://github.com/bkw777/mainline).

## Llama Cockpit (TUI)

**[Llama Cockpit](https://github.com/kyuz0/llama-toolboxes-cockpit)** is a Terminal User Interface (TUI) that makes it easier to manage llama.cpp toolboxes and GGUF weights. It also includes a server mode that doesn't require toolbox or distrobox, running natively via docker/podman to ensure compatibility with any Linux distribution.

### Installation

Install via `pipx`:
```sh
pipx install git+https://github.com/kyuz0/llama-toolboxes-cockpit.git
```

### Usage
```sh
llama-cockpit
```


## Links

*   [Strix Halo Home Lab](https://strixhalo.wiki)
*   [Join the Discord](https://discord.gg/pnPRyucNrG)

## Support

This is a hobby project that takes a lot of time to test and maintain. If you'd like to support my work, you can [buy me a coffee](https://buymeacoffee.com/dcapitella).