# AMD Strix Halo Toolboxes & Compatibility

This is a collection of toolboxes I maintain for running AI workloads on AMD Ryzen AI Max "Strix Halo" (gfx1151). It tracks what works and what doesn't for LLMs, image generation, and fine-tuning.

## ⚠️ Compatibility Matrix: Kernel vs ROCm

**Critical Warning:** Stability depends heavily on the kernel/ROCm combination. 

| Linux Kernel | ROCm Version | Status on Strix Halo | Notes |
| :--- | :--- | :--- | :--- |
| **≤ 6.18.3** | ROCm 6.4.x | ⚠ **Instability issues** | Can be unstable under certain AI workloads (e.g., ComfyUI). |
| **≤ 6.18.3** | ROCm 7.1.x | ⚠ **Instability issues** | Can be unstable under certain AI workloads (e.g., ComfyUI). |
| **≤ 6.18.3** | ROCm nightly | ⚠ **Instability issues** | Can be unstable under certain AI workloads (e.g., ComfyUI). |
| **≥ 6.18.4** | ROCm 6.4.x | ❌ **Incompatible\*** | Immediate crashes due to kernel/ROCm VGPR mismatch. |
| **≥ 6.18.4** | ROCm 7.1.x | ❌ **Incompatible\*** | Same incompatibility — not a regression, just mismatch. |
| **≥ 6.18.4** | ROCm 7.2+ | ✔ **Works** | Future release. Will include the same fixes found in nightly. |
| **≥ 6.18.4** | ROCm nightly (TheRock) | ✔ **Works** | Includes the VGPR fixes; this is the current stable path. |

*\*Note: Some distributions may backport patches or AMD may release point-release updates (e.g., 6.4.5) to address this.*

### 🚨 Firmware Warning
`linux-firmware-20251125` has a regression that breaks ROCm. You **must** either:
* **Downgrade** to `20251111`, OR
* **Update** to `20260110` (or newer).

---

## 📦 Active Toolboxes

* [**1. Llama.cpp Toolboxes**](#1-llamacpp-toolboxes) – LLM Inference & Clustering
* [**2. ComfyUI Toolboxes**](#2-comfyui-toolboxes) – Image/Video Generation
* [**3. LLM Fine-tuning**](#3-llm-fine-tuning) – Training & QLoRA
* [**4. vLLM Toolboxes**](#4-vllm-toolboxes) – High-performance Serving

### 1. Llama.cpp Toolboxes
**Repo:** [kyuz0/amd-strix-halo-toolboxes](https://github.com/kyuz0/amd-strix-halo-toolboxes)

The main toolbox for running `llama.cpp`. Pre-built containers for Fedora (Toolbx) and works on Ubuntu (via Distrobox).

* **Stable Configs:**
    * Kernel `6.18.3` + ROCm 6.4.4 / ROCm 7.1.1 / ROCm 7 Nightly Builds.
    * Kernel `6.18.4+` + ROCm 7 Nightly Builds.
* **Details:**
    * **Backends:** Vulkan (RADV/AMDVLK) & ROCm (6.4.4, 7.1.1, Nightly Builds).
    * **Tools:** `run_distributed_llama.py` (Cluster inference TUI) and `gguf-vram-estimator.py`.
* **Usage:** You must use `-fa 1 --no-mmap` or it will crash.

### 2. ComfyUI Toolboxes
**Repo:** [kyuz0/amd-strix-halo-comfyui-toolboxes](https://github.com/kyuz0/amd-strix-halo-comfyui-toolboxes)

Fedora toolbox with a ROCm environment (TheRock Nightlies) set up for image & video generation.

* **Workflows:** Qwen Image, Qwen Image Edit, Wan 2.2, HunyuanVideo 1.5.
* **Config:** Pre-configured with `--disable-mmap`, `--cache-none` and `--bf16-vae`.
* **Benchmarks:** [View Performance Benchmarks](https://kyuz0.github.io/amd-strix-halo-comfyui/)

### 3. LLM Fine-tuning
**Repo:** [kyuz0/amd-strix-halo-llm-finetuning](https://github.com/kyuz0/amd-strix-halo-llm-finetuning)

Environment for fine-tuning running ROCm 7 Nightly Builds with Jupyter Lab.

* **Models:** Gemma-3, Qwen-3, GPT-OSS-20B (MXFP4).
* **Methods:** Full Fine-Tuning (small models) and QLoRA.

### 4. vLLM Toolboxes
**Repo:** [kyuz0/amd-strix-halo-vllm-toolboxes](https://github.com/kyuz0/amd-strix-halo-vllm-toolboxes)

Serving container built on Fedora 43 and TheRock Nightly Builds.

* **Features:** `start-vllm` TUI wizard for launching models.
* **Context:** Validated 128k on Llama 3.1 8B, GPT-OSS-120B; 256k on Qwen3-Coder-30B.

---

## 🛑 Retired / Unmaintained

I'm not updating these anymore. Use the active ones above.

* **[amd-strix-halo-image-video-toolboxes](https://github.com/kyuz0/amd-strix-halo-image-video-toolboxes)**
    * ❌ **Retired** (Use *ComfyUI Toolboxes* instead)
* **[amd-strix-halo-voice-toolbox](https://github.com/kyuz0/amd-strix-halo-voice-toolbox)**
    * ❌ **Retired**
