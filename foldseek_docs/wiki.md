# Foldseek User Guide {#fs-user-guide}

This chapter focuses on operational readiness: platform prerequisites, installation strategies, memory planning, and troubleshooting patterns that affect real runs. For command selection and workflow design, continue to the [manual](#fs-manual).

## Platform and System Requirements {#fs-user-system-requirements}

Foldseek supports modern Linux and macOS environments. On x86_64 platforms, performance depends strongly on SIMD support. AVX2 is the fastest CPU path, while SSE4.1 and SSE2 compatibility paths exist for older hardware. ARM64 and PPC64LE are also supported with architecture-specific SIMD backends.

For production usage, validate CPU capabilities before benchmarking. A run that silently falls back to a lower SIMD tier can look like a configuration bug when it is actually a hardware-path mismatch.

### Quick CPU Capability Checks {#fs-user-simd-checks}

Linux:

```bash
[ $(uname -m) = "x86_64" ] && echo "64bit: Yes" || echo "64bit: No"
grep -q avx2 /proc/cpuinfo && echo "AVX2: Yes" || echo "AVX2: No"
grep -q sse4_1 /proc/cpuinfo && echo "SSE4.1: Yes" || echo "SSE4.1: No"
grep -q sse2 /proc/cpuinfo && echo "SSE2: Yes" || echo "SSE2: No"
```

macOS:

```bash
[ $(uname -m) = "x86_64" ] && echo "64bit: Yes" || echo "64bit: No"
sysctl machdep.cpu.leaf7_features | grep -q AVX2 && echo "AVX2: Yes" || echo "AVX2: No"
sysctl machdep.cpu.features | grep -q SSE4.1 && echo "SSE4.1: Yes" || echo "SSE4.1: No"
```

### GPU Requirements {#fs-user-gpu-requirements}

Foldseek supports CUDA acceleration for search workflows and ProstT5-assisted 3Di prediction. Full speed is typically achieved on Ampere-generation or newer NVIDIA GPUs, while older Tesla-generation hardware can still run with reduced throughput.

For GPU search and GPU-backed `createdb` runs, verify both driver/runtime compatibility and the command path (`--gpu`, plus workflow-specific constraints such as prefilter mode behavior).

## Memory Planning for Large Searches {#fs-user-memory}

Memory footprint is dominated by database representation and index settings. A practical baseline for structure-aware runs is:

```text
RAM ≈ (6 bytes C-alpha + 1 byte 3Di + 1 byte AA) × total residues
```

For AFDB50-scale workloads, this can exceed 100 GB depending on index and scoring mode. If you disable structure-bit sorting (`--sort-by-structure-bits 0`) and rely on paths that do not require C-alpha coordinates during ranking, effective runtime memory can drop substantially.

A safe planning approach is:

1. Estimate peak RAM from residue counts.
2. Decide whether coordinate-aware ranking/metrics are required.
3. Choose index subset/exclusion options that remain compatible with downstream scoring and output requirements.

## Installation Paths {#fs-user-installation}

### Precompiled Binaries {#fs-user-install-prebuilt}

Linux AVX2:

```bash
wget https://mmseqs.com/foldseek/foldseek-linux-avx2.tar.gz
tar xvzf foldseek-linux-avx2.tar.gz
export PATH=$(pwd)/foldseek/bin/:$PATH
```

Linux SSE4.1:

```bash
wget https://mmseqs.com/foldseek/foldseek-linux-sse41.tar.gz
tar xvzf foldseek-linux-sse41.tar.gz
export PATH=$(pwd)/foldseek/bin/:$PATH
```

macOS universal build:

```bash
wget https://mmseqs.com/foldseek/foldseek-osx-universal.tar.gz
tar xvzf foldseek-osx-universal.tar.gz
export PATH=$(pwd)/foldseek/bin/:$PATH
```

### Conda Installation {#fs-user-install-conda}

```bash
conda install -c conda-forge -c bioconda foldseek
```

### Build from Source (Linux CPU) {#fs-user-build-linux-cpu}

```bash
git clone https://github.com/steineggerlab/foldseek.git
cd foldseek
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=. ..
make -j$(nproc)
make install
export PATH=$(pwd)/bin/:$PATH
```

### Build from Source (Linux GPU) {#fs-user-build-linux-gpu}

```bash
conda create -n nvcc -c conda-forge cuda-nvcc cuda-cudart-dev libcublas-dev libcublas-static cuda-version=12.6 cmake
conda activate nvcc
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=. -DENABLE_CUDA=1 -DCMAKE_CUDA_ARCHITECTURES="75;80;86;89;90" ..
make -j8
make install
export PATH=$(pwd)/bin/:$PATH
```

### Build from Source (macOS) {#fs-user-build-macos}

Clang path:

```bash
brew install cmake libomp zlib bzip2
./util/build_osx.sh PATH_TO_FOLDSEEK_REPO OUTPUT_DIR
```

GCC path:

```bash
brew install cmake gcc@11 zlib bzip2
CC="gcc-14" CXX="g++-14" cmake -DCMAKE_BUILD_TYPE=RELEASE -DCMAKE_INSTALL_PREFIX=. ..
```

### Build Customization {#fs-user-build-customization}

Most relevant MMseqs2 CMake flags apply to Foldseek. For example, Google Cloud Storage support for `createdb` can be enabled using `vcpkg` and `-DHAVE_GCS=1`.

## Operational Checklist After Installation {#fs-user-postinstall}

Before starting large jobs:

1. Confirm `foldseek` is on `PATH` and binary architecture matches host capabilities.
2. Run a small `createdb` and `search` smoke test.
3. Validate temporary storage path throughput and capacity.
4. If using GPU, verify CUDA visibility and run one GPU-enabled search trial.

## FAQ and Troubleshooting {#fs-user-faq}

### What does Foldseek hit probability represent? {#fs-user-faq-probability}

Hit probability is an empirical estimate of true-positive likelihood as a function of structural bit score, calibrated on benchmark distributions. It is useful for ranking interpretation, not a direct replacement for domain-specific validation.

### Why can ranking change when `--sort-by-structure-bits` changes? {#fs-user-faq-structure-bits}

With structure-bit sorting enabled, ranking uses structural quality terms derived from TM/LDDT-aware scoring. Disabling it reverts ordering closer to raw bit-score behavior. E-values are not necessarily affected in the same way as ranking order.

### When should I use `--alignment-type 1` (TM-align) instead of `2` (3Di+AA)? {#fs-user-faq-alignment-type}

Use TM-align mode when global superposition quality is the primary objective. Use 3Di+AA when balancing structural and sequence evidence for high-throughput screening and clustering pipelines.

### Why do I get warnings about C-alpha data or disabled thresholds? {#fs-user-faq-ca-warnings}

Some scoring and filtering paths require coordinate channels (`_ca`). If the database layout omits required coordinate components, Foldseek disables incompatible threshold/ranking features to prevent invalid outputs.

### How do I apply `U` and `T` transforms to coordinates? {#fs-user-faq-ut-transform}

Foldseek reports transform parameters for superposition. For direct coordinate transformation workflows, you can use custom scripts or generate superposed outputs through `convert2pdb`/`convertalis` modes that already apply transforms.

### How can I align only specific known query-target pairs? {#fs-user-faq-pairwise}

Construct a custom prefilter DB containing only the desired pair IDs, then run `structurealign` on that prefilter result. A practical template is:

```bash
foldseek createdb inputs1/ db1
foldseek createdb inputs2/ db2

# Build a pair list mapped to internal IDs, then:
foldseek tsv2db keys.tsv pref --output-dbtype 7
foldseek structurealign db1 db2 pref aln
foldseek convertalis db1 db2 aln aln.m8
```

This approach avoids full all-vs-all candidate generation when pair identities are known in advance.
