# v2.1.1
- All artifacts are CI-built: gadget downloaded from official frida release and patched in CI (no pre-committed binaries).
- gadget/ removed from git; rusda patch script moved to tools/.

# v2.1.0
- Upstream decoupled: Frida gadget is now self-hosted under `gadget/` (no download from taisuii/rusda).
- Frida kernel bumped to 17.22.1 with rusda anti-detection patch baked in (all ABIs: arm/arm64/x86/x86_64).
- Toolchain modernized: AGP 7.4.2 -> 8.6.1, Gradle wrapper 7.5 -> 8.9, targetSdk 32 -> 34.
- Zygisk native lib now rebuilt by CI from source (removed de.undercouch.download plugin).

# v2.0.2
- Unified system and JNI logging tag to KsuRusda
- Cleaned up all obsolete workflows and project metadata
- Optimized WebUI language cache storage key

# v2.0.1
- Integrated taisuii/rusda anti-detection Frida core (v17.15.0) to eliminate thread and RPC detection traces
- Rebranded and streamlined WebUI with responsive mobile layout and ultra-fast lazy loading
- Added offline script injection mode for applications without internet permissions
- Implemented atomic safe config persistence and instant target toggling
- Upgraded build system with modern Java 17, Android NDK 25 LTS toolchain, and CI automation
- Standardized project licensing, derivative documentation, and comprehensive upstream credits

# v1.9.20
- Fixed WebUI-saved config file permissions so the target app can read them (thanks @limbang, #7)

# v1.9.4
- Frida gadget updated to 17.9.1
- Switched to own patched Frida fork
- Added auto-update workflow

# v1.9.3
- Auto-update support via KernelSU/Magisk Manager
- Updated docs to match current config schema
- Fixed child gating modes in WebUI
- Default gadget config set to listen mode

# v1.9.2
- Rebranded to KsuFrida
- Removed Riru support (Zygisk only)
- Rewrote WebUI with dark theme
- Fixed ksu.exec callback mechanism
- Added kernel_assisted_evasion toggle
- Added app labels in WebUI target list
- Fixed cpplint errors
