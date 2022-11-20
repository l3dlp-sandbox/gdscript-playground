import version

if version.major == 3:
    platform = "server"
    target = "release_debug"
    optimize = "size"
    use_lto = "yes"
    use_static_cpp = "no"
    debug_symbols = "yes"
    deprecated = "no"
    minizip = "no"
    xaudio2 = "no"
    module_bmp_enabled = "no"
    module_bullet_enabled = "no"
    module_camera_enabled = "no"
    module_csg_enabled = "no"
    module_cvtt_enabled = "no"
    module_dds_enabled = "no"
    module_denoise_enabled = "no"
    module_enet_enabled = "no"
    module_etc_enabled = "no"
    module_fbx_enabled = "no"
    module_freetype_enabled = "yes"
    module_gdnative_enabled = "no"
    module_gdscript_enabled = "yes"
    module_gltf_enabled = "no"
    module_gridmap_enabled = "yes"
    module_hdr_enabled = "no"
    module_jpg_enabled = "no"
    module_jsonrpc_enabled = "no"
    module_lightmapper_cpu_enabled = "no"
    module_mbedtls_enabled = "yes"
    module_minimp3_enabled = "no"
    module_mobile_vr_enabled = "no"
    module_mono_enabled = "no"
    module_navigation_enabled = "yes" # crashes if disabled
    module_ogg_enabled = "no"
    module_opensimplex_enabled = "no"
    module_opus_enabled = "no"
    module_pvr_enabled = "no"
    module_raycast_enabled = "no"
    module_regex_enabled = "yes"
    module_squish_enabled = "no"
    module_stb_vorbis_enabled = "no"
    module_svg_enabled = "no"
    module_tga_enabled = "no"
    module_theora_enabled = "no"
    module_tinyexr_enabled = "no"
    module_upnp_enabled = "no"
    module_vhacd_enabled = "no"
    module_visual_script_enabled = "no"
    module_vorbis_enabled = "no"
    module_webm_enabled = "no"
    module_webp_enabled = "no"
    module_webrtc_enabled = "no"
    module_websocket_enabled = "no"
    module_webxr_enabled = "no"
    module_xatlas_unwrap_enabled = "no"

elif version.major == 4:
    dev_build = "no"
    platform = "linuxbsd"
    target = "editor"
    vulkan = "no"
    optimize = "size"
    use_lto = "yes"
    use_static_cpp = "no"
    debug_symbols = "no"
    deprecated = "no"
    minizip = "no"
    xaudio2 = "no"
    opengl3 = "no"
    x11 = "no"
    touch = "no"
    openxr = "no"
    module_basis_universal_enabled = "no"
    module_bmp_enabled = "no"
    module_camera_enabled = "no"
    module_csg_enabled = "no"
    module_cvtt_enabled = "no"
    module_dds_enabled = "no"
    module_denoise_enabled = "no"
    module_enet_enabled = "no"
    module_etcpak_enabled = "no"
    brotli = "no"
    module_freetype_enabled = "no"
    module_gdscript_enabled = "yes"
    module_glslang_enabled = "no"
    module_gltf_enabled = "no"
    module_gridmap_enabled = "yes"
    module_hdr_enabled = "no"
    module_jpg_enabled = "no"
    module_jsonrpc_enabled = "no"
    module_lightmapper_rd_enabled = "no"
    module_mbedtls_enabled = "yes"
    module_meshoptimizer_enabled = "no"
    module_minimp3_enabled = "no"
    module_mobile_vr_enabled = "no"
    module_mono_enabled = "no"
    module_msdfgen_enabled = "no"
    module_multiplayer_enabled = "no"
    module_navigation_enabled = "yes" # crashes if disabled
    module_noise_enabled = "no"
    module_ogg_enabled = "no"
    module_openxr_enabled = "no"
    module_raycast_enabled = "no"
    module_regex_enabled = "yes"
    module_squish_enabled = "no"
    module_svg_enabled = "no"
    graphite = "no"
    module_text_server_adv_enabled = "no"
    module_text_server_fb_enabled = "no"
    module_tga_enabled = "no"
    module_theora_enabled = "no"
    module_tinyexr_enabled = "no"
    module_upnp_enabled = "no"
    module_vhacd_enabled = "no"
    module_vorbis_enabled = "no"
    module_webp_enabled = "no"
    module_webrtc_enabled = "no"
    module_websocket_enabled = "no"
    module_webxr_enabled = "no"
    module_xatlas_unwrap_enabled = "no"
    module_zip_enabled = "no"