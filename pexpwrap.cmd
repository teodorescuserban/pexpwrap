alicreate "dc_hp_dmz_49", "10:00:00:00:c9:e2:5a:32" 
alicreate "dc_ds5100_up_ch1", "20:16:00:a0:b1:47:be:2c"
alicreate "dc_ds5100_up_ch2", "20:26:00:a0:b1:47:be:2c"
alicreate "dc_ds_5100_ch1", "20:17:00:a0:b1:47:be:2c"
alicreate "dc_ds_5100_ch2", "20:27:00:a0:b1:47:be:2c"
alicreate "dc_svc4_port4", "50:05:07:68:03:40:65:0f"
alicreate "dc_svc4_port3", "50:05:07:68:03:30:65:0f"

zonecreate "dc_bkp_197_to_dc_ts3200_215", "dc_bkp_197; dc_ts3200_215"
zonecreate "dc_hp_dmz_49_to_svc_f1", "dc_hp_dmz_49; dc_svc4_port3; dc_svc3_port1; dc_svc2_port3; dc_svc_port1"
zonecreate "dc_hp_dmz_50_to_svc_f1", "dc_hp_dmz_50; dc_svc4_port3; dc_svc3_port1; dc_svc2_port3; dc_svc_port1"

# do not forget to run cfgsave and cfgenable :)
