# Strix Halo AI Toolboxes

This is a collection of containerized environments for running GenAI workloads on AMD Ryzen AI MAX+ "Strix Halo" (gfx1151).

## Repositories

*   **[Llama.cpp Toolboxes](https://github.com/kyuz0/amd-strix-halo-toolboxes)** - LLM Inference & Clustering (Vulkan/ROCm)
*   **[ComfyUI Toolboxes](https://github.com/kyuz0/amd-strix-halo-comfyui-toolboxes)** - Image & Video Generation (Flux, Wan, Hunyuan)
*   **[vLLM Toolboxes](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes)** - High-performance Serving & Clustering
*   **[LLM Fine-tuning](https://github.com/kyuz0/amd-strix-halo-llm-finetuning)** - Training & QLoRA

## Host Config

*   **OS**: Fedora 43 (Linux 6.18.5)
*   **Kernel Parameters**: `iommu=pt amdgpu.gttsize=126976 ttm.pages_limit=32505856`
*   **Tuning**: `tuned` via `accelerator-performance` profile.

## Links

*   [Strix Halo Home Lab](strixhalo.wiki)
*   [Join the Discord](https://discord.gg/pnPRyucNrG)

## Support

This is a hobby project that takes a lot of time to test and maintain. If you'd like to support my work, you can [buy me a coffee](https://buymeacoffee.com/dcapitella).