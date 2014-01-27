# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class DivT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    div_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    div_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    lang_typ = models.BigIntegerField()
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    comp_typ_grp_cd = models.CharField(max_length=48, blank=True)
    itm_grp_cd = models.CharField(max_length=48, blank=True)
    mnft_num_defd_yn = models.CharField(max_length=1)
    fb_num_defd_yn = models.CharField(max_length=1)
    invc_num_defd_yn = models.CharField(max_length=1)
    addr_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."div_t"'    
#        db_table = u'div_t'

class DllT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dll_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dll_cd = models.CharField(max_length=30)
    dll_desc = models.CharField(max_length=280, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dll_t"'

class DeleteArfnclDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fncl_ctl_id = models.BigIntegerField()
    delete_ctl_id = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    chrg_detl_id = models.BigIntegerField(null=True, blank=True)
    chrg_detl_stat_id = models.BigIntegerField(null=True, blank=True)
    chrg_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pymnt_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_lvl_enu = models.BigIntegerField(null=True, blank=True)
    vchrar_num = models.CharField(max_length=48, blank=True)
    vchrar_opstat_cd = models.BigIntegerField(null=True, blank=True)
    vchrar_hold = models.CharField(max_length=1, blank=True)
    vchrar_held = models.CharField(max_length=1, blank=True)
    vchrar_crtd_dtt = models.DateField(null=True, blank=True)
    vchrar_updt_dtt = models.DateField(null=True, blank=True)
    invcd_id = models.BigIntegerField(null=True, blank=True)
    invcd_cur_stat_id = models.BigIntegerField(null=True, blank=True)
    invc_id = models.BigIntegerField(null=True, blank=True)
    invc_cur_stat_id = models.BigIntegerField(null=True, blank=True)
    invc_hold = models.CharField(max_length=1, blank=True)
    invc_held = models.CharField(max_length=1, blank=True)
    invc_crtd_dtt = models.DateField(null=True, blank=True)
    invc_updt_dtt = models.DateField(null=True, blank=True)
    gl_id = models.BigIntegerField(null=True, blank=True)
    gl_cur_stat_id = models.BigIntegerField(null=True, blank=True)
    gl_crtd_dtt = models.DateField(null=True, blank=True)
    gl_updt_dtt = models.DateField(null=True, blank=True)
    deleted_yn = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."delete_arfncl_detl_t"'

class MvCompletedByCustomer(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shipment_id = models.CharField(max_length=120, blank=True)
    shipment_tracking_number = models.CharField(max_length=280, blank=True)
    origin_location_code = models.CharField(max_length=64)
    origin_location_type = models.CharField(max_length=9, blank=True)
    origin_city = models.CharField(max_length=280)
    origin_state = models.CharField(max_length=16)
    origin_country = models.CharField(max_length=16)
    destination_location_code = models.CharField(max_length=64)
    destination_location_type = models.CharField(max_length=9, blank=True)
    destination_city = models.CharField(max_length=280)
    destination_state = models.CharField(max_length=16)
    destination_country = models.CharField(max_length=16)
    pickup_datetime = models.DateField()
    scale_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    weight_unit_of_measure = models.CharField(max_length=48, blank=True)
    event_reason_code = models.CharField(max_length=70, blank=True)
    division_code = models.CharField(max_length=16)
    reported_delivery_datetime = models.DateField(null=True, blank=True)
    customer_code = models.CharField(max_length=64)
    class Meta:
        db_table = u'"I2TM_APP"."mv_completed_by_customer"'

class MvMissingPodsByCarrier(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shipment_id = models.CharField(max_length=120, blank=True)
    shipment_tracking_number = models.CharField(max_length=280, blank=True)
    carrier_tracking_number = models.CharField(max_length=120, blank=True)
    customer_code = models.CharField(max_length=64)
    load_id = models.BigIntegerField(null=True, blank=True)
    load_description = models.CharField(max_length=280, blank=True)
    shipment_leg_id = models.BigIntegerField(null=True, blank=True)
    shipment_leg_sequence = models.BigIntegerField()
    stop_sequence = models.BigIntegerField(null=True, blank=True)
    origin_location_code = models.CharField(max_length=64)
    origin_location_type = models.CharField(max_length=19, blank=True)
    origin_city = models.CharField(max_length=280)
    origin_state = models.CharField(max_length=16)
    origin_country = models.CharField(max_length=16)
    destination_location_code = models.CharField(max_length=64)
    destination_location_type = models.CharField(max_length=19, blank=True)
    destination_city = models.CharField(max_length=280)
    destination_state = models.CharField(max_length=16)
    destination_country = models.CharField(max_length=16)
    scale_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    weight_unit_of_measure = models.CharField(max_length=48, blank=True)
    scheduled_arrival_datetime = models.DateField(null=True, blank=True)
    confirmation_datetime = models.DateField(null=True, blank=True)
    division_code = models.CharField(max_length=16)
    reported_delivery_datetime = models.DateField(null=True, blank=True)
    carrier_code = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mv_missing_pods_by_carrier"'

class MvMissingPodsByCustomer(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shipment_id = models.CharField(max_length=120, blank=True)
    shipment_tracking_number = models.CharField(max_length=280, blank=True)
    carrier_code = models.CharField(max_length=64, blank=True)
    load_id = models.BigIntegerField(null=True, blank=True)
    load_description = models.CharField(max_length=280, blank=True)
    origin_location_code = models.CharField(max_length=64)
    origin_location_type = models.CharField(max_length=19, blank=True)
    origin_city = models.CharField(max_length=280)
    origin_state = models.CharField(max_length=16)
    origin_country = models.CharField(max_length=16)
    destination_location_code = models.CharField(max_length=64)
    destination_location_type = models.CharField(max_length=19, blank=True)
    destination_city = models.CharField(max_length=280)
    destination_state = models.CharField(max_length=16)
    destination_country = models.CharField(max_length=16)
    scale_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    weight_unit_of_measure = models.CharField(max_length=48, blank=True)
    scheduled_arrival_datetime = models.DateField(null=True, blank=True)
    confirmation_datetime = models.DateField(null=True, blank=True)
    division_code = models.CharField(max_length=16)
    reported_delivery_datetime = models.DateField(null=True, blank=True)
    customer_code = models.CharField(max_length=64)
    class Meta:
        db_table = u'"I2TM_APP"."mv_missing_pods_by_customer"'

class MvUndeliveredByCarrier(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shipment_id = models.CharField(max_length=120, blank=True)
    shipment_tracking_number = models.CharField(max_length=280, blank=True)
    carrier_tracking_number = models.CharField(max_length=120, blank=True)
    customer_code = models.CharField(max_length=64)
    load_id = models.BigIntegerField(null=True, blank=True)
    load_description = models.CharField(max_length=280, blank=True)
    shipment_leg_id = models.BigIntegerField(null=True, blank=True)
    shipment_leg_sequence = models.BigIntegerField()
    stop_sequence = models.BigIntegerField(null=True, blank=True)
    origin_location_code = models.CharField(max_length=64)
    origin_location_type = models.CharField(max_length=19, blank=True)
    origin_city = models.CharField(max_length=280)
    origin_state = models.CharField(max_length=16)
    origin_country = models.CharField(max_length=16)
    destination_location_code = models.CharField(max_length=64)
    destination_location_type = models.CharField(max_length=19, blank=True)
    destination_city = models.CharField(max_length=280)
    destination_state = models.CharField(max_length=16)
    destination_country = models.CharField(max_length=16)
    scale_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    weight_unit_of_measure = models.CharField(max_length=48, blank=True)
    pickup_datetime = models.DateField()
    crystal_sort_datetime = models.DateField(null=True, blank=True)
    division_code = models.CharField(max_length=16)
    scheduled_arrival_datetime = models.DateField(null=True, blank=True)
    invalid_scheduled_arrival_yn = models.CharField(max_length=1, blank=True)
    carrier_code = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mv_undelivered_by_carrier"'

class MvUndeliveredByCustomer(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shipment_id = models.CharField(max_length=120, blank=True)
    shipment_tracking_number = models.CharField(max_length=280, blank=True)
    status_code = models.CharField(max_length=280, blank=True)
    origin_location_code = models.CharField(max_length=64)
    origin_location_type = models.CharField(max_length=19, blank=True)
    origin_city = models.CharField(max_length=280, blank=True)
    origin_state = models.CharField(max_length=16, blank=True)
    origin_country = models.CharField(max_length=16, blank=True)
    destination_location_code = models.CharField(max_length=64)
    destination_location_type = models.CharField(max_length=19, blank=True)
    destination_city = models.CharField(max_length=280, blank=True)
    destination_state = models.CharField(max_length=16, blank=True)
    destination_country = models.CharField(max_length=16, blank=True)
    from_delivery_datetime = models.DateField()
    to_delivery_datetime = models.DateField()
    scale_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    weight_unit_of_measure = models.CharField(max_length=48, blank=True)
    scheduled_arrival_datetime = models.DateField(null=True, blank=True)
    confirmation_datetime = models.DateField(null=True, blank=True)
    division_code = models.CharField(max_length=16)
    cutoff_datetime = models.DateField(null=True, blank=True)
    customer_code = models.CharField(max_length=64)
    class Meta:
        db_table = u'"I2TM_APP"."mv_undelivered_by_customer"'

class MvUnscheduledByCustomer(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shipment_id = models.CharField(max_length=120, blank=True)
    shipment_tracking_number = models.CharField(max_length=280, blank=True)
    status_code = models.CharField(max_length=280, blank=True)
    shipment_leg_sequence = models.BigIntegerField()
    origin_location_code = models.CharField(max_length=64)
    origin_location_type = models.CharField(max_length=19, blank=True)
    origin_city = models.CharField(max_length=280)
    origin_state = models.CharField(max_length=16)
    origin_country = models.CharField(max_length=16)
    destination_location_code = models.CharField(max_length=64)
    destination_location_type = models.CharField(max_length=19, blank=True)
    destination_city = models.CharField(max_length=280)
    destination_state = models.CharField(max_length=16)
    destination_country = models.CharField(max_length=16)
    from_pickup_datetime = models.DateField()
    to_pickup_datetime = models.DateField()
    from_delivery_datetime = models.DateField()
    to_delivery_datetime = models.DateField()
    scale_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    weight_unit_of_measure = models.CharField(max_length=48, blank=True)
    division_code = models.CharField(max_length=16)
    first_shipment_leg_yn = models.CharField(max_length=1, blank=True)
    previous_shipment_leg_status = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    previous_shipment_leg_eta = models.DateField(null=True, blank=True)
    customer_code = models.CharField(max_length=64)
    class Meta:
        db_table = u'"I2TM_APP"."mv_unscheduled_by_customer"'

class DeleteDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    delete_detl_id = models.BigIntegerField()
    delete_ctl_id = models.BigIntegerField(null=True, blank=True)
    ll_id = models.BigIntegerField(null=True, blank=True)
    ll_opstat_cd = models.BigIntegerField(null=True, blank=True)
    ll_fnclstat_cd = models.BigIntegerField(null=True, blank=True)
    ll_crtd_dtt = models.DateField(null=True, blank=True)
    ll_updt_dtt = models.DateField(null=True, blank=True)
    ll_mnft_ld_grp_cd = models.CharField(max_length=16, blank=True)
    lld_id = models.BigIntegerField(null=True, blank=True)
    lld_opstat_cd = models.BigIntegerField(null=True, blank=True)
    lld_fnclstat_cd = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    shpm_opstat_cd = models.BigIntegerField(null=True, blank=True)
    shpm_fnclstat_cd = models.BigIntegerField(null=True, blank=True)
    shpm_crtd_dtt = models.DateField(null=True, blank=True)
    shpm_updt_dtt = models.DateField(null=True, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    to_opstat_cd = models.BigIntegerField(null=True, blank=True)
    to_crtd_dtt = models.DateField(null=True, blank=True)
    to_updt_dtt = models.DateField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    trip_opstat_cd = models.BigIntegerField(null=True, blank=True)
    trip_fnclstat_cd = models.BigIntegerField(null=True, blank=True)
    trip_crtd_dtt = models.DateField(null=True, blank=True)
    trip_updt_dtt = models.DateField(null=True, blank=True)
    plan_id = models.BigIntegerField(null=True, blank=True)
    que_id = models.BigIntegerField(null=True, blank=True)
    misc = models.CharField(max_length=2000, blank=True)
    unattached_shpm = models.BigIntegerField(null=True, blank=True)
    deleted_yn = models.CharField(max_length=1, blank=True)
    delete_shpm_yn = models.CharField(max_length=1, blank=True)
    ll_lgst_grp = models.CharField(max_length=16, blank=True)
    lld_lgst_grp = models.CharField(max_length=16, blank=True)
    ll_cust_cd = models.CharField(max_length=64, blank=True)
    lld_cust_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."delete_detl_t"'

class DeleteCtlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    delete_ctl_id = models.BigIntegerField()
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    plan_id = models.BigIntegerField(null=True, blank=True)
    que_id = models.BigIntegerField(null=True, blank=True)
    delatable = models.CharField(max_length=1, blank=True)
    misc = models.CharField(max_length=2000, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."delete_ctl_t"'

class AptT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    apt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    apt_athy_num = models.CharField(max_length=120, blank=True)
    apt_with_name = models.CharField(max_length=128, blank=True)
    apt_frm_dtt = models.DateField()
    apt_to_dtt = models.DateField()
    cur_stat_id = models.BigIntegerField()
    ovrd_hrs_op_yn = models.CharField(max_length=1, blank=True)
    rqrdtrdgptnr_yn = models.CharField(max_length=1, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    pot_rrat_rqrd_yn = models.CharField(max_length=1)
    last_sec_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."apt_t"'

class Accessgroup(models.Model):
    allow_sync = True
    connection_name = 'tm'
    groupname = models.CharField(max_length=255)
    combinator = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."accessgroup"'

class AccgPridT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    opt_lck = models.BigIntegerField()
    strd_dt = models.DateField()
    endd_dt = models.DateField()
    ar_clsd_dtt = models.DateField(null=True, blank=True)
    ap_clsd_dtt = models.DateField(null=True, blank=True)
    gl_clsd_dtt = models.DateField(null=True, blank=True)
    ar_clsd_usr_cd = models.CharField(max_length=40, blank=True)
    ap_clsd_usr_cd = models.CharField(max_length=40, blank=True)
    gl_clsd_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."accg_prid_t"'

class AcrlRunT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    run_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    sent_to_tms = models.BigIntegerField()
    num_enty_crtd = models.BigIntegerField()
    ap_acrl_ver_cd = models.CharField(max_length=40, blank=True)
    ar_acrl_ver_cd = models.CharField(max_length=40, blank=True)
    endd_dtt = models.DateField(null=True, blank=True)
    iniprtd_crtd_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    prly_prgd_yn = models.CharField(max_length=1)
    que_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=4000, blank=True)
    excl_carr_yn = models.CharField(max_length=1)
    cust_cd = models.CharField(max_length=4000, blank=True)
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."acrl_run_t"'

class AcrlVerApT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    acrl_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    acrl_ver_desc = models.CharField(max_length=280)
    cut_off_adj_day = models.BigIntegerField()
    prt_rgst_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=4000, blank=True)
    strt_adj_day = models.BigIntegerField()
    excl_carr_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."acrl_ver_ap_t"'

class AcrlVerArT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    acrl_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    acrl_ver_desc = models.CharField(max_length=280)
    cut_off_adj_day = models.BigIntegerField()
    prt_rgst_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    cust_cd = models.CharField(max_length=4000, blank=True)
    strt_adj_day = models.BigIntegerField()
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."acrl_ver_ar_t"'

class AddrvbtchqueT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    que_id = models.BigIntegerField()
    srvr_id = models.BigIntegerField(null=True, blank=True)
    que_dtt = models.DateField()
    strt_dtt = models.DateField()
    cpld_dtt = models.DateField(null=True, blank=True)
    prty = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    disd_yn = models.CharField(max_length=1)
    usr_cd = models.CharField(max_length=44, blank=True)
    opt_lck = models.BigIntegerField()
    targ_cus_yn = models.CharField(max_length=1)
    targ_carr_yn = models.CharField(max_length=1)
    targ_salespsn_yn = models.CharField(max_length=1)
    targ_ldat_yn = models.CharField(max_length=1)
    targ_cnse_yn = models.CharField(max_length=1)
    targ_dc_yn = models.CharField(max_length=1)
    targ_hub_yn = models.CharField(max_length=1)
    targ_shpg_yn = models.CharField(max_length=1)
    vldt_vld_yn = models.CharField(max_length=1)
    vldt_invld_yn = models.CharField(max_length=1)
    vldt_nonvld_yn = models.CharField(max_length=1)
    addr_chng_yn = models.CharField(max_length=1)
    pstl_vldn_yn = models.CharField(max_length=1)
    vldt_schd_enu = models.BigIntegerField()
    schd_itvl = models.BigIntegerField(null=True, blank=True)
    msg_log_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."addrvbtchque_t"'

class AddrFmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    addr_fmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField(null=True, blank=True)
    fmt_value_cd = models.CharField(max_length=200)
    class Meta:
        db_table = u'"I2TM_APP"."addr_fmt_t"'

class AddrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    addr_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    loc = models.CharField(max_length=280, blank=True)
    blk_bldg = models.CharField(max_length=40, blank=True)
    unit = models.CharField(max_length=24, blank=True)
    st_name = models.CharField(max_length=280)
    cty_name = models.CharField(max_length=280)
    pstl_cd = models.CharField(max_length=48, blank=True)
    addr_stat_enu = models.BigIntegerField()
    pstlcd_id = models.BigIntegerField(null=True, blank=True)
    ctry_cd = models.CharField(max_length=16)
    sta_cd = models.CharField(max_length=16)
    ctry_stat_enu = models.BigIntegerField()
    sta_stat_enu = models.BigIntegerField()
    city_stat_enu = models.BigIntegerField()
    st_stat_enu = models.BigIntegerField()
    blk_stat_enu = models.BigIntegerField()
    unit_stat_enu = models.BigIntegerField()
    pstlcd_stat_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    uptd_dtt = models.DateField(null=True, blank=True)
    uptdbvldtsrvrid = models.BigIntegerField(null=True, blank=True)
    addrentytyp_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=44)
    updt_usr_cd = models.CharField(max_length=44, blank=True)
    tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    glrgn_zn_cd = models.CharField(max_length=64, blank=True)
    loc_name = models.CharField(max_length=280, blank=True)
    geocd_ovrd_yn = models.CharField(max_length=1)
    latitude = models.DecimalField(max_digits=6, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    resident_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."addr_t"'

class AlrtTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    alrt_typ_cd = models.CharField(max_length=80)
    opt_lck = models.BigIntegerField()
    alrt_typ_desc = models.CharField(max_length=280)
    alrt_cat_enu = models.BigIntegerField()
    sys_prvd_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    alrt_ebl_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mntr_situatn_cd = models.CharField(max_length=80, blank=True)
    sec_cd = models.CharField(max_length=64, blank=True)
    gen_evnt_notf_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."alrt_typ_t"'

class ApplT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    appl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    appl_cd = models.CharField(max_length=60)
    appl_enu = models.BigIntegerField()
    div_cd = models.CharField(max_length=16, blank=True)
    appl_desc = models.CharField(max_length=280, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."appl_t"'

class AptStaTnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField()
    sta_tnst_dtt = models.DateField()
    rptd_dtt = models.DateField()
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    sec_cd = models.CharField(max_length=64)
    prevstatus_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    apt_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."apt_sta_tnst_t"'

class ApTrnsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    trns_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sm_apvdfidtl_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    smapvddtltax_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    tot_frhtchrg_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    tot_tax_amt_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    invc_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    pymt_due_dt = models.DateField()
    crtd_dtt = models.DateField()
    cur_stat_id = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    carr_name = models.CharField(max_length=280)
    pyto_carr_name = models.CharField(max_length=280)
    frht_bill_num = models.CharField(max_length=120)
    frhtbill_src_enu = models.BigIntegerField()
    rcvd_dt = models.DateField()
    trns_ver_cd = models.CharField(max_length=40)
    frht_bill_id = models.BigIntegerField()
    carr_cd = models.CharField(max_length=64)
    pyto_carr_cd = models.CharField(max_length=64)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    run_id = models.BigIntegerField(null=True, blank=True)
    carr_vend_num = models.CharField(max_length=136, blank=True)
    carr_acc_num = models.CharField(max_length=136, blank=True)
    pyto_vend_num = models.CharField(max_length=136, blank=True)
    pyto_acc_num = models.CharField(max_length=136, blank=True)
    frht_bill_typ_typ = models.BigIntegerField(null=True, blank=True)
    pymt_trms_typ = models.BigIntegerField(null=True, blank=True)
    ori_frhtbill_num = models.CharField(max_length=120, blank=True)
    ori_frht_bill_id = models.BigIntegerField(null=True, blank=True)
    fb_btch_ctl_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ap_trns_t"'

class ApTrnsVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    trns_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    trns_ver_desc = models.CharField(max_length=280)
    fis_btch_aprd_yn = models.CharField(max_length=1)
    cut_off_adj_day = models.BigIntegerField()
    prt_rgst_yn = models.CharField(max_length=1)
    prt_frht_invc_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=4000, blank=True)
    strt_adj_day = models.BigIntegerField()
    excl_carr_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."ap_trns_ver_t"'

class ArchRfrcNumT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    arch_rfrc_num_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    shpm_id = models.BigIntegerField()
    carr_cd = models.CharField(max_length=64)
    rfrc_num = models.CharField(max_length=120)
    rfrc_num_typ = models.BigIntegerField()
    rfrc_num_qlfr_id = models.BigIntegerField()
    archrfrcnumrsn_enu = models.BigIntegerField()
    arch_dtt = models.DateField()
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    arch_usr_cd = models.CharField(max_length=40)
    class Meta:
        db_table = u'"I2TM_APP"."arch_rfrc_num_t"'

class ArTrnsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    trns_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sm_apvdfidtl_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    smapvddtltax_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    tot_frhtchrg_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    tot_tax_amt_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    invc_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    pymt_due_dt = models.DateField()
    crtd_dtt = models.DateField()
    cur_stat_id = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    invc_src_enu = models.BigIntegerField()
    invc_num = models.CharField(max_length=120)
    trns_ver_cd = models.CharField(max_length=40)
    cust_cd = models.CharField(max_length=64)
    bill_to_cust_cd = models.CharField(max_length=64)
    frht_invc_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    run_id = models.BigIntegerField(null=True, blank=True)
    cust_name = models.CharField(max_length=280, blank=True)
    cust_acc_num = models.CharField(max_length=136, blank=True)
    acc_num_withcust = models.CharField(max_length=136, blank=True)
    billto_cust_name = models.CharField(max_length=280, blank=True)
    billto_acc_num = models.CharField(max_length=136, blank=True)
    accnumwithbillto = models.CharField(max_length=136, blank=True)
    invc_typ = models.BigIntegerField(null=True, blank=True)
    pymt_trms_typ = models.BigIntegerField(null=True, blank=True)
    ori_invc_num = models.CharField(max_length=120, blank=True)
    ori_frht_invc_id = models.BigIntegerField(null=True, blank=True)
    rcvd_dt = models.DateField()
    class Meta:
        db_table = u'"I2TM_APP"."ar_trns_t"'

class ArTrnsVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    trns_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    trns_ver_desc = models.CharField(max_length=280)
    fis_btch_aprd_yn = models.CharField(max_length=1)
    cut_off_adj_day = models.BigIntegerField()
    prt_rgst_yn = models.CharField(max_length=1)
    prt_frht_invc_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    cust_cd = models.CharField(max_length=4000, blank=True)
    strt_adj_day = models.BigIntegerField()
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."ar_trns_ver_t"'

class AssEvntSecT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_id = models.BigIntegerField()
    sec_cd = models.CharField(max_length=64)
    ebl_yn = models.CharField(max_length=1)
    usr_gen_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."ass_evnt_sec_t"'

class AssExclCdtyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cdty_cd_field = models.CharField(max_length=48)
    cdty_cd = models.CharField(max_length=48)
    class Meta:
        db_table = u'"I2TM_APP"."ass_excl_cdty_t"'

class AssSecStatT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_cd = models.CharField(max_length=64)
    stat_id = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."ass_sec_stat_t"'

class AssUsrdfnZnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    zn_cd = models.CharField(max_length=64)
    zn_grp_cd = models.CharField(max_length=48)
    class Meta:
        db_table = u'"I2TM_APP"."ass_usrdfn_zn_t"'

class AudtChrgDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_chrg_detl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    audt_ctl_id = models.BigIntegerField(null=True, blank=True)
    chrg_adj_lvl_cd = models.CharField(max_length=48, blank=True)
    chrg_adj_lvl_desc = models.CharField(max_length=280, blank=True)
    chrg_rsn_cd = models.CharField(max_length=48, blank=True)
    chrg_rsn_desc = models.CharField(max_length=280, blank=True)
    audt_cnfg_cd = models.CharField(max_length=64, blank=True)
    chrg_gross_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_pymnt_net_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_ratg_net_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    chrg_detl_id = models.BigIntegerField(null=True, blank=True)
    chrg_lvl_cd = models.CharField(max_length=48, blank=True)
    chrg_lvl_desc = models.CharField(max_length=280, blank=True)
    chrg_typ_cd = models.CharField(max_length=48, blank=True)
    chrg_typ_desc = models.CharField(max_length=280, blank=True)
    chrg_audt_id = models.BigIntegerField(null=True, blank=True)
    audt_usr_cd = models.CharField(max_length=40, blank=True)
    chrg_frht_cls_cd = models.CharField(max_length=16, blank=True)
    chrg_ratd_as_frht_cls_cd = models.CharField(max_length=16, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    audt_ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_optm_plan_id = models.BigIntegerField(null=True, blank=True)
    ld_src_cd = models.CharField(max_length=48, blank=True)
    ld_src_desc = models.CharField(max_length=280, blank=True)
    chrg_opt_apld_cd = models.CharField(max_length=48, blank=True)
    chrg_opt_apld_desc = models.CharField(max_length=280, blank=True)
    chrg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    chrg_rate_as_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chrg_rate_as_uom_cd = models.CharField(max_length=48, blank=True)
    chrg_rate_as_uom_desc = models.CharField(max_length=280, blank=True)
    chrg_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chrg_uom_cd = models.CharField(max_length=48, blank=True)
    chrg_uom_desc = models.CharField(max_length=280, blank=True)
    chrg_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_lkup_unit_cd = models.CharField(max_length=48, blank=True)
    chrg_lkup_unit_desc = models.CharField(max_length=280, blank=True)
    chrg_lkup_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chrg_ratd_at_rng = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chrg_prty = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    chrg_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    chrg_shpg_loc_typ_cd = models.CharField(max_length=48, blank=True)
    chrg_shpg_loc_typ_desc = models.CharField(max_length=280, blank=True)
    chrg_cur_stat_cd = models.CharField(max_length=48, blank=True)
    chrg_cur_stat_desc = models.CharField(max_length=80, blank=True)
    chrg_seq_num = models.BigIntegerField(null=True, blank=True)
    audt_sys_dtt = models.DateField(null=True, blank=True)
    audt_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    audt_sec_cd = models.CharField(max_length=64, blank=True)
    chrg_unit_typ_cd = models.CharField(max_length=48, blank=True)
    chrg_unit_typ_desc = models.CharField(max_length=280, blank=True)
    ld_ratg_cncy_cd = models.CharField(max_length=48, blank=True)
    ld_ratg_cncy_desc = models.CharField(max_length=280, blank=True)
    ld_pymnt_cncy_typ_cd = models.CharField(max_length=48, blank=True)
    ld_pymnt_cncy_typ_desc = models.CharField(max_length=280, blank=True)
    stat_rptd_dtt = models.DateField(null=True, blank=True)
    chrg_stop_id = models.BigIntegerField(null=True, blank=True)
    trip_lvl_chrg_yn = models.CharField(max_length=1, blank=True)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    ratd_as_eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    pre_pchd_yn = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."audt_chrg_detl_t"'

class AudtCnfgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_cnfg_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    audt_cnfg_desc = models.CharField(max_length=280, blank=True)
    sort_seq = models.BigIntegerField(null=True, blank=True)
    ld_enbl_yn = models.CharField(max_length=1)
    ld_actv_yn = models.CharField(max_length=1)
    shpm_enbl_yn = models.CharField(max_length=1)
    shpm_actv_yn = models.CharField(max_length=1)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    chrg_actv_yn = models.CharField(max_length=1)
    stop_actv_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."audt_cnfg_t"'

class AudtCtlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_ctl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    audt_cnfg_cd = models.CharField(max_length=64, blank=True)
    audt_rptd_dtt = models.DateField(null=True, blank=True)
    audt_usr_cd = models.CharField(max_length=40, blank=True)
    audt_sec_cd = models.CharField(max_length=64, blank=True)
    audt_sec_desc = models.CharField(max_length=280, blank=True)
    audt_sys_dtt = models.DateField(null=True, blank=True)
    audt_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."audt_ctl_t"'

class AudtLdLegDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_ld_leg_detl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    audt_ctl_id = models.BigIntegerField(null=True, blank=True)
    detl_drop_apt_rqrd_yn = models.CharField(max_length=1, blank=True)
    detl_pick_apt_rqrd_yn = models.CharField(max_length=1, blank=True)
    audt_cnfg_cd = models.CharField(max_length=64, blank=True)
    shpm_mxd_ld_yn = models.CharField(max_length=1, blank=True)
    shpm_billto_cust_cd = models.CharField(max_length=64, blank=True)
    shpm_billto_cust_name = models.CharField(max_length=280, blank=True)
    shpm_buyer_seller_cd = models.CharField(max_length=48, blank=True)
    shpm_buyer_seller_desc = models.CharField(max_length=280, blank=True)
    shpm_cdty_cd = models.CharField(max_length=48, blank=True)
    stat_cur_loc_cty_name = models.CharField(max_length=280, blank=True)
    stat_cur_loc_ctry_cd = models.CharField(max_length=12, blank=True)
    stat_cur_loc_sta_cd = models.CharField(max_length=16, blank=True)
    shpm_cust_cd = models.CharField(max_length=64, blank=True)
    shpm_cust_name = models.CharField(max_length=280, blank=True)
    detl_cfmd_dtt = models.DateField(null=True, blank=True)
    detl_drop_arvl_dtt = models.DateField(null=True, blank=True)
    detl_drop_dptr_dtt = models.DateField(null=True, blank=True)
    detl_pkup_arvl_dtt = models.DateField(null=True, blank=True)
    detl_pkup_dptr_dtt = models.DateField(null=True, blank=True)
    detl_drop_date_src = models.BigIntegerField(null=True, blank=True)
    detl_pkup_date_src = models.BigIntegerField(null=True, blank=True)
    detl_to_loc = models.CharField(max_length=280, blank=True)
    detl_to_apt_emal = models.CharField(max_length=100, blank=True)
    detl_to_apt_fax_phn = models.CharField(max_length=23, blank=True)
    detl_to_apt_with_name = models.CharField(max_length=128, blank=True)
    detl_to_apt_tel1_phn = models.CharField(max_length=23, blank=True)
    detl_to_apt_tel2_phn = models.CharField(max_length=23, blank=True)
    detl_to_apt_url = models.CharField(max_length=256, blank=True)
    detl_to_apt_frm_dtt = models.DateField(null=True, blank=True)
    detl_to_apt_athy_num = models.CharField(max_length=120, blank=True)
    detl_to_apt_ovrd_hrs_op_yn = models.CharField(max_length=1, blank=True)
    detl_to_apt_pot_rrat_rqrd_yn = models.CharField(max_length=1, blank=True)
    detl_to_apt_cur_stat_cd = models.CharField(max_length=48, blank=True)
    detl_to_apt_cur_stat_desc = models.CharField(max_length=80, blank=True)
    detl_to_apt_to_dtt = models.DateField(null=True, blank=True)
    detl_to_addr_id = models.BigIntegerField(null=True, blank=True)
    detl_to_blk_bldg = models.CharField(max_length=40, blank=True)
    detl_to_cty_name = models.CharField(max_length=280, blank=True)
    detl_to_ctry_cd = models.CharField(max_length=12, blank=True)
    detl_to_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    detl_to_shpg_loc_name = models.CharField(max_length=280, blank=True)
    detl_to_ship_loc_typ_cd = models.CharField(max_length=48, blank=True)
    detl_to_ship_loc_typ_desc = models.CharField(max_length=280, blank=True)
    detl_to_sta_cd = models.CharField(max_length=16, blank=True)
    detl_to_st_name = models.CharField(max_length=280, blank=True)
    detl_to_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    detl_to_unit = models.CharField(max_length=24, blank=True)
    detl_to_pstl_cd = models.CharField(max_length=48, blank=True)
    detl_rptd_yn = models.CharField(max_length=1, blank=True)
    detl_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    shpm_div_cd = models.CharField(max_length=16, blank=True)
    detl_drop_stop_id = models.BigIntegerField(null=True, blank=True)
    stat_rptd_dtt = models.DateField(null=True, blank=True)
    audt_usr_cd = models.CharField(max_length=40, blank=True)
    shpm_frht_trms_cd = models.CharField(max_length=48, blank=True)
    shpm_frht_trms_desc = models.CharField(max_length=280, blank=True)
    shpm_inco_terms_cd = models.CharField(max_length=12, blank=True)
    shpm_inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpm_inco_shpg_loc_name = models.CharField(max_length=280, blank=True)
    shpm_inco_shpg_loc_typ_cd = models.CharField(max_length=48, blank=True)
    shpm_inco_shpg_loc_typ_desc = models.CharField(max_length=280, blank=True)
    shpm_inco_ver_cd = models.CharField(max_length=48, blank=True)
    shpm_inco_ver_desc = models.CharField(max_length=280, blank=True)
    ld_dlvy_seq = models.BigIntegerField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_pick_seq = models.BigIntegerField(null=True, blank=True)
    ld_src_cd = models.CharField(max_length=48, blank=True)
    ld_src_desc = models.CharField(max_length=280, blank=True)
    ld_lgst_grp_cd = models.CharField(max_length=16, blank=True)
    shpm_lgst_grp_cd = models.CharField(max_length=16, blank=True)
    shpm_mrge_csld_cls_id = models.CharField(max_length=120, blank=True)
    shpm_mrge_csld_seq_num = models.BigIntegerField(null=True, blank=True)
    detl_non_live_drpf_yn = models.CharField(max_length=1, blank=True)
    detl_non_live_pkup_yn = models.CharField(max_length=1, blank=True)
    shpm_held_yn = models.CharField(max_length=1, blank=True)
    ld_optm_plan_id = models.BigIntegerField(null=True, blank=True)
    shpm_ordr_grp_cd = models.CharField(max_length=16, blank=True)
    shpm_cdty_pick_seq_num = models.BigIntegerField(null=True, blank=True)
    detl_frm_loc = models.CharField(max_length=280, blank=True)
    detl_frm_apt_emal = models.CharField(max_length=100, blank=True)
    detl_frm_apt_fax_phn = models.CharField(max_length=23, blank=True)
    detl_frm_apt_with_name = models.CharField(max_length=128, blank=True)
    detl_frm_apt_tel1_phn = models.CharField(max_length=23, blank=True)
    detl_frm_apt_tel2_phn = models.CharField(max_length=23, blank=True)
    detl_frm_apt_url = models.CharField(max_length=256, blank=True)
    detl_frm_apt_frm_dtt = models.DateField(null=True, blank=True)
    detl_frm_apt_athy_num = models.CharField(max_length=120, blank=True)
    detl_frm_apt_ovrd_hrs_op_yn = models.CharField(max_length=1, blank=True)
    detl_frm_apt_pot_rrat_rqrd_yn = models.CharField(max_length=1, blank=True)
    detl_frm_apt_cur_stat_cd = models.CharField(max_length=48, blank=True)
    detl_frm_apt_cur_stat_desc = models.CharField(max_length=80, blank=True)
    detl_frm_apt_to_dtt = models.DateField(null=True, blank=True)
    detl_frm_addr_id = models.BigIntegerField(null=True, blank=True)
    detl_frm_blk_bldg = models.CharField(max_length=40, blank=True)
    detl_frm_cty_name = models.CharField(max_length=280, blank=True)
    detl_frm_ctry_cd = models.CharField(max_length=12, blank=True)
    detl_frm_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    detl_frm_shpg_loc_name = models.CharField(max_length=280, blank=True)
    detl_frm_ship_loc_typ_cd = models.CharField(max_length=48, blank=True)
    detl_frm_ship_loc_typ_desc = models.CharField(max_length=280, blank=True)
    detl_frm_sta_cd = models.CharField(max_length=16, blank=True)
    detl_frm_st_name = models.CharField(max_length=280, blank=True)
    detl_frm_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    detl_frm_unit = models.CharField(max_length=24, blank=True)
    detl_frm_pstl_cd = models.CharField(max_length=48, blank=True)
    detl_pod_dtt = models.DateField(null=True, blank=True)
    detl_pod_desc = models.CharField(max_length=280, blank=True)
    detl_pod_extl_cd = models.CharField(max_length=48, blank=True)
    detl_pod_pce_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    detl_pod_detl_yn = models.CharField(max_length=1, blank=True)
    detl_pod_usr_cd = models.CharField(max_length=40, blank=True)
    detl_pod_sig = models.CharField(max_length=128, blank=True)
    detl_pod_skid_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    detl_pod_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_prf_ctr_cd = models.CharField(max_length=48, blank=True)
    shpm_prf_ctr_desc = models.CharField(max_length=280, blank=True)
    detl_pick_stop_id = models.BigIntegerField(null=True, blank=True)
    detl_rfrc_num1 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num2 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num3 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num4 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num5 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num6 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num7 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num8 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num9 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num10 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num11 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num12 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num13 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num14 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num15 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num16 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num17 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num18 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num19 = models.CharField(max_length=120, blank=True)
    detl_rfrc_num20 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num1 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num2 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num3 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num4 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num5 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num6 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num7 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num8 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num9 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num10 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num11 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num12 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num13 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num14 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num15 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num16 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num17 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num18 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num19 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num20 = models.CharField(max_length=120, blank=True)
    shpm_rvnu_trpt_odr_yn = models.CharField(max_length=1, blank=True)
    detl_schd_actv_yn = models.CharField(max_length=1, blank=True)
    audt_sec_cd = models.CharField(max_length=64, blank=True)
    shpm_drct_frht_yn = models.CharField(max_length=1, blank=True)
    shpm_cncy_cd = models.CharField(max_length=48, blank=True)
    shpm_cncy_desc = models.CharField(max_length=280, blank=True)
    shpm_bs_dcld_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_dcld_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_umsrdist_cd = models.CharField(max_length=48, blank=True)
    shpm_umsrdist_desc = models.CharField(max_length=280, blank=True)
    shpm_echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    shpm_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    shpm_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    shpm_umsrvol_cd = models.CharField(max_length=48, blank=True)
    shpm_umsrvol_desc = models.CharField(max_length=280, blank=True)
    shpm_bs_odr_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_odr_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_tot_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpm_tot_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpm_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_umsrwgt_cd = models.CharField(max_length=48, blank=True)
    shpm_umsrwgt_desc = models.CharField(max_length=280, blank=True)
    shpm_csld_cls = models.CharField(max_length=120, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    detl_bs_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    detl_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    detl_bs_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_tot_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    detl_tot_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    detl_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_fnclstat_cd = models.CharField(max_length=48, blank=True)
    detl_fnclstat_desc = models.CharField(max_length=80, blank=True)
    detl_ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    detl_optlstat_cd = models.CharField(max_length=48, blank=True)
    detl_optlstat_desc = models.CharField(max_length=80, blank=True)
    detl_seq_num = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    shpm_desc = models.CharField(max_length=280, blank=True)
    shpm_typ_cd = models.CharField(max_length=8, blank=True)
    shpm_ver_cd = models.CharField(max_length=40, blank=True)
    stop_drop_seq_num = models.BigIntegerField(null=True, blank=True)
    stop_pick_seq_num = models.BigIntegerField(null=True, blank=True)
    audt_sys_dtt = models.DateField(null=True, blank=True)
    audt_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    ld_trip_id = models.BigIntegerField(null=True, blank=True)
    ld_trip_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpm_urgt_yn = models.CharField(max_length=1, blank=True)
    audt_ld_leg_id = models.BigIntegerField(null=True, blank=True)
    audt_opmr_que_id = models.BigIntegerField(null=True, blank=True)
    detl_shft_seq = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_vbty_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."audt_ld_leg_detl_t"'

class AudtLdLegT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_ld_leg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    audt_ctl_id = models.BigIntegerField(null=True, blank=True)
    ld_actl_carrsrvc = models.CharField(max_length=120, blank=True)
    ld_ratg_tot_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ld_ratg_dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ld_ratg_net_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    audt_cnfg_cd = models.CharField(max_length=64, blank=True)
    ld_bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    ld_carr_cd = models.CharField(max_length=64, blank=True)
    ld_cdty_cd = models.CharField(max_length=48, blank=True)
    ld_cost_ctr_cd = models.CharField(max_length=48, blank=True)
    ld_cost_ctr_desc = models.CharField(max_length=280, blank=True)
    ld_ratg_cncy_cd = models.CharField(max_length=48, blank=True)
    ld_ratg_cncy_desc = models.CharField(max_length=280, blank=True)
    stat_cur_loc_cty_name = models.CharField(max_length=128, blank=True)
    stat_cur_loc_ctry_cd = models.CharField(max_length=12, blank=True)
    stat_cur_loc_sta_cd = models.CharField(max_length=16, blank=True)
    ld_cust_cd = models.CharField(max_length=64, blank=True)
    ld_cust_name = models.CharField(max_length=280, blank=True)
    ld_cpld_dtt = models.DateField(null=True, blank=True)
    ld_end_dtt = models.DateField(null=True, blank=True)
    ld_scdd_dtt = models.DateField(null=True, blank=True)
    ld_shpd_dtt = models.DateField(null=True, blank=True)
    ld_strd_dtt = models.DateField(null=True, blank=True)
    ld_tdr_rsps_by_dtt = models.DateField(null=True, blank=True)
    ld_bs_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ld_last_addr_id = models.BigIntegerField(null=True, blank=True)
    ld_last_cty_name = models.CharField(max_length=280, blank=True)
    ld_last_ctry_cd = models.CharField(max_length=12, blank=True)
    ld_last_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ld_last_shpg_loc_name = models.CharField(max_length=280, blank=True)
    ld_last_shpg_loc_typ_cd = models.CharField(max_length=48, blank=True)
    ld_last_shpg_loc_typ_desc = models.CharField(max_length=280, blank=True)
    ld_last_sta_cd = models.CharField(max_length=16, blank=True)
    ld_last_pstl_cd = models.CharField(max_length=48, blank=True)
    ld_last_loc = models.CharField(max_length=280, blank=True)
    ld_last_st_name = models.CharField(max_length=280, blank=True)
    ld_last_blk_bldg = models.CharField(max_length=40, blank=True)
    ld_last_unit = models.CharField(max_length=24, blank=True)
    ld_last_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    ld_drct_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_fixd_itnr_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_in_tnst_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_init_reps_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_ldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_outofrout_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_ret_to_orig_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_mile_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_tot_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_div_cd = models.CharField(max_length=16, blank=True)
    ld_drvr = models.CharField(max_length=32, blank=True)
    ld_drvr_lic_num = models.CharField(max_length=120, blank=True)
    ld_eqmt_typ = models.CharField(max_length=20, blank=True)
    stat_rptd_dtt = models.DateField(null=True, blank=True)
    audt_usr_cd = models.CharField(max_length=40, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    ld_ratg_echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    ld_fnclstat_cd = models.CharField(max_length=48, blank=True)
    ld_fnclstat_desc = models.CharField(max_length=80, blank=True)
    ld_term_cd = models.CharField(max_length=48, blank=True)
    ld_term_desc = models.CharField(max_length=280, blank=True)
    ld_tot_driving_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_elpd_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_tot_loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_tot_off_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_tot_on_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_tot_wait_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_tot_unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    ld_leg_cat_cd = models.CharField(max_length=48, blank=True)
    ld_leg_cat_desc = models.CharField(max_length=280, blank=True)
    ld_cmps_aprd_yn = models.CharField(max_length=1, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_optm_plan_id = models.BigIntegerField(null=True, blank=True)
    ld_src_cd = models.CharField(max_length=48, blank=True)
    ld_src_desc = models.CharField(max_length=280, blank=True)
    ld_desc = models.CharField(max_length=280, blank=True)
    ld_lgst_grp_cd = models.CharField(max_length=16, blank=True)
    ld_non_live_pkup_yn = models.CharField(max_length=1, blank=True)
    ld_non_live_drpf_yn = models.CharField(max_length=1, blank=True)
    ld_num_lldheld = models.BigIntegerField(null=True, blank=True)
    ld_num_shpm = models.BigIntegerField(null=True, blank=True)
    ld_num_stop = models.BigIntegerField(null=True, blank=True)
    ld_num_urgt_lld = models.BigIntegerField(null=True, blank=True)
    ld_optlstat_cd = models.CharField(max_length=48, blank=True)
    ld_optlstat_desc = models.CharField(max_length=80, blank=True)
    ld_bs_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ld_frst_addr_id = models.BigIntegerField(null=True, blank=True)
    ld_frst_cty_name = models.CharField(max_length=280, blank=True)
    ld_frst_ctry_cd = models.CharField(max_length=12, blank=True)
    ld_frst_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ld_frst_shpg_loc_name = models.CharField(max_length=280, blank=True)
    ld_frst_shpg_loc_typ_cd = models.CharField(max_length=48, blank=True)
    ld_frst_shpg_loc_typ_desc = models.CharField(max_length=280, blank=True)
    ld_frst_sta_cd = models.CharField(max_length=16, blank=True)
    ld_frst_pstl_cd = models.CharField(max_length=48, blank=True)
    ld_frst_loc = models.CharField(max_length=280, blank=True)
    ld_frst_st_name = models.CharField(max_length=280, blank=True)
    ld_frst_blk_bldg = models.CharField(max_length=40, blank=True)
    ld_frst_unit = models.CharField(max_length=24, blank=True)
    ld_frst_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    ld_pce_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_skid_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_pre_bult_yn = models.CharField(max_length=1, blank=True)
    ld_ratg_rate_cd = models.CharField(max_length=132, blank=True)
    ld_ratg_rshp_rsn_cd = models.CharField(max_length=48, blank=True)
    ld_ratg_rshp_rsn_desc = models.CharField(max_length=280, blank=True)
    rfrc_num1 = models.CharField(max_length=120, blank=True)
    rfrc_num2 = models.CharField(max_length=120, blank=True)
    rfrc_num3 = models.CharField(max_length=120, blank=True)
    rfrc_num4 = models.CharField(max_length=120, blank=True)
    rfrc_num5 = models.CharField(max_length=120, blank=True)
    rfrc_num6 = models.CharField(max_length=120, blank=True)
    rfrc_num7 = models.CharField(max_length=120, blank=True)
    rfrc_num8 = models.CharField(max_length=120, blank=True)
    rfrc_num9 = models.CharField(max_length=120, blank=True)
    rfrc_num10 = models.CharField(max_length=120, blank=True)
    rfrc_num11 = models.CharField(max_length=120, blank=True)
    rfrc_num12 = models.CharField(max_length=120, blank=True)
    rfrc_num13 = models.CharField(max_length=120, blank=True)
    rfrc_num14 = models.CharField(max_length=120, blank=True)
    rfrc_num15 = models.CharField(max_length=120, blank=True)
    rfrc_num16 = models.CharField(max_length=120, blank=True)
    rfrc_num17 = models.CharField(max_length=120, blank=True)
    rfrc_num18 = models.CharField(max_length=120, blank=True)
    rfrc_num19 = models.CharField(max_length=120, blank=True)
    rfrc_num20 = models.CharField(max_length=120, blank=True)
    ld_schd_cmpd_yn = models.CharField(max_length=1, blank=True)
    ld_seal_num = models.CharField(max_length=64, blank=True)
    audt_sec_cd = models.CharField(max_length=64, blank=True)
    ld_srvc_cd = models.CharField(max_length=16, blank=True)
    ld_ratg_spot_rate_yn = models.CharField(max_length=1, blank=True)
    ld_sus_func_cd = models.CharField(max_length=48, blank=True)
    ld_sus_func_desc = models.CharField(max_length=280, blank=True)
    audt_sys_dtt = models.DateField(null=True, blank=True)
    audt_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    ld_ratg_tff_id = models.BigIntegerField(null=True, blank=True)
    ld_ratg_team_drvr_yn = models.CharField(max_length=1, blank=True)
    ld_tdr_acpd_by_name = models.CharField(max_length=128, blank=True)
    ld_trctr_onr = models.CharField(max_length=64, blank=True)
    ld_trctr_lic_num = models.CharField(max_length=120, blank=True)
    ld_trlr_num = models.CharField(max_length=96, blank=True)
    ld_trlr_onr = models.CharField(max_length=64, blank=True)
    ld_trlr_lic_num = models.CharField(max_length=120, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    trip_seq_num = models.BigIntegerField(null=True, blank=True)
    ld_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ld_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ld_ratg_umsrwgt_cd = models.CharField(max_length=48, blank=True)
    ld_ratg_umsrwgt_desc = models.CharField(max_length=280, blank=True)
    ld_ratg_umsrvol_cd = models.CharField(max_length=48, blank=True)
    ld_ratg_umsrvol_desc = models.CharField(max_length=280, blank=True)
    ld_ratg_umsrdist_cd = models.CharField(max_length=48, blank=True)
    ld_ratg_umsrdist_desc = models.CharField(max_length=280, blank=True)
    stat_etmd1_dtt = models.DateField(null=True, blank=True)
    stat_etmd2_dtt = models.DateField(null=True, blank=True)
    prfd_grsmrgn_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    etmd_grsmrgn_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    plng_stat_cd = models.CharField(max_length=48, blank=True)
    plng_stat_desc = models.CharField(max_length=280, blank=True)
    plng_stat_ovrd_cd = models.CharField(max_length=48, blank=True)
    plng_stat_ovrd_desc = models.CharField(max_length=280, blank=True)
    audt_opmr_que_id = models.BigIntegerField(null=True, blank=True)
    carr_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    carr_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    srvc_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    srvc_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    eqmt_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    eqmt_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    cstr_ovrd_yn = models.CharField(max_length=1, blank=True)
    cdty_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    cdty_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    ld_num_pmy_stop = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_vbty_id = models.BigIntegerField(null=True, blank=True)
    ld_ratg_extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dmcl_cd_trctr = models.CharField(max_length=64, blank=True)
    dmcl_cd_trctr_name = models.CharField(max_length=280, blank=True)
    dmcl_cd_trlr = models.CharField(max_length=64, blank=True)
    dmcl_cd_trlr_name = models.CharField(max_length=280, blank=True)
    dmcl_trctr_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    dmcl_trctr_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    dmcl_trlr_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    dmcl_trlr_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    eqmt_trctr_cmtd_stat_cd = models.CharField(max_length=48, blank=True)
    eqmt_trctr_cmtd_stat_desc = models.CharField(max_length=280, blank=True)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    far_pnt_stop_id = models.BigIntegerField(null=True, blank=True)
    lane_assc_id = models.BigIntegerField(null=True, blank=True)
    trctr_num = models.CharField(max_length=96, blank=True)
    in_tnst_unldd_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    trctr_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    lld_carrcmtd_tms = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    lld_srvccmtd_tms = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    eqmt_typ_rqrd_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    eqmt_typ_trctr_rqrd_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tdr_req_id = models.BigIntegerField(null=True, blank=True)
    wgt_dist_extd = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    trip_tff_sav_bas_cd = models.CharField(max_length=48, blank=True)
    trip_tff_sav_bas_desc = models.CharField(max_length=280, blank=True)
    trip_cost_cncy_cd = models.CharField(max_length=48, blank=True)
    trip_cost_cncy_desc = models.CharField(max_length=280, blank=True)
    trip_cost_echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    trip_cost_chrg_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    trip_cost_srvc_cd = models.CharField(max_length=16, blank=True)
    trip_cost_eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    trip_cost_tff_id = models.BigIntegerField(null=True, blank=True)
    trip_cost_ratd_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."audt_ld_leg_t"'

class AudtShpmT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_shpm_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    audt_ctl_id = models.BigIntegerField(null=True, blank=True)
    shpm_ar_srvc_cd = models.CharField(max_length=16, blank=True)
    shpm_mxd_ld_yn = models.CharField(max_length=1, blank=True)
    shpm_spto_apt_rqrd_yn = models.CharField(max_length=1, blank=True)
    shpm_spfm_apt_rqrd_yn = models.CharField(max_length=1, blank=True)
    audt_cnfg_cd = models.CharField(max_length=64, blank=True)
    shpm_billto_cust_cd = models.CharField(max_length=64, blank=True)
    shpm_billto_cust_ver_id = models.BigIntegerField(null=True, blank=True)
    shpm_billto_cust_name = models.CharField(max_length=280, blank=True)
    shpm_buyer_seller_cd = models.CharField(max_length=48, blank=True)
    shpm_buyer_seller_desc = models.CharField(max_length=280, blank=True)
    shpm_chrg_bsd_carr_yn = models.CharField(max_length=1, blank=True)
    shpm_cdty_cd = models.CharField(max_length=48, blank=True)
    shpm_cnse_grp_cd = models.CharField(max_length=48, blank=True)
    shpm_cnse_grp_desc = models.CharField(max_length=280, blank=True)
    shpm_cust_cd = models.CharField(max_length=64, blank=True)
    shpm_cust_ver_id = models.BigIntegerField(null=True, blank=True)
    shpm_cust_name = models.CharField(max_length=280, blank=True)
    shpm_cust_srvc_rep_cd = models.CharField(max_length=48, blank=True)
    shpm_cust_srvc_rep_desc = models.CharField(max_length=280, blank=True)
    shpm_frm_dlvy_dtt = models.DateField(null=True, blank=True)
    shpm_to_dlvy_dtt = models.DateField(null=True, blank=True)
    shpm_frm_pkup_dtt = models.DateField(null=True, blank=True)
    shpm_to_pkup_dtt = models.DateField(null=True, blank=True)
    shpm_to_loc = models.CharField(max_length=280, blank=True)
    shpm_to_addr_id = models.BigIntegerField(null=True, blank=True)
    shpm_to_blk_bldg = models.CharField(max_length=40, blank=True)
    shpm_to_cty_name = models.CharField(max_length=280, blank=True)
    shpm_to_ctry_cd = models.CharField(max_length=12, blank=True)
    shpm_to_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpm_to_shpg_loc_name = models.CharField(max_length=280, blank=True)
    shpm_to_ship_loc_typ_cd = models.CharField(max_length=48, blank=True)
    shpm_to_ship_loc_typ_desc = models.CharField(max_length=280, blank=True)
    shpm_to_sta_cd = models.CharField(max_length=16, blank=True)
    shpm_to_st_name = models.CharField(max_length=280, blank=True)
    shpm_to_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    shpm_to_unit = models.CharField(max_length=24, blank=True)
    shpm_to_pstl_cd = models.CharField(max_length=48, blank=True)
    shpm_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    shpm_div_cd = models.CharField(max_length=16, blank=True)
    stat_rptd_dtt = models.DateField(null=True, blank=True)
    audt_usr_cd = models.CharField(max_length=40, blank=True)
    shpm_frht_trms_cd = models.CharField(max_length=48, blank=True)
    shpm_frht_trms_desc = models.CharField(max_length=280, blank=True)
    shpm_inco_terms_cd = models.CharField(max_length=12, blank=True)
    shpm_inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpm_inco_shpg_loc_name = models.CharField(max_length=280, blank=True)
    shpm_inco_shpg_loc_typ_cd = models.CharField(max_length=48, blank=True)
    shpm_inco_shpg_loc_typ_desc = models.CharField(max_length=280, blank=True)
    shpm_inco_ver_cd = models.CharField(max_length=48, blank=True)
    shpm_inco_ver_desc = models.CharField(max_length=280, blank=True)
    shpm_prepaid_seg_only_yn = models.CharField(max_length=1, blank=True)
    shpm_jrny_tplt_cd = models.CharField(max_length=32, blank=True)
    shpm_lgst_grp_cd = models.CharField(max_length=16, blank=True)
    shpm_mrge_csld_cls_id = models.CharField(max_length=120, blank=True)
    shpm_mrge_csld_seq_num = models.BigIntegerField(null=True, blank=True)
    shpm_hold_yn = models.CharField(max_length=1, blank=True)
    shpm_ordr_grp_cd = models.CharField(max_length=16, blank=True)
    shpm_cdty_pick_seq_num = models.BigIntegerField(null=True, blank=True)
    shpm_odr_src_cd = models.CharField(max_length=48, blank=True)
    shpm_odr_src_desc = models.CharField(max_length=280, blank=True)
    shpm_frm_loc = models.CharField(max_length=280, blank=True)
    shpm_frm_addr_id = models.BigIntegerField(null=True, blank=True)
    shpm_frm_blk_bldg = models.CharField(max_length=40, blank=True)
    shpm_frm_cty_name = models.CharField(max_length=280, blank=True)
    shpm_frm_ctry_cd = models.CharField(max_length=12, blank=True)
    shpm_frm_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpm_frm_shpg_loc_name = models.CharField(max_length=280, blank=True)
    shpm_frm_ship_loc_typ_cd = models.CharField(max_length=48, blank=True)
    shpm_frm_ship_loc_typ_desc = models.CharField(max_length=280, blank=True)
    shpm_frm_sta_cd = models.CharField(max_length=16, blank=True)
    shpm_frm_st_name = models.CharField(max_length=280, blank=True)
    shpm_frm_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    shpm_frm_unit = models.CharField(max_length=24, blank=True)
    shpm_frm_pstl_cd = models.CharField(max_length=48, blank=True)
    shpm_prf_ctr_cd = models.CharField(max_length=48, blank=True)
    shpm_prf_ctr_desc = models.CharField(max_length=280, blank=True)
    shpm_prj_cd = models.CharField(max_length=48, blank=True)
    shpm_rfrc_num1 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num2 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num3 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num4 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num5 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num6 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num7 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num8 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num9 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num10 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num11 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num12 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num13 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num14 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num15 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num16 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num17 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num18 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num19 = models.CharField(max_length=120, blank=True)
    shpm_rfrc_num20 = models.CharField(max_length=120, blank=True)
    shpm_rvnu_trpt_odr_yn = models.CharField(max_length=1, blank=True)
    shpm_sale_pers_cd = models.CharField(max_length=40, blank=True)
    audt_sec_cd = models.CharField(max_length=64, blank=True)
    shpm_drct_frht_yn = models.CharField(max_length=1, blank=True)
    shpm_cncy_cd = models.CharField(max_length=48, blank=True)
    shpm_cncy_desc = models.CharField(max_length=280, blank=True)
    shpm_bs_dcld_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_dcld_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_umsrdist_cd = models.CharField(max_length=48, blank=True)
    shpm_umsrdist_desc = models.CharField(max_length=280, blank=True)
    shpm_echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    shpm_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    shpm_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    shpm_umsrvol_cd = models.CharField(max_length=48, blank=True)
    shpm_umsrvol_desc = models.CharField(max_length=280, blank=True)
    shpm_bs_odr_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_odr_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_tot_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpm_tot_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpm_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_umsrwgt_cd = models.CharField(max_length=48, blank=True)
    shpm_umsrwgt_desc = models.CharField(max_length=280, blank=True)
    shpm_csld_cls = models.CharField(max_length=120, blank=True)
    shpm_fnclstat_cd = models.CharField(max_length=48, blank=True)
    shpm_fnclstat_desc = models.CharField(max_length=80, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    shpm_optlstat_cd = models.CharField(max_length=48, blank=True)
    shpm_optlstat_desc = models.CharField(max_length=80, blank=True)
    shpm_ratg_cncy_cd = models.CharField(max_length=48, blank=True)
    shpm_ratg_cncy_desc = models.CharField(max_length=280, blank=True)
    shpm_ratg_elpd_tm = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    shpm_ratg_echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    shpm_chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_sys_calc_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_ratg_rate_cd = models.CharField(max_length=132, blank=True)
    shpm_ratg_rshp_rsn_cd = models.CharField(max_length=48, blank=True)
    shpm_ratg_rshp_rsn_desc = models.CharField(max_length=280, blank=True)
    shpm_ratg_spot_rate_yn = models.CharField(max_length=1, blank=True)
    shpm_dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shpm_ratg_umsrdist_cd = models.CharField(max_length=48, blank=True)
    shpm_ratg_umsrdist_desc = models.CharField(max_length=280, blank=True)
    shpm_ratg_umsrvol_cd = models.CharField(max_length=48, blank=True)
    shpm_ratg_umsrvol_desc = models.CharField(max_length=280, blank=True)
    shpm_ratg_tff_id = models.BigIntegerField(null=True, blank=True)
    shpm_ratg_umsrwgt_cd = models.CharField(max_length=48, blank=True)
    shpm_ratg_umsrwgt_desc = models.CharField(max_length=280, blank=True)
    shpm_desc = models.CharField(max_length=280, blank=True)
    shpm_typ_cd = models.CharField(max_length=8, blank=True)
    shpm_ver_cd = models.CharField(max_length=40, blank=True)
    audt_sys_dtt = models.DateField(null=True, blank=True)
    audt_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    shpm_urgt_yn = models.CharField(max_length=1, blank=True)
    shpm_shft_seq = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_vbty_id = models.BigIntegerField(null=True, blank=True)
    shpm_ratg_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    shpm_ratg_extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."audt_shpm_t"'

class AudtStopT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    audt_stop_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    audt_ctl_id = models.BigIntegerField(null=True, blank=True)
    stop_apt_athy_num = models.CharField(max_length=120, blank=True)
    stop_apt_with_name = models.CharField(max_length=128, blank=True)
    stop_apt_frm_dtt = models.DateField(null=True, blank=True)
    stop_apt_to_dtt = models.DateField(null=True, blank=True)
    stop_apt_cur_stat_cd = models.CharField(max_length=48, blank=True)
    stop_apt_cur_stat_desc = models.CharField(max_length=80, blank=True)
    stop_apt_ovrd_hrs_op_yn = models.CharField(max_length=1, blank=True)
    stop_apt_tel1_phn = models.CharField(max_length=23, blank=True)
    stop_apt_tel2_phn = models.CharField(max_length=23, blank=True)
    stop_apt_fax_phn = models.CharField(max_length=23, blank=True)
    stop_apt_emal = models.CharField(max_length=100, blank=True)
    stop_apt_url = models.CharField(max_length=256, blank=True)
    stop_apt_rrat_rqrd_yn = models.CharField(max_length=1, blank=True)
    audt_cnfg_cd = models.CharField(max_length=64, blank=True)
    stop_cust_cd = models.CharField(max_length=64, blank=True)
    stop_cmpd_arvl_dtt = models.DateField(null=True, blank=True)
    stop_cmpd_dptr_dtt = models.DateField(null=True, blank=True)
    stop_eta_dtt = models.DateField(null=True, blank=True)
    stop_pick_arvl_rptd_dtt = models.DateField(null=True, blank=True)
    stop_pick_dptr_rptd_dtt = models.DateField(null=True, blank=True)
    stop_drop_arvl_rptd_dtt = models.DateField(null=True, blank=True)
    stop_drop_dptr_rptd_dtt = models.DateField(null=True, blank=True)
    stop_frmprevstop_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    stop_drop_bs_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    stop_drop_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    stop_drop_shpm_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_drop_bs_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    stop_drop_skid_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_drop_pce_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_drop_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    stop_drop_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    audt_usr_cd = models.CharField(max_length=40, blank=True)
    stop_loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    stop_tnstprevstop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    stop_unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    stop_waiting_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    audt_ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_optm_plan_id = models.BigIntegerField(null=True, blank=True)
    ld_src_cd = models.CharField(max_length=48, blank=True)
    ld_src_desc = models.CharField(max_length=280, blank=True)
    stop_pick_bs_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    stop_pick_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    stop_pick_shpm_num = models.BigIntegerField(null=True, blank=True)
    stop_pick_bs_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    stop_pick_skid_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_pick_pce_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_pick_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    stop_pick_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    stop_pick_cfmd_usr_cd = models.CharField(max_length=40, blank=True)
    stop_pick_cfmd_yn = models.CharField(max_length=1, blank=True)
    stop_pod_desc = models.CharField(max_length=280, blank=True)
    stop_pod_dtt = models.DateField(null=True, blank=True)
    stop_pod_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    stop_pod_pce_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_pod_skid_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_pod_sig = models.CharField(max_length=128, blank=True)
    stop_pod_usr_cd = models.CharField(max_length=40, blank=True)
    stop_pod_extl_cd = models.CharField(max_length=48, blank=True)
    stop_addr_id = models.BigIntegerField(null=True, blank=True)
    stop_cty_name = models.CharField(max_length=280, blank=True)
    stop_shpg_pnt_cd = models.CharField(max_length=48, blank=True)
    stop_shpg_pnt_desc = models.CharField(max_length=280, blank=True)
    stop_ctry_cd = models.CharField(max_length=12, blank=True)
    stop_loc_name = models.CharField(max_length=280, blank=True)
    stop_sta_cd = models.CharField(max_length=16, blank=True)
    stop_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    stop_pstl_cd = models.CharField(max_length=48, blank=True)
    stop_loc = models.CharField(max_length=280, blank=True)
    stop_st_name = models.CharField(max_length=280, blank=True)
    stop_blk_bldg = models.CharField(max_length=40, blank=True)
    stop_unit = models.CharField(max_length=24, blank=True)
    stop_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    stop_seq_num = models.BigIntegerField(null=True, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    audt_sys_dtt = models.DateField(null=True, blank=True)
    audt_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    audt_sec_cd = models.CharField(max_length=64, blank=True)
    stat_rptd_dtt = models.DateField(null=True, blank=True)
    apt_rqrd_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    stop_pmy_shpg_pnt_cd = models.CharField(max_length=64, blank=True)
    stop_pmy_shpg_pnt_desc = models.CharField(max_length=280, blank=True)
    wknd_hldy_prev_stop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    strd_wknd_hldy_dtt = models.DateField(null=True, blank=True)
    end_wknd_hldy_dtt = models.DateField(null=True, blank=True)
    wknd_hldy_ortn_cd = models.CharField(max_length=48, blank=True)
    wknd_hldy_ortn_desc = models.CharField(max_length=280, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."audt_stop_t"'

class AutoApldOptT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    auto_apld_opt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    aply_frm_ar_enu = models.BigIntegerField()
    aply_frm_ap_enu = models.BigIntegerField()
    aply_to_ar_enu = models.BigIntegerField()
    aply_to_ap_enu = models.BigIntegerField()
    aplytoibndar_enu = models.BigIntegerField()
    aplytoibndap_enu = models.BigIntegerField()
    aplytotsfrar_enu = models.BigIntegerField()
    aplytotsfrap_enu = models.BigIntegerField()
    aplytoobndar_enu = models.BigIntegerField()
    aplytoobndap_enu = models.BigIntegerField()
    cdty_cd = models.CharField(max_length=48, blank=True)
    cnse_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    comp_typ_id = models.BigIntegerField(null=True, blank=True)
    hub_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ldat_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    dc_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."auto_apld_opt_t"'

class AutoTdrInfoT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    auto_tdr_info_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    ld_leg_id = models.BigIntegerField()
    curr_carr_ptr = models.BigIntegerField()
    elgb_carrs = models.CharField(max_length=2480)
    err_msg = models.CharField(max_length=256, blank=True)
    scdd_dtt = models.DateField(null=True, blank=True)
    frst_stop_pkup_dtt = models.DateField(null=True, blank=True)
    auto_acpt_seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    rshp_defr_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."auto_tdr_info_t"'

class BolRngT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    seq_name = models.CharField(max_length=88)
    lwr_bdry = models.BigIntegerField()
    upr_bdry = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."bol_rng_t"'

class BusDaysT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    bus_days_cd = models.CharField(max_length=20)
    bus_days_desc = models.CharField(max_length=280)
    bus_day_sun_yn = models.CharField(max_length=1, blank=True)
    bus_day_mon_yn = models.CharField(max_length=1, blank=True)
    bus_day_tue_yn = models.CharField(max_length=1, blank=True)
    bus_day_wed_yn = models.CharField(max_length=1, blank=True)
    bus_day_thr_yn = models.CharField(max_length=1, blank=True)
    bus_day_fri_yn = models.CharField(max_length=1, blank=True)
    bus_day_sat_yn = models.CharField(max_length=1, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."bus_days_t"'

class BusHrsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    bus_hrs_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    bus_hrs = models.CharField(max_length=256)
    hldys = models.CharField(max_length=4000, blank=True)
    daylgt_ofst = models.DecimalField(max_digits=3, decimal_places=2)
    tm_zn_ofst = models.DecimalField(max_digits=4, decimal_places=2)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    class Meta:
        db_table = u'"I2TM_APP"."bus_hrs_t"'

class CachCtlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    enty_name = models.CharField(max_length=50)
    opt_lck = models.BigIntegerField()
    seq = models.BigIntegerField()
    qry = models.CharField(max_length=255)
    dsbl_yn = models.CharField(max_length=1)
    srvr_only_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."cach_ctl_t"'

class CachSyncT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    objclassid = models.BigIntegerField()
    objkey = models.CharField(max_length=256)
    mdfd_dtt = models.DateField()
    op_kind = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."cach_sync_t"'

class CarrAccNumT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    carr_acc_num_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    frht_trm_enu = models.BigIntegerField()
    shpg_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    carr_acc_num = models.CharField(max_length=136)
    acc_actv_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64)
    cust_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    droppicksrvctyp = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."carr_acc_num_t"'

class CarrCustFrhtAdtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    carr_cust_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    carr_cd = models.CharField(max_length=64)
    unmatd_auth_enu = models.BigIntegerField()
    max_var_pos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    max_var_pos_amt = models.DecimalField(max_digits=15, decimal_places=2)
    max_var_neg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    max_var_neg_amt = models.DecimalField(max_digits=15, decimal_places=2)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."carr_cust_frht_adt_t"'

class CarrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    carr_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    name = models.CharField(max_length=280)
    lang_typ = models.BigIntegerField()
    carr_typ = models.BigIntegerField()
    scac_typ = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    ctrc_id_cd = models.CharField(max_length=96, blank=True)
    ctrc_dt = models.DateField(null=True, blank=True)
    cost_ctr_typ = models.BigIntegerField()
    acc_num_cd = models.CharField(max_length=136, blank=True)
    ap_vend_num_cd = models.CharField(max_length=136, blank=True)
    fb_pymt_md_enu = models.BigIntegerField()
    cncy_typ = models.BigIntegerField()
    fax_ebl_yn = models.CharField(max_length=1)
    pkup_led_tm_typ = models.BigIntegerField(null=True, blank=True)
    comp_trkg_yn = models.CharField(max_length=1)
    brcd_typ = models.BigIntegerField()
    prt_lbl_yn = models.CharField(max_length=1)
    prt_bol_yn = models.CharField(max_length=1)
    prt_mnft_yn = models.CharField(max_length=1)
    prt_frht_bill_yn = models.CharField(max_length=1)
    athz_apt_yn = models.CharField(max_length=1)
    ins_exp_dt = models.DateField()
    ins_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    sgl_tdr_need_yn = models.CharField(max_length=1)
    rout_prcn_enu = models.BigIntegerField()
    bol_fmt_typ = models.BigIntegerField(null=True, blank=True)
    shp_lbl_fmt_typ = models.BigIntegerField(null=True, blank=True)
    mnft_fmt_typ = models.BigIntegerField()
    frhtbill_fmt_typ = models.BigIntegerField(null=True, blank=True)
    maxpayvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxpayvarpos_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    maxpayvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxpayvarneg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    srvc_grd_typ = models.BigIntegerField(null=True, blank=True)
    mino_grp_typ = models.BigIntegerField(null=True, blank=True)
    mnft_num_defd_yn = models.CharField(max_length=1)
    fb_num_defd_yn = models.CharField(max_length=1)
    bolnum_fmt_cd = models.CharField(max_length=96)
    bolnum_entaut_yn = models.CharField(max_length=1)
    slc_tff_md_enu = models.BigIntegerField(null=True, blank=True)
    rstd_carr_yn = models.CharField(max_length=1)
    edi_capb = models.BigIntegerField(null=True, blank=True)
    enrt_cmnt = models.BigIntegerField(null=True, blank=True)
    stat_vrfc_enu = models.BigIntegerField()
    ap_trms_typ = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    fb_grp_lvl_enu = models.BigIntegerField()
    vchr_gen_lvl_enu = models.BigIntegerField()
    pyto_carr_cd = models.CharField(max_length=64, blank=True)
    addr_id = models.BigIntegerField()
    usr_cd = models.CharField(max_length=40)
    bus_hrs_ofst_id = models.BigIntegerField()
    ins_notes_mmo_id = models.BigIntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    tdr_rsps_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    intl_carr_yn = models.CharField(max_length=1)
    min_tdr_led_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    nonlive_ld_unld_yn = models.CharField(max_length=1)
    elgb_cnts_mv_yn = models.CharField(max_length=1)
    min_trp_ctn_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    vchr_gen_lvl_trip_enu = models.BigIntegerField()
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    fa_detl_chrg_yn = models.CharField(max_length=1)
    apvchrcncy_enu = models.BigIntegerField()
    cea_actv_yn = models.CharField(max_length=1)
    cea_min_lds = models.BigIntegerField(null=True, blank=True)
    cea_max_lds = models.BigIntegerField(null=True, blank=True)
    cea_pnltymin_lds_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    cea_pnltymax_lds_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    spot_carr_yn = models.CharField(max_length=1)
    max_alw_lwstcost_pct = models.DecimalField(max_digits=5, decimal_places=2)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    elgb_cnts_mv_plnd_yn = models.CharField(max_length=1)
    elgb_cnts_mv_tdrd_yn = models.CharField(max_length=1)
    elgb_cnts_mv_tdr_acpd_yn = models.CharField(max_length=1)
    elgb_cnts_mv_cfmd_yn = models.CharField(max_length=1)
    elgb_cnts_mv_cpld_yn = models.CharField(max_length=1)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    cea_cstr_pct_yn = models.CharField(max_length=1)
    alw_shpm_tdr_yn = models.CharField(max_length=1)
    trip_elgb_ctnn_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."carr_t"'

class CdtyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cdty_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    cdty_desc = models.CharField(max_length=280)
    hzds_yn = models.CharField(max_length=1)
    edi_cdty_cd_typ = models.BigIntegerField(null=True, blank=True)
    cdty_pick_seq_num = models.BigIntegerField(null=True, blank=True)
    extl_cd = models.CharField(max_length=120, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."cdty_t"'

class ChrgDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    chrg_detl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_lvl_enu = models.BigIntegerField()
    prty = models.BigIntegerField(null=True, blank=True)
    unit_typ_enu = models.BigIntegerField(null=True, blank=True)
    lkup_unit_enu = models.BigIntegerField(null=True, blank=True)
    lkup_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    opt_apld_lvl_enu = models.BigIntegerField(null=True, blank=True)
    ratd_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chgd_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    mnly_ovrd_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chgd_unit_rate = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    mnlyovrdunitrate = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    chrg_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    mnly_ovrd_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ratd_at_rng = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    rate_ovrdrsn_typ = models.BigIntegerField(null=True, blank=True)
    ovrd_dtt = models.DateField(null=True, blank=True)
    calc_mthd = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    elmt_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    chrgdetl_typ_enu = models.BigIntegerField()
    rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    adj_lvl_enu = models.BigIntegerField()
    tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    frht_cls_cd = models.CharField(max_length=16, blank=True)
    ratd_as_fc_cd = models.CharField(max_length=16, blank=True)
    usr_cd = models.CharField(max_length=40, blank=True)
    cur_stat_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    vchr_num = models.CharField(max_length=48, blank=True)
    chrg_backcust_yn = models.CharField(max_length=1, blank=True)
    custchrg_gend_yn = models.CharField(max_length=1)
    chrg_detl_rvwd_yn = models.CharField(max_length=1)
    bs_chrg_detl_id = models.BigIntegerField(null=True, blank=True)
    vchr_num_ar = models.CharField(max_length=48, blank=True)
    vchr_num_ap = models.CharField(max_length=48, blank=True)
    gl_acc1 = models.CharField(max_length=120, blank=True)
    gl_acc2 = models.CharField(max_length=120, blank=True)
    gl_acc3 = models.CharField(max_length=120, blank=True)
    gl_acc4 = models.CharField(max_length=120, blank=True)
    pymnt_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    non_op_frht_ap_id = models.BigIntegerField(null=True, blank=True)
    non_op_frht_ar_id = models.BigIntegerField(null=True, blank=True)
    rspb_cust_ovr_id = models.BigIntegerField(null=True, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    ratd_as_eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    trip_lvl_chrg_yn = models.CharField(max_length=1)
    ratg_info_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    pre_pchd_yn = models.CharField(max_length=1)
    apvl_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    apvl_usr_cd = models.CharField(max_length=40, blank=True)
    apvl_dtt = models.DateField(null=True, blank=True)
    cond_is_tax_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."chrg_detl_t"'

class ChrgOvrdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    chrg_ovrd_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_cd = models.CharField(max_length=64)
    optactap_enu = models.BigIntegerField(null=True, blank=True)
    optactap_ovrd_enu = models.BigIntegerField(null=True, blank=True)
    optactar_enu = models.BigIntegerField(null=True, blank=True)
    optactar_ovrd_enu = models.BigIntegerField(null=True, blank=True)
    mnl_unit_ovrd_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.BigIntegerField()
    addr_id = models.BigIntegerField(null=True, blank=True)
    rate_qte_id = models.BigIntegerField(null=True, blank=True)
    mnl_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."chrg_ovrd_t"'

class CnseT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpg_loc_cd = models.CharField(max_length=64)
    stor_num = models.CharField(max_length=40, blank=True)
    gl_cat_typ = models.BigIntegerField(null=True, blank=True)
    drtn_mmo_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    name = models.CharField(max_length=280)
    lang_typ = models.BigIntegerField()
    apt_rqrd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    max_shpm_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_shpm_vol = models.DecimalField(max_digits=11, decimal_places=4)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField()
    mmo_id = models.BigIntegerField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    csldarea_zn_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    loc_emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    opt_lck = models.BigIntegerField()
    cnse_grp_typ = models.BigIntegerField(null=True, blank=True)
    stat_enu = models.BigIntegerField()
    carr_cd = models.CharField(max_length=64, blank=True)
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_unit_typ_enu = models.BigIntegerField(null=True, blank=True)
    unld_unittyp_enu = models.BigIntegerField(null=True, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_lead_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    glrgn_zn_cd = models.CharField(max_length=64)
    live_ld_typ_enu = models.BigIntegerField(null=True, blank=True)
    frst_pick_yn = models.CharField(max_length=1)
    last_drp_yn = models.CharField(max_length=1)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    bdry_rule_enu = models.BigIntegerField(null=True, blank=True)
    tm_zn_ofst = models.DecimalField(max_digits=4, decimal_places=2)
    daylgt_ofst = models.DecimalField(max_digits=3, decimal_places=2)
    inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    inco_shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    max_eqmt_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    dock_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    sde_dr_unld_rqrd_yn = models.CharField(max_length=1)
    near_tail_unld_rqrd_yn = models.CharField(max_length=1)
    shpgloc_pick_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_tm_calc_enu = models.DecimalField(max_digits=20, decimal_places=8)
    live_unld_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."cnse_t"'

class CompTypGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    comp_typ_grp_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    comp_typ_grp_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    rfrc_by_num = models.BigIntegerField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."comp_typ_grp_t"'

class CompTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    comp_typ_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    comp_typ_cd = models.CharField(max_length=80)
    comp_typ_desc = models.CharField(max_length=280)
    lvl = models.BigIntegerField(null=True, blank=True)
    actv_yn = models.CharField(max_length=1)
    max_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    ratgunittyp_enu = models.BigIntegerField()
    rcsv_yn = models.CharField(max_length=1, blank=True)
    tare_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    stkd_on_comp_lvl = models.BigIntegerField(null=True, blank=True)
    stkb_on_comp_lvl = models.BigIntegerField(null=True, blank=True)
    frht_cls_cd = models.CharField(max_length=16, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    dc_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    edi_pck_cd_typ = models.BigIntegerField(null=True, blank=True)
    pkgg_typ_typ = models.BigIntegerField(null=True, blank=True)
    lc_comp_typ = models.BigIntegerField(null=True, blank=True)
    comp_typ_grp_cd = models.CharField(max_length=48)
    rfrc_by_num = models.BigIntegerField(null=True, blank=True)
    itm_gl_cat = models.BigIntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_dtt = models.DateField()
    extl_cd = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."comp_typ_t"'

class CtryT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ctry_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    ctry_name = models.CharField(max_length=280)
    exst_pstl_cd_yn = models.CharField(max_length=1, blank=True)
    ctry_2char_cd = models.CharField(max_length=2)
    sys_prvd_yn = models.CharField(max_length=1)
    addr_fmt_id = models.BigIntegerField(null=True, blank=True)
    geocd_rqrd_yn = models.CharField(max_length=1)
    geocd_eng_typ = models.BigIntegerField(null=True, blank=True)
    dtte_eng_typ = models.BigIntegerField(null=True, blank=True)
    ctry_3num_cd = models.IntegerField(null=True, blank=True)
    ctry_uncar_cd = models.CharField(max_length=3, blank=True)
    ctry_fips_cd = models.CharField(max_length=2, blank=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    ctry_3char_cd = models.CharField(max_length=3, blank=True)
    pstl_hier_num_yn = models.CharField(max_length=1)
    pstl_cd_rqrd_yn = models.CharField(max_length=1)
    addr_fmt_ovrd_yn = models.CharField(max_length=1)
    geocd_extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    dtte_extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ctry_t"'

class CustDrvdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cust_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    ytd_shpms = models.BigIntegerField(null=True, blank=True)
    ytd_tax_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    ytd_dsc_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    ytd_adj_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    ytd_invc_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    cur_shpms = models.BigIntegerField(null=True, blank=True)
    cur_tax_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    cur_dsc_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    cur_adj_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    cur_invc_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    not_invc_val_amt = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."cust_drvd_t"'

class CustShpgLocExtlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cust_shpg_loc_extl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    shpg_loc_cd = models.CharField(max_length=64)
    shpg_loc_typ_enu = models.BigIntegerField()
    extl_cd = models.CharField(max_length=68)
    prfd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    extl_loc_desc = models.CharField(max_length=280, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    cust_shpg_loc_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."cust_shpg_loc_extl_t"'

class CustShpgLocT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cust_shpg_loc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rel_typ_enu = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    shpg_loc_cd = models.CharField(max_length=64)
    shpg_loc_typ_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    droppicksrvctyp = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."cust_shpg_loc_t"'

class CustStstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cust_stst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    num_shpm_hdld = models.BigIntegerField(null=True, blank=True)
    acmdfrhtchrg_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    acmd_dsc_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    acmd_tax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    acmdadjpost_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    acmdmiscchrg_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."cust_stst_t"'

class CustT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cust_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    lang_typ = models.BigIntegerField()
    corp_cust_yn = models.CharField(max_length=1, blank=True)
    prf_ctr_typ = models.BigIntegerField()
    cust_srvcrep_typ = models.BigIntegerField(null=True, blank=True)
    stat_enu = models.BigIntegerField()
    cncy_typ = models.BigIntegerField()
    alw_shpm_yn = models.CharField(max_length=1)
    prt_invc_yn = models.CharField(max_length=1)
    ar_invc_fmt_typ = models.BigIntegerField(null=True, blank=True)
    prt_chrg_invc_yn = models.CharField(max_length=1)
    fax_ebl_yn = models.CharField(max_length=1)
    max_invc_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ar_cdt_trm_typ = models.BigIntegerField(null=True, blank=True)
    ar_acc_num = models.CharField(max_length=136, blank=True)
    brcd_typ = models.BigIntegerField()
    rout_prcn_typ = models.BigIntegerField()
    stat_vrfc_enu = models.BigIntegerField()
    chrg_bsd_carr_yn = models.CharField(max_length=1)
    schg_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    schg_rate = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    mxd_ld_yn = models.CharField(max_length=1)
    tff_sel_ctl_typ = models.BigIntegerField()
    mnft_num_defd_yn = models.CharField(max_length=1)
    tffctrl_rshp_enu = models.BigIntegerField()
    min_odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    ship_frm_typ_enu = models.BigIntegerField(null=True, blank=True)
    ship_to_typ_enu = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    carr_pymt_rqrd_yn = models.CharField(max_length=1)
    div_sel_enu = models.BigIntegerField()
    lgst_grp_sel_enu = models.BigIntegerField()
    bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    corpparn_cust_cd = models.CharField(max_length=64, blank=True)
    cur_cust_ver_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    bus_hrs_ofst_id = models.BigIntegerField()
    sale_pers_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    to_ent_ver_cd = models.CharField(max_length=40)
    cdty_cd = models.CharField(max_length=48)
    frht_cls_cd = models.CharField(max_length=16)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    frm_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    to_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    maxpayvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxpayvarpos_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    maxpayvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxpayvarneg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    invc_grp_lvl_enu = models.BigIntegerField()
    accnum_withcust = models.CharField(max_length=136, blank=True)
    intl_cust_yn = models.CharField(max_length=1)
    invc_num_defd_yn = models.CharField(max_length=1)
    invc_pymt_md_enu = models.BigIntegerField()
    tdr_rsps_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    cnsd_rfrc_num_id = models.BigIntegerField(null=True, blank=True)
    vchrcncy_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    trsp_ebl_yn = models.CharField(max_length=1)
    matd_adt_ebl_yn = models.CharField(max_length=1)
    un_matd_adt_ebl_yn = models.CharField(max_length=1)
    carr_pymt_rblt_enu = models.BigIntegerField()
    matd_adt_qlfr_id = models.BigIntegerField(null=True, blank=True)
    un_matd_adt_qlfr_id = models.BigIntegerField(null=True, blank=True)
    shpm_ent_typ_cd = models.CharField(max_length=8)
    itm_grp_cd = models.CharField(max_length=48, blank=True)
    comp_typ_grp_cd = models.CharField(max_length=48, blank=True)
    vldt_itm = models.BigIntegerField(null=True, blank=True)
    ild_actv_enu = models.BigIntegerField()
    inco_ver_enu = models.BigIntegerField(null=True, blank=True)
    prepaid_seg_only_yn = models.CharField(max_length=1)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    cust_dom_prof_enu = models.BigIntegerField()
    cut_off_adj_day = models.DecimalField(max_digits=20, decimal_places=8)
    prfd_grsmrgn_pct = models.DecimalField(max_digits=5, decimal_places=2)
    strt_adj_day = models.BigIntegerField()
    mxd_trip_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."cust_t"'

class CustVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cust_ver_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    name = models.CharField(max_length=280)
    eftv_frm_dt = models.DateField()
    eftv_to_dt = models.DateField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    cust_tel1_phn = models.CharField(max_length=23, blank=True)
    cust_tel2_phn = models.CharField(max_length=23, blank=True)
    cust_fax_phn = models.CharField(max_length=23, blank=True)
    cust_emal = models.CharField(max_length=100, blank=True)
    cust_url = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."cust_ver_t"'

class DaySchdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frst_set_yn = models.CharField(max_length=1)
    day_of_week_enu = models.BigIntegerField()
    schd_cd = models.CharField(max_length=60)
    opt_lck = models.BigIntegerField()
    ship_tm = models.DateField()
    arvl_week = models.BigIntegerField()
    arvl_day_enu = models.BigIntegerField()
    arvl_tm = models.DateField(null=True, blank=True)
    days_for_dlvy = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."day_schd_t"'

class DcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpg_loc_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    name = models.CharField(max_length=280)
    lang_typ = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    cncy_typ = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    max_shpm_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_shpm_vol = models.DecimalField(max_digits=11, decimal_places=4)
    apt_rqrd_yn = models.CharField(max_length=1, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField()
    mmo_id = models.BigIntegerField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    csldarea_zn_cd = models.CharField(max_length=64, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    loc_emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_unit_typ_enu = models.BigIntegerField(null=True, blank=True)
    unld_unittyp_enu = models.BigIntegerField(null=True, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_lead_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    glrgn_zn_cd = models.CharField(max_length=64)
    gl_cat_typ = models.BigIntegerField(null=True, blank=True)
    live_ld_typ_enu = models.BigIntegerField()
    frst_pick_yn = models.CharField(max_length=1)
    last_drp_yn = models.CharField(max_length=1)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    bdry_rule_enu = models.BigIntegerField(null=True, blank=True)
    tm_zn_ofst = models.DecimalField(max_digits=4, decimal_places=2)
    daylgt_ofst = models.DecimalField(max_digits=3, decimal_places=2)
    inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    inco_shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    max_eqmt_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    dock_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tdr_rsps_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    sde_dr_unld_rqrd_yn = models.CharField(max_length=1)
    near_tail_unld_rqrd_yn = models.CharField(max_length=1)
    odr_grp_ebl_yn = models.CharField(max_length=1)
    shpgloc_pick_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    alw_emty_ld_yn = models.CharField(max_length=1)
    ld_tm_calc_enu = models.DecimalField(max_digits=20, decimal_places=8)
    live_unld_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    trlr_swap_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."dc_t"'

class DeconT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    instance = models.DecimalField(max_digits=20, decimal_places=8)
    datavalue = models.CharField(max_length=2000, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."decon_t"'

class DeleteApfnclDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fncl_ctl_id = models.BigIntegerField()
    delete_ctl_id = models.BigIntegerField(null=True, blank=True)
    ll_id = models.BigIntegerField(null=True, blank=True)
    lld_id = models.BigIntegerField(null=True, blank=True)
    chrg_detl_id = models.BigIntegerField(null=True, blank=True)
    chrg_detl_stat_id = models.BigIntegerField(null=True, blank=True)
    chrg_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pymnt_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chrg_lvl_enu = models.BigIntegerField(null=True, blank=True)
    vchrap_num = models.CharField(max_length=48, blank=True)
    vchrap_opstat_cd = models.BigIntegerField(null=True, blank=True)
    vchrap_hold = models.CharField(max_length=1, blank=True)
    vchrap_held = models.CharField(max_length=1, blank=True)
    vchrap_crtd_dtt = models.DateField(null=True, blank=True)
    vchrap_updt_dtt = models.DateField(null=True, blank=True)
    fbd_id = models.BigIntegerField(null=True, blank=True)
    fbd_cur_stat_id = models.BigIntegerField(null=True, blank=True)
    fb_id = models.BigIntegerField(null=True, blank=True)
    fb_cur_stat_id = models.BigIntegerField(null=True, blank=True)
    fb_hold = models.CharField(max_length=1, blank=True)
    fb_held = models.CharField(max_length=1, blank=True)
    fb_crtd_dtt = models.DateField(null=True, blank=True)
    fb_updt_dtt = models.DateField(null=True, blank=True)
    gl_id = models.BigIntegerField(null=True, blank=True)
    gl_cur_stat_id = models.BigIntegerField(null=True, blank=True)
    gl_crtd_dtt = models.DateField(null=True, blank=True)
    gl_updt_dtt = models.DateField(null=True, blank=True)
    deleted_yn = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."delete_apfncl_detl_t"'

class DlvySchdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dlvy_schd_cd = models.CharField(max_length=60)
    opt_lck = models.BigIntegerField()
    dlvy_schd_desc = models.CharField(max_length=280)
    dftloc_enu = models.BigIntegerField(null=True, blank=True)
    primdate_enu = models.BigIntegerField(null=True, blank=True)
    enfc_geo_hier_yn = models.CharField(max_length=1, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    bus_days_cd = models.CharField(max_length=20, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dlvy_schd_t"'

class DmclEqmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dmcl_eqmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dmcl_cd = models.CharField(max_length=64)
    eqmt_typ_cd = models.CharField(max_length=20)
    availstrt_dtt = models.DateField(null=True, blank=True)
    strtby_dtt = models.DateField(null=True, blank=True)
    reuse_yn = models.CharField(max_length=1, blank=True)
    min_lds = models.BigIntegerField(null=True, blank=True)
    max_lds = models.BigIntegerField(null=True, blank=True)
    pnltymin_lds_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pnltymax_lds_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_trvl_dst = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    cstr_pct_yn = models.CharField(max_length=1)
    maxdhed_btwnld_dst = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    maxret_dst = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    maxreps_dst = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dmcl_eqmt_t"'

class DmclT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dmcl_cd = models.CharField(max_length=64)
    dmcl_name = models.CharField(max_length=280)
    opt_lck = models.BigIntegerField()
    shpglocpnt_enu = models.BigIntegerField(null=True, blank=True)
    shpgloc_cd = models.CharField(max_length=64, blank=True)
    addr_id = models.BigIntegerField()
    carr_cd = models.CharField(max_length=64)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    dspt_zn_cd = models.CharField(max_length=64, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField()
    ebl_opmz_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dmcl_t"'

class DockCdtyExclT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dock_cdty_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dock_id = models.BigIntegerField()
    cdty_cd = models.CharField(max_length=48)
    class Meta:
        db_table = u'"I2TM_APP"."dock_cdty_excl_t"'

class DockCmtdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dock_cmtd_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dock_id = models.BigIntegerField()
    cmtd_strt_dtt = models.DateField(null=True, blank=True)
    cmtd_end_dtt = models.DateField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    cdty_viol_yn = models.CharField(max_length=1)
    eqmt_viol_yn = models.CharField(max_length=1)
    bkd_clsd_yn = models.CharField(max_length=1)
    ovr_bkd_cmtd_yn = models.CharField(max_length=1)
    carr_cd = models.CharField(max_length=64, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    last_sec_cd = models.CharField(max_length=64, blank=True)
    que_id = models.BigIntegerField(null=True, blank=True)
    dock_on_hold_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    class Meta:
        db_table = u'"I2TM_APP"."dock_cmtd_t"'

class DockEqmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dock_eqmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dock_id = models.BigIntegerField()
    eqmt_typ_cd = models.CharField(max_length=20)
    class Meta:
        db_table = u'"I2TM_APP"."dock_eqmt_t"'

class DockT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dock_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dock_cd = models.CharField(max_length=64)
    dock_desc = models.CharField(max_length=280)
    dock_typ_enu = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64)
    shpg_loc_typ_enu = models.BigIntegerField()
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField(null=True, blank=True)
    length = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dock_cmtm_elgb_start_tm_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dock_cmtm_min_led_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    dock_cmtm_cutoff_tm = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dock_t"'

class Domain(models.Model):
    allow_sync = True
    connection_name = 'tm'
    domainid = models.CharField(max_length=4)
    name = models.CharField(max_length=32, blank=True)
    nexthostid = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."domain"'

class DomTabT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tab_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    tab_cd = models.CharField(max_length=80)
    max_cd_len = models.BigIntegerField()
    tab_name = models.CharField(max_length=280)
    sys_mtnd_yn = models.CharField(max_length=1)
    cur_num_vals = models.BigIntegerField()
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    val_cls_id = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."dom_tab_t"'

class DomValT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    val_enu = models.BigIntegerField()
    tab_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    val_cd = models.CharField(max_length=48, blank=True)
    val_desc = models.CharField(max_length=280, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    classid = models.BigIntegerField(null=True, blank=True)
    edirfrcnumtyp_cd = models.CharField(max_length=3, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dom_val_t"'

class DstAdjT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dst_adj_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dst = models.DecimalField(max_digits=6, decimal_places=1)
    dst_adj_pctg = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ttm_fctr = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dst_adj_t"'

class DstCachDelT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    entry_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    class Meta:
        db_table = u'"I2TM_APP"."dst_cach_del_t"'

class DstCachT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    entry_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    loc1 = models.CharField(max_length=512)
    loc2 = models.CharField(max_length=512)
    engid = models.CharField(max_length=80, blank=True)
    engrttyp_enu = models.BigIntegerField(null=True, blank=True)
    dst = models.BigIntegerField()
    ttm = models.BigIntegerField(null=True, blank=True)
    ovrd_yn = models.CharField(max_length=1)
    pnt_a_typ_enu = models.BigIntegerField(null=True, blank=True)
    pnt_b_typ_enu = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    pnt_a_loc_cd = models.CharField(max_length=68, blank=True)
    pnt_b_loc_cd = models.CharField(max_length=68, blank=True)
    ttm_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dst_cach_t"'

class EchgRateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    val_enu = models.BigIntegerField()
    tab_id = models.BigIntegerField()
    drvd_val_cd = models.CharField(max_length=16)
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    euro_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    rndg_prcn = models.BigIntegerField(null=True, blank=True)
    dcml_prcn = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."echg_rate_t"'

class EdiRfrcnumtypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tab_id = models.BigIntegerField()
    val_enu = models.BigIntegerField()
    drvd_val_cd = models.CharField(max_length=48)
    edirfrcnumtyp_cd = models.CharField(max_length=3, blank=True)
    extl_cd = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."edi_rfrcnumtyp_t"'

class ElmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    elmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    parncomp_elmt_id = models.BigIntegerField(null=True, blank=True)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    cur_optlstat_id = models.BigIntegerField()
    ret_optlstat_id = models.BigIntegerField(null=True, blank=True)
    cur_fnclstat_id = models.BigIntegerField()
    ret_fnclstat_id = models.BigIntegerField(null=True, blank=True)
    lic_plat = models.CharField(max_length=20, blank=True)
    cod_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    cod_cash_only_yn = models.CharField(max_length=1)
    len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    grth_size = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    qnty = models.IntegerField()
    parn_fetr_enu = models.BigIntegerField()
    chdn_fetr_enu = models.BigIntegerField()
    ocrn = models.BigIntegerField()
    frm_pkup_dtt = models.DateField()
    to_pkup_dtt = models.DateField()
    frm_dlvy_dtt = models.DateField()
    to_dlvy_dtt = models.DateField()
    codlbl_prtd_tms = models.BigIntegerField()
    comp_typ_id = models.BigIntegerField(null=True, blank=True)
    mrkd_for_cd = models.CharField(max_length=32, blank=True)
    cdty_cd = models.CharField(max_length=48)
    scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    tot_pce = models.BigIntegerField(null=True, blank=True)
    tot_skid = models.BigIntegerField(null=True, blank=True)
    csld_cls = models.CharField(max_length=120, blank=True)
    vchr_run_excp_id = models.BigIntegerField(null=True, blank=True)
    trkg_num = models.CharField(max_length=120, blank=True)
    trkg_qlfr_id = models.BigIntegerField(null=True, blank=True)
    wbfctare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    wbfcscle_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    wbfcfrht_cls_cd = models.CharField(max_length=16, blank=True)
    wbfcnumfrhtcls = models.BigIntegerField(null=True, blank=True)
    ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    comp_desc = models.CharField(max_length=280, blank=True)
    stck_cd = models.BigIntegerField(null=True, blank=True)
    stck_fctr = models.BigIntegerField(null=True, blank=True)
    stck_grp = models.BigIntegerField(null=True, blank=True)
    nest_dimn_enu = models.BigIntegerField(null=True, blank=True)
    nest_val = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_nest_size = models.BigIntegerField(null=True, blank=True)
    cntr_ortn_str = models.CharField(max_length=36, blank=True)
    lc_comp_typ = models.BigIntegerField(null=True, blank=True)
    op_lst_non_emty_yn = models.CharField(max_length=1)
    max_scld_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    ratg_unit_typ_enu = models.BigIntegerField()
    shpm_cntr_num = models.CharField(max_length=140, blank=True)
    shpm_cntr_xref = models.CharField(max_length=120, blank=True)
    itm_gl_cat = models.BigIntegerField(null=True, blank=True)
    inpt_src_enu = models.BigIntegerField()
    mrkedforloc_enu = models.BigIntegerField(null=True, blank=True)
    mrkedforloc_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."elmt_t"'

class EqmtTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    eqmt_typ_cd = models.CharField(max_length=20)
    eqmt_typ_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField(null=True, blank=True)
    lc_eqmt_typ = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    edi_eqmt_typ = models.BigIntegerField(null=True, blank=True)
    len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    usable_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    usable_wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    usable_hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_ld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    umsrsys_enu = models.BigIntegerField()
    umsrwgt_enu = models.BigIntegerField()
    umsrlen_enu = models.BigIntegerField()
    umsrdist_enu = models.BigIntegerField()
    ldpnt1_loc = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    ldpnt1_tare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ldpnt1_max_ld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ldpnt2_loc = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    ldpnt2_tare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ldpnt2_max_ld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ld_unit_typ_enu = models.BigIntegerField(null=True, blank=True)
    unld_unittyp_enu = models.BigIntegerField(null=True, blank=True)
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    extl_cd = models.CharField(max_length=120, blank=True)
    sde_dr_yn = models.CharField(max_length=1)
    sde_dr_loc = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    near_tail_loc = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    drvr_ctl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    eqmt_cat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."eqmt_typ_t"'

class Errormap(models.Model):
    allow_sync = True
    connection_name = 'tm'
    varname = models.CharField(max_length=32)
    errornumber = models.BigIntegerField(null=True, blank=True)
    fcnareaname = models.CharField(max_length=32, blank=True)
    errmsg = models.CharField(max_length=255, blank=True)
    helpmsg = models.CharField(max_length=255, blank=True)
    errorcategory = models.BigIntegerField(null=True, blank=True)
    featureflag = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."errormap"'

class EvntdlvyRcpnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evntdlvy_rcpn_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evntdrstat_enu = models.BigIntegerField()
    evntrcpn_enu = models.BigIntegerField()
    evntdlvymthd_enu = models.BigIntegerField()
    evntdetllvl_enu = models.BigIntegerField()
    rstd_vw_yn = models.CharField(max_length=1)
    enty_cd = models.CharField(max_length=120)
    lang_typ = models.BigIntegerField(null=True, blank=True)
    attn_name = models.CharField(max_length=280, blank=True)
    evntdrfail_enu = models.BigIntegerField(null=True, blank=True)
    retry_cnt = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    evnt_dlvy_id = models.BigIntegerField()
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evntdlvy_rcpn_t"'

class EvntAttrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_id = models.BigIntegerField()
    attr_name = models.CharField(max_length=512)
    opt_lck = models.BigIntegerField()
    posn_num = models.BigIntegerField()
    attr_desc = models.CharField(max_length=280, blank=True)
    tm_cls_name = models.CharField(max_length=128)
    tm_attr_name = models.CharField(max_length=512)
    parn_attr_name = models.CharField(max_length=512, blank=True)
    evnt_rtrv_md_enu = models.BigIntegerField()
    evnt_rptn_qlfr_enu = models.BigIntegerField()
    xml_attr_yn = models.CharField(max_length=1)
    cur_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    reqd_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    temp_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    expn_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_attr_t"'

class EvntDistRcpnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evntdist_rcpn_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evntrcpn_enu = models.BigIntegerField()
    evntdlvymthd_enu = models.BigIntegerField()
    evntdetllvl_enu = models.BigIntegerField()
    rstd_vw_yn = models.CharField(max_length=1)
    ebl_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    evnt_dist_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_dist_rcpn_t"'

class EvntDistT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_dist_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    ebl_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    evnt_notf_id = models.BigIntegerField()
    sbsg_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_dist_t"'

class EvntDlvyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_dlvy_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evntdlvystat_enu = models.BigIntegerField()
    retry_cnt = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    evnt_que_id = models.BigIntegerField()
    sbsg_id = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."evnt_dlvy_t"'

class EvntDroT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_dro_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evntrcpn_enu = models.BigIntegerField()
    evntdlvymthd_enu = models.BigIntegerField()
    evntdetllvl_enu = models.BigIntegerField()
    rstd_vw_yn = models.CharField(max_length=1)
    enty_cd = models.CharField(max_length=120)
    lang_typ = models.BigIntegerField(null=True, blank=True)
    ebl_yn = models.CharField(max_length=1)
    attn_name = models.CharField(max_length=280, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    evntdist_rcpn_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_dro_t"'

class EvntNotfT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_notf_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    evnt_notf_desc = models.CharField(max_length=280, blank=True)
    ebl_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    evnt_id = models.BigIntegerField()
    sec_cd = models.CharField(max_length=64)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    dft_role_typ = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_notf_t"'

class EvntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evnt_enu = models.BigIntegerField()
    xml_name = models.CharField(max_length=280)
    ebl_yn = models.CharField(max_length=1)
    usr_rsn_cd_alwd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_t"'

class ExtlCustacctdefT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    acct_num_id = models.CharField(max_length=120)
    cust_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    attr_desc = models.CharField(max_length=280, blank=True)
    actv_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."extl_custacctdef_t"'

class ExtlCustacctpstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    extl_custacctpst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_lvl_enu = models.BigIntegerField()
    acct_num_id = models.CharField(max_length=120)
    amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pst_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    acct_pstd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    frht_invc_id = models.BigIntegerField()
    non_op_frht_id = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    chrg_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."extl_custacctpst_t"'

class ExtlEginT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    egin_cd = models.CharField(max_length=80)
    sys_prvd_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1, blank=True)
    egin_desc = models.CharField(max_length=280)
    fn_ent_pt = models.CharField(max_length=104)
    data_path = models.CharField(max_length=256, blank=True)
    extlegin_typ = models.BigIntegerField(null=True, blank=True)
    map_grp_cd_enu = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    user_pass = models.CharField(max_length=800, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    logon_cntr = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."extl_egin_t"'

class ExtlEginVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    extl_egin_ver_cd = models.CharField(max_length=60)
    egin_ver_desc = models.CharField(max_length=280)
    egin_typ = models.CharField(max_length=12, blank=True)
    egin_data = models.CharField(max_length=4000, blank=True)
    egin_data2 = models.CharField(max_length=80, blank=True)
    egin_cd = models.CharField(max_length=80)
    map_grp_cd_enu = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    actv_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."extl_egin_ver_t"'

class ExtrInfoT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    extr_info_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    attr_name = models.CharField(max_length=28)
    attr_desc = models.CharField(max_length=280, blank=True)
    attr_val = models.CharField(max_length=200)
    ent_fren_typ_enu = models.BigIntegerField()
    ent_fren_key = models.CharField(max_length=100)
    class Meta:
        db_table = u'"I2TM_APP"."extr_info_t"'

class FbautopymtRunT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    run_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    endd_dtt = models.DateField(null=True, blank=True)
    num_enty_crtd = models.BigIntegerField()
    iniprtd_crtd_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    num_of_vchr_proc = models.BigIntegerField(null=True, blank=True)
    opt_lck = models.BigIntegerField()
    frht_bill_ver_cd = models.CharField(max_length=40)
    prly_prgd_yn = models.CharField(max_length=1)
    carr_cd = models.CharField(max_length=4000, blank=True)
    excl_carr_yn = models.CharField(max_length=1)
    cust_cd = models.CharField(max_length=4000, blank=True)
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."fbautopymt_run_t"'

class FcCrsRfrcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fc_crs_rfrc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_id = models.BigIntegerField()
    fc_cd = models.CharField(max_length=16)
    ratedas_fc_cd = models.CharField(max_length=16)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fc_crs_rfrc_t"'

class FnclApStatnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sta_tnst_dtt = models.DateField()
    rptd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    sec_cd = models.CharField(max_length=64)
    prevstatus_id = models.BigIntegerField()
    ovrd1_hrs_op_yn = models.CharField(max_length=1)
    ovrd2_hrs_op_yn = models.CharField(max_length=1)
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    cur_loc_cty_name = models.CharField(max_length=280, blank=True)
    cur_loc_sta_cd = models.CharField(max_length=16, blank=True)
    cur_loc_ctry_cd = models.CharField(max_length=12, blank=True)
    apt1_frm_dtt = models.DateField(null=True, blank=True)
    apt1_to_dtt = models.DateField(null=True, blank=True)
    apt2_frm_dtt = models.DateField(null=True, blank=True)
    apt2_to_dtt = models.DateField(null=True, blank=True)
    etmd1_dtt = models.DateField(null=True, blank=True)
    etmd2_dtt = models.DateField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_lld_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fncl_ap_statnst_t"'

class FnclArStatnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sta_tnst_dtt = models.DateField()
    rptd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    sec_cd = models.CharField(max_length=64)
    prevstatus_id = models.BigIntegerField()
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    shpm_itm_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fncl_ar_statnst_t"'

class FnclEntyTnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField()
    sta_tnst_dtt = models.DateField()
    rptd_dtt = models.DateField()
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    sec_cd = models.CharField(max_length=64)
    prevstatus_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    vchr_num = models.CharField(max_length=48, blank=True)
    chrg_detl_id = models.BigIntegerField(null=True, blank=True)
    frht_bill_id = models.BigIntegerField(null=True, blank=True)
    frhtbill_detl_id = models.BigIntegerField(null=True, blank=True)
    vchr_num_ap = models.CharField(max_length=48, blank=True)
    vchr_num_ar = models.CharField(max_length=48, blank=True)
    invc_id = models.BigIntegerField(null=True, blank=True)
    invc_detl_id = models.BigIntegerField(null=True, blank=True)
    ap_trns_id = models.BigIntegerField(null=True, blank=True)
    ar_trns_id = models.BigIntegerField(null=True, blank=True)
    gl_trns_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fncl_enty_tnst_t"'

class FnclQueT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    que_id = models.BigIntegerField()
    srvr_id = models.BigIntegerField(null=True, blank=True)
    que_dtt = models.DateField()
    strt_dtt = models.DateField()
    cpld_dtt = models.DateField(null=True, blank=True)
    prty = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    disd_yn = models.CharField(max_length=1)
    usr_cd = models.CharField(max_length=40, blank=True)
    opt_lck = models.BigIntegerField()
    inpt_parm = models.CharField(max_length=4000, blank=True)
    msg_log_id = models.BigIntegerField(null=True, blank=True)
    fncl_req_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    div_cd = models.CharField(max_length=16, blank=True)
    job_name = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fncl_que_t"'

class FrhtBillDetlChrgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frht_bill_detl_chrg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    srvc_lvl_chrg_yn = models.CharField(max_length=1, blank=True)
    frht_bill_detl_id = models.BigIntegerField()
    cur_stat_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    chrg_cd = models.CharField(max_length=64, blank=True)
    chgd_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    chgd_unit_rate = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    frht_cls_cd = models.CharField(max_length=16, blank=True)
    extd_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dsct_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    net_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    aprd_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    vchr_chrg_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    var_pct = models.DecimalField(max_digits=5, decimal_places=2)
    chrg_lvl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."frht_bill_detl_chrg_t"'

class FrhtBillDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frhtinvc_detl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    frhtinvcdetl_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    detl_tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    apvd_detlamt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    apvd_tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    cur_stat_id = models.BigIntegerField()
    frht_invc_id = models.BigIntegerField()
    fb_detl_src_enu = models.BigIntegerField()
    fi_detl_seq_num = models.BigIntegerField()
    rfrc_num = models.CharField(max_length=120, blank=True)
    rfrc_num_typ_enu = models.BigIntegerField(null=True, blank=True)
    vchr_num = models.CharField(max_length=48, blank=True)
    mat_exst_vchr_yn = models.CharField(max_length=1)
    frht_adt_md_enu = models.BigIntegerField()
    aprd_by_usr_cd = models.CharField(max_length=40, blank=True)
    rfrc_num_qlfr_id = models.BigIntegerField(null=True, blank=True)
    usr_rfrc_num = models.CharField(max_length=120, blank=True)
    vchr_chrg_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    vchr_tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    var_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    var_pct = models.DecimalField(max_digits=5, decimal_places=2)
    vchr_held_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."frht_bill_detl_t"'

class FrhtBillT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frht_invc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    crtd_dtt = models.DateField()
    invc_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    tot_fi_amt_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    tot_tax_amt_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    hold_yn = models.CharField(max_length=1)
    held_yn = models.CharField(max_length=1)
    pymt_due_dt = models.DateField()
    fi_prtd_tms = models.BigIntegerField()
    pymt_stat_enum = models.BigIntegerField()
    frhtinvc_vlid_yn = models.CharField(max_length=1)
    cur_stat_id = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    frht_bill_num = models.CharField(max_length=120)
    rcvd_dt = models.DateField()
    frht_bill_src_enu = models.BigIntegerField()
    frht_bill_ver_cd = models.CharField(max_length=40)
    carr_cd = models.CharField(max_length=64)
    updt_dtt = models.DateField(null=True, blank=True)
    sum_fidtlamt_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sum_fidtltax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sm_apvdfidtl_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    smapvddtltax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sum_vchrfrht_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sum_vchr_tax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    ori_frht_invc_id = models.BigIntegerField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    pymt_trms_typ = models.BigIntegerField(null=True, blank=True)
    carr_act_num = models.CharField(max_length=136, blank=True)
    frht_bill_typ = models.BigIntegerField(null=True, blank=True)
    run_id = models.BigIntegerField(null=True, blank=True)
    fb_btch_ctl_id = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    carr_pymt_trms_enu = models.BigIntegerField()
    assn_to_usr_cd = models.CharField(max_length=40, blank=True)
    prly_prgd_yn = models.CharField(max_length=1)
    unmatd_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    matd_var_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    aprd_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    held_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."frht_bill_t"'

class FrhtBillVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frht_bill_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    fiver_desc = models.CharField(max_length=280)
    cut_off_adj_day = models.BigIntegerField()
    hold_fi_crte_yn = models.CharField(max_length=1)
    frhtinvc_adj_day = models.BigIntegerField()
    uniq_postchrg_yn = models.CharField(max_length=1)
    max_fi_per_btch = models.BigIntegerField(null=True, blank=True)
    dft_apvd_amt_enu = models.BigIntegerField()
    prt_rgst_yn = models.CharField(max_length=1)
    one_carr_btch_yn = models.CharField(max_length=1)
    btch_ctl_rqrd_yn = models.CharField(max_length=1)
    frhtbill_fmt_typ = models.BigIntegerField()
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    frht_bill_typ = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=4000, blank=True)
    carr_frht_trm_enu = models.BigIntegerField()
    apvl_lvl_enu = models.BigIntegerField()
    cust_cd = models.CharField(max_length=4000, blank=True)
    imd_rcn_yn = models.CharField(max_length=1)
    strt_adj_day = models.BigIntegerField()
    excl_carr_yn = models.CharField(max_length=1)
    excl_cust_yn = models.CharField(max_length=1)
    init_vchr_yn = models.CharField(max_length=1)
    postchrg_vchr_yn = models.CharField(max_length=1)
    misc_vchr_yn = models.CharField(max_length=1)
    vchr_lvl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    cust_optl_vchr_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."frht_bill_ver_t"'

class FrhtClsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frht_cls_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    frht_cls_desc = models.CharField(max_length=280)
    prty = models.BigIntegerField()
    stat = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."frht_cls_t"'

class FuelEqivChrgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fuel_eqiv_chrg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    fuel_schg_rate_id = models.BigIntegerField()
    tff_cd = models.CharField(max_length=64)
    srvc_cd = models.CharField(max_length=16, blank=True)
    chrg_cd = models.CharField(max_length=64)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fuel_eqiv_chrg_t"'

class FuelRngRateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fuel_rng_rate_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rng_to = models.DecimalField(max_digits=15, decimal_places=4)
    chrg_typ_enu = models.BigIntegerField()
    brk_amt_dlr = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    fuel_schg_rate_id = models.BigIntegerField()
    rng_brk_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fuel_rng_rate_t"'

class FuelSchgPrceT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fuel_schg_prce_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    efct_dt = models.DateField()
    expd_dt = models.DateField()
    fuel_schg_prce_dlr = models.DecimalField(max_digits=11, decimal_places=4)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    fuel_schg_typ_cd = models.CharField(max_length=24)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fuel_schg_prce_t"'

class FuelSchgRateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fuel_schg_rate_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    fuel_rate_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    rng_cd = models.CharField(max_length=16)
    fuel_schg_typ_cd = models.CharField(max_length=24)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fuel_schg_rate_t"'

class FuelSchgTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    fuel_schg_typ_cd = models.CharField(max_length=24)
    opt_lck = models.BigIntegerField()
    fuel_schg_typ_desc = models.CharField(max_length=280)
    cncy_typ = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."fuel_schg_typ_t"'

class FuncT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    func_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    func_desc = models.CharField(max_length=280)
    empl_empl_elgb_yn = models.CharField(max_length=1)
    empl_gnrc_carr_yn = models.CharField(max_length=1)
    empl_spfc_carr_yn = models.CharField(max_length=1)
    empl_gnrc_cust_yn = models.CharField(max_length=1)
    empl_spfc_cust_yn = models.CharField(max_length=1)
    carr_elgb_yn = models.CharField(max_length=1)
    cust_elgb_yn = models.CharField(max_length=1)
    secr_md_enu = models.DecimalField(max_digits=20, decimal_places=8)
    url = models.CharField(max_length=256)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    url_parms = models.CharField(max_length=1024, blank=True)
    upd_yn = models.CharField(max_length=1)
    sdry_mdul_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."func_t"'

class GeoAreaT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    geo_area_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    usr_pstl_cd_from = models.CharField(max_length=48, blank=True)
    usr_pstl_cd_to = models.CharField(max_length=48, blank=True)
    dist = models.DecimalField(max_digits=6, decimal_places=1)
    ctyprc_zip_yn = models.CharField(max_length=1)
    city_name = models.CharField(max_length=280, blank=True)
    sta_cd = models.CharField(max_length=16, blank=True)
    geoarea_prcn_enu = models.BigIntegerField(null=True, blank=True)
    zn_cd = models.CharField(max_length=64)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."geo_area_t"'

class GlAccDsgnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    gl_acc_dsgn_id = models.BigIntegerField()
    gl_clsc_enu = models.BigIntegerField()
    gl_typ = models.BigIntegerField()
    prf_ctr_typ = models.BigIntegerField(null=True, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    oriloc_glcat_typ = models.BigIntegerField(null=True, blank=True)
    destlocglcat_typ = models.BigIntegerField(null=True, blank=True)
    gl_acc_num = models.CharField(max_length=120)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    ori_gl_rgn_zn_cd = models.CharField(max_length=64, blank=True)
    destgl_rgn_zn_cd = models.CharField(max_length=64, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."gl_acc_dsgn_t"'

class GlTrnsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    gl_trns_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    gl_trns_typ_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    gl_acc_num = models.CharField(max_length=120)
    glaccnum_src_enu = models.BigIntegerField()
    cdt_dbt_enu = models.BigIntegerField()
    cust_name = models.CharField(max_length=280)
    rfrc_num = models.CharField(max_length=120)
    chrgdetl_typ_enu = models.BigIntegerField()
    amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    chrg_detl_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    cur_stat_id = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    to_ent_typ_cd = models.CharField(max_length=8, blank=True)
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    cust_cd = models.CharField(max_length=64)
    gl_clsc_enu = models.BigIntegerField()
    rfrc_num_typ_enu = models.BigIntegerField()
    vchr_num = models.CharField(max_length=48)
    classid = models.BigIntegerField()
    frht_bill_num = models.CharField(max_length=120, blank=True)
    frht_bill_id = models.BigIntegerField(null=True, blank=True)
    invc_num = models.CharField(max_length=120, blank=True)
    invc_id = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    gl_typ = models.BigIntegerField(null=True, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    prf_ctr_typ = models.BigIntegerField(null=True, blank=True)
    orilocgl_cat_typ = models.BigIntegerField(null=True, blank=True)
    destlocglcat_typ = models.BigIntegerField(null=True, blank=True)
    carr_name = models.CharField(max_length=280, blank=True)
    btch_seq_num = models.BigIntegerField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    ori_gl_rgn_zn_cd = models.CharField(max_length=64, blank=True)
    destgl_rgn_zn_cd = models.CharField(max_length=64, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    acrl_run_id = models.BigIntegerField(null=True, blank=True)
    trns_run_id = models.BigIntegerField(null=True, blank=True)
    ori_frhtbill_num = models.CharField(max_length=120, blank=True)
    ori_frht_bill_id = models.BigIntegerField(null=True, blank=True)
    acrl_ver_cd = models.CharField(max_length=40, blank=True)
    ori_invc_num = models.CharField(max_length=120, blank=True)
    ori_invc_id = models.BigIntegerField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    intl_carr_cust_yn = models.CharField(max_length=1)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."gl_trns_t"'

class Grouprightassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    groupname = models.CharField(max_length=255)
    rightid = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."grouprightassoc"'

class HeldLogT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    held_log_id = models.BigIntegerField()
    vchrheld_rsn_enu = models.BigIntegerField()
    shpmratgcsld_num = models.CharField(max_length=120, blank=True)
    vchr_num_ap = models.CharField(max_length=48, blank=True)
    vchr_num_ar = models.CharField(max_length=48, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    chrg_detl_id = models.BigIntegerField(null=True, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."held_log_t"'

class HmnTffT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    hmn_tff_cd = models.CharField(max_length=120)
    opt_lck = models.BigIntegerField()
    hmn_tff_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    rfrc_by_num = models.BigIntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."hmn_tff_t"'

class Host(models.Model):
    allow_sync = True
    connection_name = 'tm'
    hostid = models.CharField(max_length=6)
    domainid = models.CharField(max_length=4, blank=True)
    hostname = models.CharField(max_length=128, blank=True)
    isavailable = models.CharField(max_length=1, blank=True)
    nextdeplid = models.BigIntegerField(null=True, blank=True)
    nextimplid = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."host"'

class HubT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpg_loc_cd = models.CharField(max_length=64)
    name = models.CharField(max_length=280)
    lang_typ = models.BigIntegerField()
    apt_rqrd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    max_shpm_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_shpm_vol = models.DecimalField(max_digits=11, decimal_places=4)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField()
    mmo_id = models.BigIntegerField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    csldarea_zn_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    loc_emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    opt_lck = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    drpf_enu = models.BigIntegerField()
    pkup_enu = models.BigIntegerField()
    alw_dcon_yn = models.CharField(max_length=1)
    min_dcon_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_csld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_drp_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    lgst_free_yn = models.CharField(max_length=1, blank=True)
    ebl_alrt_yn = models.CharField(max_length=1, blank=True)
    carr_cd = models.CharField(max_length=64)
    hubexclrgngrp_cd = models.CharField(max_length=48, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_unit_typ_enu = models.BigIntegerField(null=True, blank=True)
    unld_unittyp_enu = models.BigIntegerField(null=True, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_lead_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    glrgn_zn_cd = models.CharField(max_length=64)
    gl_cat_typ = models.BigIntegerField(null=True, blank=True)
    full_srvc_yn = models.CharField(max_length=1)
    live_ld_typ_enu = models.BigIntegerField()
    frst_pick_yn = models.CharField(max_length=1)
    last_drp_yn = models.CharField(max_length=1)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    bdry_rule_enu = models.BigIntegerField(null=True, blank=True)
    tm_zn_ofst = models.DecimalField(max_digits=4, decimal_places=2)
    daylgt_ofst = models.DecimalField(max_digits=3, decimal_places=2)
    inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    inco_shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    max_eqmt_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tsfr_oly_yn = models.CharField(max_length=1, blank=True)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    dock_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tdr_rsps_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    sde_dr_unld_rqrd_yn = models.CharField(max_length=1)
    near_tail_unld_rqrd_yn = models.CharField(max_length=1)
    odr_grp_ebl_yn = models.CharField(max_length=1)
    shpgloc_pick_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_opmz_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_opmz_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_opmz_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_opmz_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_ibnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_ibnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_obnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_obnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_pnlt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_pnlt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_shpm_hold_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_shpm_hold_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    alw_emty_ld_yn = models.CharField(max_length=1)
    ld_tm_calc_enu = models.DecimalField(max_digits=20, decimal_places=8)
    live_unld_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    trlr_swap_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."hub_t"'

class Identity(models.Model):
    allow_sync = True
    connection_name = 'tm'
    name = models.CharField(max_length=254)
    password = models.CharField(max_length=254, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."identity"'

class Identityassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    name = models.CharField(max_length=255)
    roleid = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."identityassoc"'

class IncoTermsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    inco_terms_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    inco_terms_cd = models.CharField(max_length=12)
    inco_ver_enu = models.BigIntegerField()
    inco_terms_desc = models.CharField(max_length=280)
    shpg_loc_src_enu = models.BigIntegerField()
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."inco_terms_t"'

class Inheritence(models.Model):
    allow_sync = True
    connection_name = 'tm'
    iname = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."inheritence"'

class InvcDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frhtinvc_detl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    fi_detl_seq_num = models.BigIntegerField()
    frhtinvcdetl_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    detl_tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    apvd_detlamt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    apvd_tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    cur_stat_id = models.BigIntegerField()
    frht_invc_id = models.BigIntegerField()
    fi_detl_src_enu = models.BigIntegerField()
    rfrc_num_typ_enu = models.BigIntegerField(null=True, blank=True)
    rfrc_num = models.CharField(max_length=120, blank=True)
    vchr_num = models.CharField(max_length=48, blank=True)
    usr_rfrc_num = models.CharField(max_length=120, blank=True)
    vchr_chrg_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    vchr_tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    var_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    var_pct = models.DecimalField(max_digits=5, decimal_places=2)
    vchr_held_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."invc_detl_t"'

class InvcRunT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    run_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    num_enty_crtd = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    invc_ver_cd = models.CharField(max_length=40)
    endd_dtt = models.DateField(null=True, blank=True)
    iniprtd_crtd_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    num_of_vchr_proc = models.BigIntegerField(null=True, blank=True)
    prly_prgd_yn = models.CharField(max_length=1)
    cust_cd = models.CharField(max_length=4000, blank=True)
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."invc_run_t"'

class InvcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    frht_invc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    crtd_dtt = models.DateField()
    invc_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    tot_fi_amt_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    tot_tax_amt_dlr = models.DecimalField(max_digits=21, decimal_places=2)
    hold_yn = models.CharField(max_length=1)
    held_yn = models.CharField(max_length=1)
    pymt_due_dt = models.DateField()
    fi_prtd_tms = models.BigIntegerField()
    pymt_stat_enum = models.BigIntegerField()
    frhtinvc_vlid_yn = models.CharField(max_length=1)
    cur_stat_id = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    fscl_yr = models.IntegerField()
    accg_prid = models.IntegerField()
    invc_num = models.CharField(max_length=120)
    invc_src_enu = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    bill_to_cust_cd = models.CharField(max_length=64)
    invc_ver_cd = models.CharField(max_length=40)
    cust_ver_id = models.BigIntegerField()
    billto_ver_id = models.BigIntegerField()
    rcvd_dt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    sum_fidtlamt_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sum_fidtltax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sm_apvdfidtl_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    smapvddtltax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sum_vchrfrht_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    sum_vchr_tax_dlr = models.DecimalField(null=True, max_digits=21, decimal_places=2, blank=True)
    ori_frht_invc_id = models.BigIntegerField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    invc_typ = models.BigIntegerField(null=True, blank=True)
    pymt_trms_typ = models.BigIntegerField(null=True, blank=True)
    run_id = models.BigIntegerField(null=True, blank=True)
    prly_prgd_yn = models.CharField(max_length=1)
    unmatd_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    matd_var_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    aprd_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    held_detl_num = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."invc_t"'

class InvcVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    invc_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    fiver_desc = models.CharField(max_length=280)
    cut_off_adj_day = models.BigIntegerField()
    hold_fi_crte_yn = models.CharField(max_length=1)
    frhtinvc_adj_day = models.BigIntegerField()
    uniq_postchrg_yn = models.CharField(max_length=1)
    max_fi_per_btch = models.BigIntegerField(null=True, blank=True)
    dft_apvd_amt_enu = models.BigIntegerField()
    prt_rgst_yn = models.CharField(max_length=1)
    one_cust_btch_yn = models.CharField(max_length=1)
    invc_dt_src_enu = models.BigIntegerField()
    invc_fmt_typ = models.BigIntegerField()
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    invc_typ = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=4000, blank=True)
    cust_adj_day_yn = models.CharField(max_length=1)
    strt_adj_day = models.BigIntegerField()
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."invc_ver_t"'

class ItmGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    itm_grp_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    itm_grp_desc = models.CharField(max_length=280)
    nmfc_rqrd_yn = models.CharField(max_length=1)
    hmn_tff_rqrd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    rfrc_by_num = models.BigIntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itm_grp_t"'

class ItmMstrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    itm_num = models.CharField(max_length=120)
    itm_grp_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    itm_desc = models.CharField(max_length=280)
    itm_typ = models.BigIntegerField(null=True, blank=True)
    nmnl_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    stat_enu = models.BigIntegerField()
    seriallotctrl_enu = models.BigIntegerField()
    excl_cat = models.BigIntegerField(null=True, blank=True)
    itm_gl_cat = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    hazmat_cd = models.CharField(max_length=32, blank=True)
    nmfc_cd = models.CharField(max_length=120, blank=True)
    hmn_tff_cd = models.CharField(max_length=120, blank=True)
    frht_cls_cd = models.CharField(max_length=16, blank=True)
    orig_ctry_cd = models.CharField(max_length=16, blank=True)
    cdty_cd = models.CharField(max_length=48)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itm_mstr_t"'

class ItnrLanePerfT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tff_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16)
    frm_itnr_pnt_id = models.BigIntegerField()
    to_itnr_pnt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dlvy_schd_cd = models.CharField(max_length=60)
    itnr_cd = models.CharField(max_length=60)
    ilusrdfd_srvcgrd = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    ilsysgen_srvcgrd = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    usr_grd_hdlg_enu = models.BigIntegerField(null=True, blank=True)
    ilnum_of_trans = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itnr_lane_perf_t"'

class ItnrPntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    itnr_pnt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    itnr_pnt_desc = models.CharField(max_length=280)
    itnr_pnt_seq_num = models.BigIntegerField(null=True, blank=True)
    shpg_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    dlvy_schd_cd = models.CharField(max_length=60)
    itnr_cd = models.CharField(max_length=60)
    itnr_pnt_zn_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itnr_pnt_t"'

class ItnrPntTmtblT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dlvy_schd_cd = models.CharField(max_length=60)
    itnr_tmtbl_cd = models.CharField(max_length=60)
    itnr_tmtbl_ent_cd = models.CharField(max_length=60)
    itnr_pnt_seq_num = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    arvl_tm_frm_dtt = models.DateField(null=True, blank=True)
    arvl_tm_to_dtt = models.DateField(null=True, blank=True)
    dptr_tm_frm_dtt = models.DateField(null=True, blank=True)
    dptr_tm_to_dtt = models.DateField(null=True, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    arvl_dt = models.DateField(null=True, blank=True)
    dptr_dt = models.DateField(null=True, blank=True)
    arvl_wk = models.BigIntegerField(null=True, blank=True)
    arvl_dayofwk_enu = models.BigIntegerField(null=True, blank=True)
    dptr_dayofwk_enu = models.BigIntegerField(null=True, blank=True)
    elpd_days = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itnr_pnt_tmtbl_t"'

class ItnrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dlvy_schd_cd = models.CharField(max_length=60)
    itnr_cd = models.CharField(max_length=60)
    opt_lck = models.BigIntegerField()
    itnr_desc = models.CharField(max_length=280)
    status_enu = models.BigIntegerField(null=True, blank=True)
    itnr_tmtbl_cd = models.CharField(max_length=60, blank=True)
    itnr_tmtbl_ds_cd = models.CharField(max_length=60, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itnr_t"'

class ItnrTmtblEntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dlvy_schd_cd = models.CharField(max_length=60)
    itnr_tmtbl_cd = models.CharField(max_length=60)
    itnr_tmtbl_ent_cd = models.CharField(max_length=60)
    opt_lck = models.BigIntegerField()
    tmtbl_ent_desc = models.CharField(max_length=280)
    tmtbl_datebs_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itnr_tmtbl_ent_t"'

class ItnrTmtblT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dlvy_schd_cd = models.CharField(max_length=60)
    itnr_tmtbl_cd = models.CharField(max_length=60)
    opt_lck = models.BigIntegerField()
    itnr_tmtbl_desc = models.CharField(max_length=280)
    num_of_itnr_pnts = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."itnr_tmtbl_t"'

class JrnyTpltT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    jrny_tplt_cd = models.CharField(max_length=32)
    opt_lck = models.BigIntegerField()
    jrnytplt_desc = models.CharField(max_length=280)
    stat_enu = models.BigIntegerField()
    efct_dt = models.DateField()
    expd_dt = models.DateField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."jrny_tplt_t"'

class LaneAsscT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    lane_assc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    extl_rout_typ = models.BigIntegerField(null=True, blank=True)
    stat_enu = models.BigIntegerField()
    rstc_exst_yn = models.CharField(max_length=1)
    orig_sta_cd = models.CharField(max_length=16, blank=True)
    orig_ctry_cd = models.CharField(max_length=16, blank=True)
    dest_sta_cd = models.CharField(max_length=16, blank=True)
    dest_ctry_cd = models.CharField(max_length=16)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    tff_id = models.BigIntegerField()
    orig_zn_cd = models.CharField(max_length=64, blank=True)
    dest_zn_cd = models.CharField(max_length=64, blank=True)
    orig_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dest_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    base_div_cd = models.CharField(max_length=16)
    dc_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    rstc_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    ratecd_tff_id = models.BigIntegerField(null=True, blank=True)
    rate_cd = models.CharField(max_length=132, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    bs_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    lane_tplt_cd = models.CharField(max_length=48, blank=True)
    num_stop = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    auto_tdr_ovrd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    auto_acpt_ovrd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    srvc_grd_typ_ebl_yn = models.CharField(max_length=1)
    srvc_grd_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    opmz_excl_ovrd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    frht_auct_elgb_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."lane_assc_t"'

class LdatT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpg_loc_cd = models.CharField(max_length=64)
    stor_num = models.CharField(max_length=40, blank=True)
    gl_cat_typ = models.BigIntegerField(null=True, blank=True)
    drtn_mmo_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    name = models.CharField(max_length=280)
    lang_typ = models.BigIntegerField()
    apt_rqrd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    max_shpm_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_shpm_vol = models.DecimalField(max_digits=11, decimal_places=4)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField()
    mmo_id = models.BigIntegerField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    csldarea_zn_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    loc_emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    opt_lck = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    glrgn_zn_cd = models.CharField(max_length=64)
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    var_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    ld_unit_typ_enu = models.BigIntegerField(null=True, blank=True)
    unld_unittyp_enu = models.BigIntegerField(null=True, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_lead_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    live_ld_typ_enu = models.BigIntegerField()
    frst_pick_yn = models.CharField(max_length=1)
    last_drp_yn = models.CharField(max_length=1)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    bdry_rule_enu = models.BigIntegerField(null=True, blank=True)
    tm_zn_ofst = models.DecimalField(max_digits=4, decimal_places=2)
    daylgt_ofst = models.DecimalField(max_digits=3, decimal_places=2)
    inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    inco_shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    max_eqmt_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    dock_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tdr_rsps_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    odr_grp_ebl_yn = models.CharField(max_length=1)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_tm_calc_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."ldat_t"'

class LdngInstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ldng_inst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    inst = models.CharField(max_length=2000)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=44)
    updt_usr_cd = models.CharField(max_length=44, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ldng_inst_t"'

class LdtdrCntcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ldtdr_cntc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    name = models.CharField(max_length=280, blank=True)
    lang_typ = models.BigIntegerField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField()
    ldtdr_cntc_enu = models.BigIntegerField()
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    cntclstlvl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."ldtdr_cntc_t"'

class LdLegDetlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ld_leg_detl_id = models.BigIntegerField()
    nullldlegdetl_yn = models.CharField(max_length=1)
    opt_lck = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    frm_pnt_typ_enu = models.BigIntegerField()
    to_pnt_typ_enu = models.BigIntegerField()
    carr_cmtd_yn = models.CharField(max_length=1)
    srvc_cmtd_yn = models.CharField(max_length=1)
    drct_frht_yn = models.CharField(max_length=1)
    cncy_typ = models.BigIntegerField(null=True, blank=True)
    echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    rshp_rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    spot_rate_yn = models.CharField(max_length=1)
    held_yn = models.CharField(max_length=1)
    qnty_lckd_yn = models.CharField(max_length=1, blank=True)
    rls_func_enu = models.BigIntegerField()
    pick_apt_rqrd_yn = models.CharField(max_length=1)
    drop_apt_rqrd_yn = models.CharField(max_length=1)
    sus_yn = models.CharField(max_length=1)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    cmpd_pkup_ld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    cmpddropunld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mxd_ld_yn = models.CharField(max_length=1)
    frht_trm_enu = models.BigIntegerField()
    ratg_vlid_yn = models.CharField(max_length=1, blank=True)
    bol_prtd_tms = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    rate_cd = models.CharField(max_length=132, blank=True)
    frm_shpg_loc_cd = models.CharField(max_length=64)
    to_shpg_loc_cd = models.CharField(max_length=64)
    frm_shpg_addr_id = models.BigIntegerField(null=True, blank=True)
    to_shpg_addr_id = models.BigIntegerField(null=True, blank=True)
    frm_addr_id = models.BigIntegerField()
    to_addr_id = models.BigIntegerField()
    plan_id = models.BigIntegerField(null=True, blank=True)
    cur_optlstat_id = models.BigIntegerField()
    ret_optlstat_id = models.BigIntegerField(null=True, blank=True)
    que_id = models.BigIntegerField(null=True, blank=True)
    billto_cust_cd = models.CharField(max_length=64)
    lgst_grp_cd = models.CharField(max_length=16)
    div_cd = models.CharField(max_length=16)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    stop_pod_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_pod_id = models.BigIntegerField(null=True, blank=True)
    pick_stop_id = models.BigIntegerField(null=True, blank=True)
    drop_stop_id = models.BigIntegerField(null=True, blank=True)
    cur_fnclstat_id = models.BigIntegerField()
    ret_fnclstat_id = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    sys_calc_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    fedl_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    sta_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    loc_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    adtn_chrg_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    precsld_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    frm_hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    to_hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    csld_cls = models.CharField(max_length=120, blank=True)
    dlvy_seq = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64)
    cmpdpkuparvl_dtt = models.DateField(null=True, blank=True)
    cmpdpkupdptr_dtt = models.DateField(null=True, blank=True)
    cmpddroparvl_dtt = models.DateField(null=True, blank=True)
    cmpddropdptr_dtt = models.DateField(null=True, blank=True)
    acc_num = models.CharField(max_length=136, blank=True)
    pkup_apt_id = models.BigIntegerField(null=True, blank=True)
    drop_apt_id = models.BigIntegerField(null=True, blank=True)
    cfmd_dtt = models.DateField(null=True, blank=True)
    vchrrunexcpap_id = models.BigIntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    edi_204_isud_yn = models.CharField(max_length=1, blank=True)
    ratd_dtt = models.DateField(null=True, blank=True)
    vchrrunexcpar_id = models.BigIntegerField(null=True, blank=True)
    rutd_ori_zn_cd = models.CharField(max_length=64, blank=True)
    rutd_dest_zn_cd = models.CharField(max_length=64, blank=True)
    shpm_optlstat_id = models.BigIntegerField(null=True, blank=True)
    pkup_dptr_dtt = models.DateField(null=True, blank=True)
    pkup_arvl_dtt = models.DateField(null=True, blank=True)
    pkup_date_src = models.BigIntegerField(null=True, blank=True)
    drop_dptr_dtt = models.DateField(null=True, blank=True)
    drop_arvl_dtt = models.DateField(null=True, blank=True)
    drop_date_src = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ = models.BigIntegerField(null=True, blank=True)
    rfrc_num = models.CharField(max_length=120, blank=True)
    rfrc_num_id = models.BigIntegerField(null=True, blank=True)
    bol_qlfr_id = models.BigIntegerField(null=True, blank=True)
    bol_num = models.CharField(max_length=120, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shpm_lgst_grp_cd = models.CharField(max_length=16)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    frm_ctry_cd = models.CharField(max_length=16)
    frm_sta_cd = models.CharField(max_length=16)
    frm_cty_name = models.CharField(max_length=280)
    frm_pstl_cd = models.CharField(max_length=48, blank=True)
    to_ctry_cd = models.CharField(max_length=16)
    to_sta_cd = models.CharField(max_length=16)
    to_cty_name = models.CharField(max_length=280)
    to_pstl_cd = models.CharField(max_length=48, blank=True)
    mrge_csld_cls_id = models.CharField(max_length=120, blank=True)
    mrge_csld_seq_num = models.BigIntegerField(null=True, blank=True)
    urgt_yn = models.CharField(max_length=1)
    bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    non_live_pkup_yn = models.CharField(max_length=1)
    non_live_drpf_yn = models.CharField(max_length=1)
    eqmt_typ = models.CharField(max_length=20, blank=True)
    eqmt_typ_cmtd_yn = models.CharField(max_length=1)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    pick_seq = models.BigIntegerField(null=True, blank=True)
    rate_cd_tff_id = models.BigIntegerField(null=True, blank=True)
    op_lst_non_emty_yn = models.CharField(max_length=1)
    ordr_grp_cd = models.CharField(max_length=16, blank=True)
    cdty_pick_seq_num = models.BigIntegerField(null=True, blank=True)
    comp_trkg_yn = models.CharField(max_length=1)
    cfmg_by_shpmleg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_cat_enu = models.BigIntegerField()
    display_status = models.BigIntegerField(null=True, blank=True)
    driving_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    elpd_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    on_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    off_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    pkup_wait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    drop_wait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tnst_md_enu = models.BigIntegerField(null=True, blank=True)
    tnst_md_cmtd_yn = models.CharField(max_length=1, blank=True)
    frm_shpg_loc_name = models.CharField(max_length=280)
    to_shpg_loc_name = models.CharField(max_length=280)
    schd_actv_yn = models.CharField(max_length=1)
    hd_ld_yn = models.CharField(max_length=1)
    detl_rptd_yn = models.CharField(max_length=1)
    detl_rptd_usr_cd = models.CharField(max_length=40, blank=True)
    detl_rptd_dtt = models.DateField(null=True, blank=True)
    detl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    detl_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_tot_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    detl_tot_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    detl_bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    detl_bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    detl_bs_odrval_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    detl_bs_dcldval_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    rfrc_num1 = models.CharField(max_length=120, blank=True)
    rfrc_num2 = models.CharField(max_length=120, blank=True)
    rfrc_num3 = models.CharField(max_length=120, blank=True)
    rfrc_num4 = models.CharField(max_length=120, blank=True)
    rfrc_num5 = models.CharField(max_length=120, blank=True)
    rfrc_num6 = models.CharField(max_length=120, blank=True)
    rfrc_num7 = models.CharField(max_length=120, blank=True)
    rfrc_num8 = models.CharField(max_length=120, blank=True)
    rfrc_num9 = models.CharField(max_length=120, blank=True)
    rfrc_num10 = models.CharField(max_length=120, blank=True)
    rfrc_num11 = models.CharField(max_length=120, blank=True)
    rfrc_num12 = models.CharField(max_length=120, blank=True)
    rfrc_num13 = models.CharField(max_length=120, blank=True)
    rfrc_num14 = models.CharField(max_length=120, blank=True)
    rfrc_num15 = models.CharField(max_length=120, blank=True)
    rfrc_num16 = models.CharField(max_length=120, blank=True)
    rfrc_num17 = models.CharField(max_length=120, blank=True)
    rfrc_num18 = models.CharField(max_length=120, blank=True)
    rfrc_num19 = models.CharField(max_length=120, blank=True)
    rfrc_num20 = models.CharField(max_length=120, blank=True)
    shpm_desc = models.CharField(max_length=280, blank=True)
    cust_name = models.CharField(max_length=280, blank=True)
    billto_cust_name = models.CharField(max_length=280, blank=True)
    optm_plan_id = models.BigIntegerField(null=True, blank=True)
    ld_src_enu = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_umsr_sys_enu = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_umsr_dist_enu = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_umsr_len_enu = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_umsr_wgt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_cncy_typ = models.DecimalField(max_digits=20, decimal_places=8)
    pick_stop_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dlvy_stop_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shft_seq = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_vbty_id = models.BigIntegerField(null=True, blank=True)
    tff_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    last_ratd_tff_id = models.BigIntegerField(null=True, blank=True)
    wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    eqmt_typ_trctr_cmtd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."ld_leg_detl_t"'

class LdLegT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ld_leg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    cur_optlstat_id = models.BigIntegerField()
    ret_optlstat_id = models.BigIntegerField(null=True, blank=True)
    cur_fnclstat_id = models.BigIntegerField()
    ret_fnclstat_id = models.BigIntegerField(null=True, blank=True)
    ld_typ_enu = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    cncy_typ = models.BigIntegerField(null=True, blank=True)
    echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    trlr_num = models.CharField(max_length=96, blank=True)
    drvr = models.CharField(max_length=32, blank=True)
    seal_num = models.CharField(max_length=64, blank=True)
    ld_term_enu = models.BigIntegerField()
    carr_cmtd_yn = models.CharField(max_length=1)
    srvc_cmtd_yn = models.CharField(max_length=1)
    mile_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    num_shpm = models.BigIntegerField()
    num_stop = models.BigIntegerField()
    mstrbol_prtd_tms = models.BigIntegerField()
    mnft_prtd_tms = models.BigIntegerField()
    edi_204_isud_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    scdd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    shpd_dtt = models.DateField(null=True, blank=True)
    cpld_dtt = models.DateField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    plan_id = models.BigIntegerField(null=True, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    carr_cd = models.CharField(max_length=64, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    rate_cd = models.CharField(max_length=132, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tdrd_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    mnft_ld_grp_cd = models.CharField(max_length=16, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    sys_calc_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    fedl_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    sta_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    loc_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    adtn_chrg_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    precsld_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    scld_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    vol = models.DecimalField(max_digits=11, decimal_places=4)
    odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    dcld_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tare_wgt = models.DecimalField(max_digits=17, decimal_places=4)
    tot_pce = models.BigIntegerField()
    tot_skid = models.BigIntegerField()
    spot_rate_yn = models.CharField(max_length=1)
    ratg_vlid_yn = models.CharField(max_length=1)
    sus_func_enu = models.BigIntegerField()
    detl_retd_yn = models.CharField(max_length=1)
    num_urgt_lld = models.BigIntegerField()
    ld_leg_cat_enu = models.BigIntegerField()
    ld_schd_cmpd_yn = models.CharField(max_length=1)
    que_id = models.BigIntegerField(null=True, blank=True)
    rshp_rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    cfmg_usr_cd = models.CharField(max_length=40, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    lld_carrcmtd_tms = models.BigIntegerField()
    lld_srvccmtd_tms = models.BigIntegerField()
    stop_bult_yn = models.CharField(max_length=1)
    mile_cmpd_yn = models.CharField(max_length=1)
    cdty_cmtd_yn = models.CharField(max_length=1)
    elgb_cnts_mv_enu = models.BigIntegerField(null=True, blank=True)
    tot_shpm = models.BigIntegerField(null=True, blank=True)
    mcldunldstop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    totcexcswait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    tot_tot_pce = models.BigIntegerField(null=True, blank=True)
    tot_tot_skid = models.BigIntegerField(null=True, blank=True)
    acc_num = models.CharField(max_length=136, blank=True)
    team_drvr_yn = models.CharField(max_length=1)
    tdr_acpd_by_name = models.CharField(max_length=280, blank=True)
    vchr_run_excp_id = models.BigIntegerField(null=True, blank=True)
    ratd_dtt = models.DateField(null=True, blank=True)
    rutd_ori_zn_cd = models.CharField(max_length=64, blank=True)
    rutd_dest_zn_cd = models.CharField(max_length=64, blank=True)
    lldheld_num = models.BigIntegerField(null=True, blank=True)
    shpm_cnfm_num = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ = models.BigIntegerField(null=True, blank=True)
    rfrc_num = models.CharField(max_length=120, blank=True)
    rfrc_num_id = models.BigIntegerField(null=True, blank=True)
    mstr_bol_qlfr_id = models.BigIntegerField(null=True, blank=True)
    mstr_bol_num = models.CharField(max_length=120, blank=True)
    out_erp_crtd_dtt = models.DateField(null=True, blank=True)
    out_erp_updt_dtt = models.DateField(null=True, blank=True)
    frst_shpgpnt_enu = models.BigIntegerField(null=True, blank=True)
    frst_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    last_shpgpnt_enu = models.BigIntegerField(null=True, blank=True)
    last_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    frst_ctry_cd = models.CharField(max_length=16, blank=True)
    frst_sta_cd = models.CharField(max_length=16, blank=True)
    frst_cty_name = models.CharField(max_length=280, blank=True)
    frst_pstl_cd = models.CharField(max_length=48, blank=True)
    last_ctry_cd = models.CharField(max_length=16, blank=True)
    last_sta_cd = models.CharField(max_length=16, blank=True)
    last_cty_name = models.CharField(max_length=280, blank=True)
    last_pstl_cd = models.CharField(max_length=48, blank=True)
    tdr_rsps_by_dtt = models.DateField(null=True, blank=True)
    auto_tdr_stat_enu = models.BigIntegerField()
    end_dtt = models.DateField(null=True, blank=True)
    strd_dtt = models.DateField(null=True, blank=True)
    eqmt_typ = models.CharField(max_length=20, blank=True)
    eqmt_typ_cmtd_yn = models.CharField(max_length=1, blank=True)
    eqmt_typ_rqrd_num = models.BigIntegerField(null=True, blank=True)
    ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tot_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    elgb_cnts_mv_yn = models.CharField(max_length=1)
    bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    far_pnt_stop_id = models.BigIntegerField(null=True, blank=True)
    drct_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    outofrout_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    in_tnst_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    init_reps_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ret_to_orig_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    fixd_itnr_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    non_live_pkup_yn = models.CharField(max_length=1)
    non_live_drpf_yn = models.CharField(max_length=1)
    tot_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_desc = models.CharField(max_length=280, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    frst_addr_id = models.BigIntegerField(null=True, blank=True)
    last_addr_id = models.BigIntegerField(null=True, blank=True)
    led_tm_usd_schd_yn = models.CharField(max_length=1)
    rate_cd_tff_id = models.BigIntegerField(null=True, blank=True)
    last_ratd_tff_id = models.BigIntegerField(null=True, blank=True)
    last_ratd_srvc_cd = models.CharField(max_length=16, blank=True)
    op_lst_non_emty_yn = models.CharField(max_length=1)
    num_bill_stop = models.BigIntegerField(null=True, blank=True)
    last_sec_cd = models.CharField(max_length=64, blank=True)
    display_status = models.BigIntegerField(null=True, blank=True)
    frst_stop_id = models.BigIntegerField(null=True, blank=True)
    last_stop_id = models.BigIntegerField(null=True, blank=True)
    actl_carrsrvc = models.CharField(max_length=120, blank=True)
    actl_chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_cncy_typ = models.BigIntegerField(null=True, blank=True)
    tot_driving_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_on_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_off_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mcexcswatstp_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    elpd_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    trctr_onr = models.CharField(max_length=64, blank=True)
    trlr_onr = models.CharField(max_length=64, blank=True)
    drvr_lic_num = models.CharField(max_length=120, blank=True)
    trctr_lic_num = models.CharField(max_length=120, blank=True)
    trlr_lic_num = models.CharField(max_length=120, blank=True)
    frst_shpg_loc_name = models.CharField(max_length=280, blank=True)
    last_shpg_loc_name = models.CharField(max_length=280, blank=True)
    cust_name = models.CharField(max_length=280, blank=True)
    carrldtdr_cntc_id = models.BigIntegerField(null=True, blank=True)
    sndrldtdr_cntc_id = models.BigIntegerField(null=True, blank=True)
    carrldtdrcntc_name = models.CharField(max_length=280, blank=True)
    sndrldtdrcntc_name = models.CharField(max_length=280, blank=True)
    ld_cmps_aprd_yn = models.CharField(max_length=1)
    pre_bult_ld_yn = models.CharField(max_length=1)
    hd_ld_cntr = models.DecimalField(max_digits=20, decimal_places=8)
    optm_plan_id = models.BigIntegerField(null=True, blank=True)
    ld_src_enu = models.DecimalField(max_digits=20, decimal_places=8)
    last_ratd_carr_cd = models.CharField(max_length=64, blank=True)
    lane_assc_id = models.BigIntegerField(null=True, blank=True)
    prfd_grsmrgn_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    etmd_grsmrgn_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    plng_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    plng_stat_ovrd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    last_chngd_mngr_opmr_dtt = models.DateField(null=True, blank=True)
    last_chngd_opmr_dtt = models.DateField(null=True, blank=True)
    carr_soft_cmtd_yn = models.CharField(max_length=1)
    srvc_soft_cmtd_yn = models.CharField(max_length=1, blank=True)
    eqmt_soft_cmtd_yn = models.CharField(max_length=1, blank=True)
    cstr_ovrd_yn = models.CharField(max_length=1)
    num_pmy_stop = models.DecimalField(max_digits=20, decimal_places=8)
    csld_cls = models.CharField(max_length=120, blank=True)
    rfrc_num1 = models.CharField(max_length=120, blank=True)
    rfrc_num2 = models.CharField(max_length=120, blank=True)
    rfrc_num3 = models.CharField(max_length=120, blank=True)
    rfrc_num4 = models.CharField(max_length=120, blank=True)
    rfrc_num5 = models.CharField(max_length=120, blank=True)
    rfrc_num6 = models.CharField(max_length=120, blank=True)
    rfrc_num7 = models.CharField(max_length=120, blank=True)
    rfrc_num8 = models.CharField(max_length=120, blank=True)
    rfrc_num9 = models.CharField(max_length=120, blank=True)
    rfrc_num10 = models.CharField(max_length=120, blank=True)
    rfrc_num11 = models.CharField(max_length=120, blank=True)
    rfrc_num12 = models.CharField(max_length=120, blank=True)
    rfrc_num13 = models.CharField(max_length=120, blank=True)
    rfrc_num14 = models.CharField(max_length=120, blank=True)
    rfrc_num15 = models.CharField(max_length=120, blank=True)
    rfrc_num16 = models.CharField(max_length=120, blank=True)
    rfrc_num17 = models.CharField(max_length=120, blank=True)
    rfrc_num18 = models.CharField(max_length=120, blank=True)
    rfrc_num19 = models.CharField(max_length=120, blank=True)
    rfrc_num20 = models.CharField(max_length=120, blank=True)
    rfrc_num_vbty_id = models.BigIntegerField(null=True, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dmcl_cd = models.CharField(max_length=64, blank=True)
    dmcl_cd_trlr = models.CharField(max_length=64, blank=True)
    dmcl_trctr_cmtd_yn = models.CharField(max_length=1)
    dmcl_trlr_cmtd_yn = models.CharField(max_length=1)
    eqmt_trctr_cmtd_yn = models.CharField(max_length=1)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    eqmt_typ_trctr_rqrd_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    trctr_num = models.CharField(max_length=96, blank=True)
    in_tnst_unldd_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    trctr_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tdr_req_id = models.BigIntegerField(null=True, blank=True)
    wgt_dist_extd = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    cmpr_ld_ratg_id = models.BigIntegerField(null=True, blank=True)
    trip_tff_sav_bas_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."ld_leg_t"'

class LgstGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    lgst_grp_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    lgstgrp_desc = models.CharField(max_length=280)
    stat_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."lgst_grp_t"'

class LgstSysT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cmp_cd = models.CharField(max_length=8)
    opt_lck = models.BigIntegerField()
    secr_key = models.BigIntegerField(null=True, blank=True)
    cmp_name = models.CharField(max_length=280)
    cncy_typ = models.BigIntegerField()
    opmr_cd = models.CharField(max_length=24, blank=True)
    pmy_routcta_enu = models.BigIntegerField()
    sdry_routcta_enu = models.BigIntegerField()
    carr_typ = models.BigIntegerField()
    lang_typ = models.BigIntegerField()
    brcd_typ = models.BigIntegerField()
    csld_cls = models.CharField(max_length=120)
    ship_tm = models.DateField(null=True, blank=True)
    addr_chk_enu = models.BigIntegerField()
    acpt_tdr_yn = models.CharField(max_length=1)
    maxwgtvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxwgtvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    act_enu = models.BigIntegerField()
    maxpayvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxpayvarpos_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    maxpayvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    maxpayvarneg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    rtan_cur_mth = models.BigIntegerField(null=True, blank=True)
    rtan_his_mth = models.BigIntegerField(null=True, blank=True)
    rtan_lvl_yn = models.CharField(max_length=1, blank=True)
    max_trk_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_trk_cube_vol = models.DecimalField(max_digits=11, decimal_places=4)
    fb_grp_lvl_enu = models.BigIntegerField()
    vchr_gen_lvl_enu = models.BigIntegerField()
    carrfbpymtmd_enu = models.BigIntegerField()
    carrcsld_ctl_enu = models.BigIntegerField()
    rshp_rsn_yn = models.CharField(max_length=1)
    rshp_log_num = models.BigIntegerField()
    rshp_minathy_enu = models.BigIntegerField()
    max_pce_ratg_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    rate_ovrd_rsn_yn = models.CharField(max_length=1)
    dis_rshp_yn = models.CharField(max_length=1)
    odr_val_rqrd_yn = models.CharField(max_length=1)
    dcl_val_rqrd_yn = models.CharField(max_length=1)
    prj_id_mdy_yn = models.CharField(max_length=1)
    vldt_itm = models.BigIntegerField()
    dft_dc_frm_la_yn = models.CharField(max_length=1)
    rqr_cnl_rsncd_yn = models.CharField(max_length=1)
    ins_expdsus_days = models.BigIntegerField()
    ins_expdnfy_days = models.BigIntegerField()
    hub_chrgrule1_yn = models.CharField(max_length=1)
    hub_chrgrule2_yn = models.CharField(max_length=1)
    hub_chrgrule3_yn = models.CharField(max_length=1)
    hub_chrgrule4_yn = models.CharField(max_length=1)
    hub_chrgrule5_yn = models.CharField(max_length=1)
    pod_ctl1 = models.BigIntegerField()
    max_fnldhed_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    dlvy_tol_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    auto_rls_ld_yn = models.CharField(max_length=1)
    gl_cdty_lvl_typ = models.BigIntegerField()
    custcsld_ctl_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    bus_hrs_ofst_id = models.BigIntegerField()
    frht_cls_cd = models.CharField(max_length=16)
    to_ent_ver_cd = models.CharField(max_length=40)
    cdty_cd = models.CharField(max_length=48)
    lgst_grp_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    ld_bult_ver_cd = models.CharField(max_length=40, blank=True)
    acptinvlidaddr_yn = models.CharField(max_length=1)
    max_ld_pce = models.BigIntegerField(null=True, blank=True)
    max_ld_skid = models.BigIntegerField(null=True, blank=True)
    mtotexcswait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    safe_arve_wnd_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    mexcswaitstp_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_brk_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_non_brk_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_otrt_mile_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_stop_tnst = models.BigIntegerField(null=True, blank=True)
    max_ll_in_trip = models.BigIntegerField(null=True, blank=True)
    min_lead_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    itvl_chk_opmr = models.BigIntegerField(null=True, blank=True)
    carrcsld_lvl_enu = models.BigIntegerField()
    custinvcvrfc_enu = models.BigIntegerField()
    carr_fb_vrfc_enu = models.BigIntegerField()
    edi_supd_yn = models.CharField(max_length=1, blank=True)
    edi_scac_typ = models.BigIntegerField(null=True, blank=True)
    mnft_vchr_ver_cd = models.CharField(max_length=40)
    apmiscvchrver_cd = models.CharField(max_length=40)
    ap_pschrgver_cd = models.CharField(max_length=40)
    apschdvchrver_cd = models.CharField(max_length=40, blank=True)
    apadhcvchrver_cd = models.CharField(max_length=40)
    adhoc_fb_ver_cd = models.CharField(max_length=40)
    schd_fb_ver_cd = models.CharField(max_length=40, blank=True)
    matpay_fb_ver_cd = models.CharField(max_length=40)
    edi_fb_ver_cd = models.CharField(max_length=10, blank=True)
    edi_stat_usr_cd = models.CharField(max_length=10, blank=True)
    ap_vchrgen_enu = models.BigIntegerField(null=True, blank=True)
    ap_fb_gen_enu = models.BigIntegerField(null=True, blank=True)
    ap_acrlgen_enu = models.BigIntegerField(null=True, blank=True)
    ap_trnsgen_enu = models.BigIntegerField(null=True, blank=True)
    ar_vchrgen_enu = models.BigIntegerField(null=True, blank=True)
    ar_invc_gen_enu = models.BigIntegerField(null=True, blank=True)
    ar_acrlgen_enu = models.BigIntegerField(null=True, blank=True)
    ar_trnsgen_enu = models.BigIntegerField(null=True, blank=True)
    adhoc_ap_ver_cd = models.CharField(max_length=40)
    schd_ap_ver_cd = models.CharField(max_length=40, blank=True)
    apadhcacrlver_cd = models.CharField(max_length=40)
    apschdacrlver_cd = models.CharField(max_length=40, blank=True)
    num_accg_prid = models.BigIntegerField()
    lgst_grp_ctl_enu = models.BigIntegerField()
    ori_glcatctl_enu = models.BigIntegerField()
    destglcatctl_enu = models.BigIntegerField()
    ori_rgn_ctl_enu = models.BigIntegerField()
    dest_rgn_ctl_enu = models.BigIntegerField()
    cdty_ctl_enu = models.BigIntegerField()
    glintfactv_ap_yn = models.CharField(max_length=1)
    db_schm_id = models.CharField(max_length=40, blank=True)
    glintfactv_ar_yn = models.CharField(max_length=1)
    rvnu_cost_ctr_yn = models.CharField(max_length=1)
    cusinvpymtmd_enu = models.BigIntegerField()
    invv_grp_lvl_enu = models.BigIntegerField()
    shmratgdtsrc_enu = models.BigIntegerField()
    custcsld_lvl_enu = models.BigIntegerField()
    no_vchr_held_yn = models.CharField(max_length=1)
    adhoc_invc_ver_cd = models.CharField(max_length=40)
    schd_invc_ver_cd = models.CharField(max_length=40, blank=True)
    adhoc_ar_ver_cd = models.CharField(max_length=40)
    schd_ar_ver_cd = models.CharField(max_length=40, blank=True)
    aradhcacrlver_cd = models.CharField(max_length=40)
    arschdacrlver_cd = models.CharField(max_length=40, blank=True)
    armiscvchrver_cd = models.CharField(max_length=40)
    arpschrg_ver_cd = models.CharField(max_length=40)
    arschdvchrver_cd = models.CharField(max_length=40, blank=True)
    aradhcvchrver_cd = models.CharField(max_length=40)
    edi_invc_ver_cd = models.CharField(max_length=10, blank=True)
    mat_invc_ver_cd = models.CharField(max_length=40)
    erp_send_c_ld_yn = models.CharField(max_length=1)
    umsr_dst_enu = models.BigIntegerField(null=True, blank=True)
    erp_typ = models.BigIntegerField(null=True, blank=True)
    load_if_yn = models.CharField(max_length=1)
    shpm_if_yn = models.CharField(max_length=1)
    mnfst_if_yn = models.CharField(max_length=1)
    fin_if_yn = models.CharField(max_length=1)
    edi_rlse_id = models.BigIntegerField(null=True, blank=True)
    fax_trms_md_yn = models.CharField(max_length=1)
    email_trms_md_yn = models.CharField(max_length=1)
    auto_tdr_ebl_yn = models.CharField(max_length=1)
    auto_tdr_cnl_yn = models.CharField(max_length=1)
    auto_tdr_max_num = models.BigIntegerField(null=True, blank=True)
    min_non_brk_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    pro_ratg_frml_enu = models.BigIntegerField()
    dft_dtte_egin_ver_cd = models.CharField(max_length=15, blank=True)
    dft_dtte_eng_typ = models.BigIntegerField(null=True, blank=True)
    eqmt_typ_cd = models.CharField(max_length=20)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    lc_actv_yn = models.CharField(max_length=1)
    ld_shpd_src_enu = models.BigIntegerField()
    auto_fnl_cnfn_yn = models.CharField(max_length=1)
    frht_adt_vchr_verap_cd = models.CharField(max_length=40, blank=True)
    frht_adt_fb_ver_cd = models.CharField(max_length=40, blank=True)
    usenewreports_yn = models.CharField(max_length=1)
    ild_actv_enu = models.BigIntegerField()
    itm_grp_cd = models.CharField(max_length=48, blank=True)
    comp_typ_grp_cd = models.CharField(max_length=48, blank=True)
    ld_wgtvarpos = models.DecimalField(max_digits=11, decimal_places=4)
    ld_wgtvarneg = models.DecimalField(max_digits=11, decimal_places=4)
    ld_wgtvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    ld_wgtvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    ld_volvarpos = models.DecimalField(max_digits=11, decimal_places=4)
    ld_volvarneg = models.DecimalField(max_digits=11, decimal_places=4)
    ld_volvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    ld_volvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    ld_dstvarpos = models.DecimalField(max_digits=6, decimal_places=1)
    ld_dstvarneg = models.DecimalField(max_digits=6, decimal_places=1)
    ld_dstvarpos_pct = models.DecimalField(max_digits=5, decimal_places=2)
    ld_dstvarneg_pct = models.DecimalField(max_digits=5, decimal_places=2)
    shpm_ent_typ_cd = models.CharField(max_length=8, blank=True)
    orig_ctry_cd = models.CharField(max_length=16, blank=True)
    status_if_yn = models.CharField(max_length=1, blank=True)
    ctry_cd = models.CharField(max_length=16)
    prio_spot_elgb_carr_num = models.BigIntegerField()
    rpt_lvl_enu = models.BigIntegerField()
    lc_min_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    lc_min_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ld_plng_schd_md_yn = models.CharField(max_length=1)
    tmbsd_ratg_actv_yn = models.CharField(max_length=1)
    pnlt_perf_pnt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    pnlt_tnst_md_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_drv_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    no_drvg_beyond_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    maxoffdutystop_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    min_tnst_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    auto_tdr_use_bushrs_yn = models.CharField(max_length=1)
    auto_tdr_min_rsps_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    auto_tdr_max_incr_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    auto_tdr_max_incr_pct = models.DecimalField(max_digits=5, decimal_places=2)
    ld_cmps_aprd_dft_man_yn = models.CharField(max_length=1)
    ld_cmps_aprd_dft_api_yn = models.CharField(max_length=1)
    ld_cmps_aprd_dft_opmr_yn = models.CharField(max_length=1)
    tm_zn_cd = models.CharField(max_length=64, blank=True)
    pos_rptd_tol_days = models.DecimalField(max_digits=20, decimal_places=8)
    neg_rptd_tol_days = models.DecimalField(max_digits=20, decimal_places=8)
    pos_rptd_tol_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    neg_rptd_tol_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    stop_tol_chk_yn = models.CharField(max_length=1)
    sys_tol_chk_yn = models.CharField(max_length=1)
    mnft_ld_grp_cd = models.CharField(max_length=16)
    prtr_name = models.CharField(max_length=128, blank=True)
    csld_alwd_mrge_yn = models.CharField(max_length=1)
    cust_dom_prof_enu = models.BigIntegerField()
    cfmg_rqrd_yn = models.CharField(max_length=1)
    mitcc_strg_enu = models.DecimalField(max_digits=20, decimal_places=8)
    apt_num_rqrd_yn = models.CharField(max_length=1)
    apt_rqrd_bsis_hrs = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    apt_schd_ctl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    grsmrgn_tdr_ebl_yn = models.CharField(max_length=1)
    prfd_grsmrgn_pct = models.DecimalField(max_digits=5, decimal_places=2)
    odr_grp_src_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dft_plng_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    load_elgb_ctnn_enu = models.DecimalField(max_digits=20, decimal_places=8)
    trip_elgb_ctnn_yn = models.CharField(max_length=1)
    dft_tdracptbyusrprof_yn = models.CharField(max_length=1)
    sus_ld_shpmcdty_mod_yn = models.CharField(max_length=1)
    alw_pw_eq_usr_yn = models.CharField(max_length=1)
    rstd_acss_tgt_plan_yn = models.CharField(max_length=1)
    alw_cnnt_opmz_req_yn = models.CharField(max_length=1)
    sec_cust_updtd_yn = models.CharField(max_length=1)
    merge_scrn_updtd_yn = models.CharField(max_length=1)
    merge_srch_updtd_yn = models.CharField(max_length=1)
    merge_list_updtd_yn = models.CharField(max_length=1)
    ld_pkup_dt_tm_var = models.DecimalField(max_digits=6, decimal_places=2)
    ld_dlvy_dt_tm_var = models.DecimalField(max_digits=6, decimal_places=2)
    enfc_div_lgst_grp_rel_yn = models.CharField(max_length=1)
    alt_bus_hrs_ofst_id = models.BigIntegerField(null=True, blank=True)
    carr_max_stat = models.BigIntegerField()
    del_apt_yn = models.CharField(max_length=1)
    rls_mrge_enu = models.DecimalField(max_digits=20, decimal_places=8)
    merge_nav_updtd_yn = models.CharField(max_length=1)
    dft_scrn_hght = models.DecimalField(max_digits=20, decimal_places=8)
    dft_scrn_wdth = models.DecimalField(max_digits=20, decimal_places=8)
    merge_wrkflw_updtd_yn = models.CharField(max_length=1)
    lgst_grp_div_ebl_yn = models.CharField(max_length=1)
    carr_assn_ctl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    merge_chrt_updtd_yn = models.CharField(max_length=1)
    auto_tdr_noncst_enu = models.DecimalField(max_digits=20, decimal_places=8)
    excl_pre_pchd_carr_yn = models.CharField(max_length=1)
    dock_cmtm_rstd_start_tm_yn = models.CharField(max_length=1)
    dock_cmtm_elgb_start_tm_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dock_cmtm_elgb_viol_yn = models.CharField(max_length=1)
    dock_cmtm_dtt_acss_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dock_cmtm_elgb_edit_unassd_yn = models.CharField(max_length=1)
    dock_cmtm_enfc_min_led_tm_yn = models.CharField(max_length=1)
    dock_cmtm_enfc_cutoff_tm_yn = models.CharField(max_length=1)
    dock_cmtm_min_led_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    dock_cmtm_cutoff_tm = models.DateField(null=True, blank=True)
    vchr_adj_autopay_frht_bill_yn = models.CharField(max_length=1)
    ld_plng_ratg_md_yn = models.CharField(max_length=1)
    dpnd_leg_schd_md_enu = models.DecimalField(max_digits=20, decimal_places=8)
    max_dpnd_leg_num = models.IntegerField()
    cmpr_ld_cost_trip_yn = models.CharField(max_length=1)
    plng_tff_trip_min_sav_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."lgst_sys_t"'

class LldPrtgChrgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    lld_prtg_chrg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_lvl_enu = models.BigIntegerField()
    ratd_unit = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    extd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    net_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    chrg_desc = models.CharField(max_length=280, blank=True)
    ld_leg_detl_id = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."lld_prtg_chrg_t"'

class LnAvbltyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ln_avblty_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    actv_yn = models.CharField(max_length=1)
    carr_cd = models.CharField(max_length=64)
    tff_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    min_lds = models.BigIntegerField()
    max_lds = models.BigIntegerField()
    orig_ctry_cd = models.CharField(max_length=16, blank=True)
    orig_sta_cd = models.CharField(max_length=16, blank=True)
    dest_ctry_cd = models.CharField(max_length=16, blank=True)
    dest_sta_cd = models.CharField(max_length=16, blank=True)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    strt_dtt = models.DateField(null=True, blank=True)
    end_dtt = models.DateField(null=True, blank=True)
    orig_zn_cd = models.CharField(max_length=64, blank=True)
    orig_hub_cd = models.CharField(max_length=64, blank=True)
    dest_zn_cd = models.CharField(max_length=64, blank=True)
    dest_hub_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    cstr_pct_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    cea_grp_typ = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."ln_avblty_t"'

class LoadTenderDenorm(models.Model):
    allow_sync = True
    connection_name = 'tm'
    load_sequence = models.IntegerField(null=True, blank=True)
    load_leg_id = models.BigIntegerField(null=True, blank=True)
    scheduled_ship_date = models.DateField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=280, blank=True)
    company_block_building = models.CharField(max_length=40, blank=True)
    company_street_name = models.CharField(max_length=280, blank=True)
    company_city_name = models.CharField(max_length=280, blank=True)
    company_state_code = models.CharField(max_length=16, blank=True)
    company_country_code = models.CharField(max_length=16, blank=True)
    company_postal_code = models.CharField(max_length=48, blank=True)
    carrier_name = models.CharField(max_length=280, blank=True)
    service_description = models.CharField(max_length=280, blank=True)
    terms = models.CharField(max_length=280, blank=True)
    commodity_type_code = models.CharField(max_length=48, blank=True)
    commodity_type_description = models.CharField(max_length=280, blank=True)
    hazardous_yn = models.CharField(max_length=1, blank=True)
    number_of_urgent_shipments = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    load_description = models.CharField(max_length=280, blank=True)
    number_of_skids = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    number_of_pieces = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    scaled_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    volume = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    number_of_shipments = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    number_of_stops = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    unit_of_measure_weight = models.CharField(max_length=280, blank=True)
    unit_of_measure_volume = models.CharField(max_length=280, blank=True)
    equipment_type_description = models.CharField(max_length=280, blank=True)
    comments = models.CharField(max_length=2000, blank=True)
    tendered_by_user = models.CharField(max_length=40, blank=True)
    response_required_by_datetime = models.DateField(null=True, blank=True)
    stop_sequence_number = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_type = models.CharField(max_length=48, blank=True)
    shipping_location_code = models.CharField(max_length=64, blank=True)
    stop_name = models.CharField(max_length=280, blank=True)
    stop_block_building = models.CharField(max_length=40, blank=True)
    stop_street_name = models.CharField(max_length=280, blank=True)
    stop_city_name = models.CharField(max_length=280, blank=True)
    stop_state_code = models.CharField(max_length=16, blank=True)
    stop_country_code = models.CharField(max_length=16, blank=True)
    stop_postal_code = models.CharField(max_length=48, blank=True)
    number_of_pieces_picked_up = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    number_of_skids_picked_up = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    weight_picked_up = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    volume_picked_up = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    number_of_pieces_dropped_off = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    number_of_skids_dropped_off = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    weight_dropped_off = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    volume_dropped_off = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    scheduled_arrival_datetime = models.DateField(null=True, blank=True)
    scheduled_departure_datetime = models.DateField(null=True, blank=True)
    distance_from_previous_stop = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    appointment_name = models.CharField(max_length=128, blank=True)
    appointment_telephone = models.CharField(max_length=23, blank=True)
    appointment_fax = models.CharField(max_length=23, blank=True)
    pickup_laden_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    dropoff_laden_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    load_options = models.CharField(max_length=1024, blank=True)
    load_laden_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    load_total_laden_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tendered_on_datetime = models.DateField()
    base_uom_weight = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    base_uom_volume = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    carrier_uom_weight = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    carrier_uom_volume = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tdr_updt_yn = models.CharField(max_length=1, blank=True)
    head_load_counter = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    carrier_code = models.CharField(max_length=64, blank=True)
    weekend_holiday_break_hours = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    weekend_holiday_start_datetime = models.DateField(null=True, blank=True)
    weekend_holiday_end_datetime = models.DateField(null=True, blank=True)
    weekend_holiday_orientation = models.CharField(max_length=280, blank=True)
    equipment_type_tractor_desc = models.CharField(max_length=280, blank=True)
    tractor_domicile_name = models.CharField(max_length=280, blank=True)
    tractor_number = models.CharField(max_length=96, blank=True)
    trailer_domicile_name = models.CharField(max_length=280, blank=True)
    trailer_number = models.CharField(max_length=96, blank=True)
    tender_request_id = models.BigIntegerField(null=True, blank=True)
    trip_sequence_number = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."load_tender_denorm"'

class MaskValT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ctry_cd = models.CharField(max_length=16)
    mask_enu = models.BigIntegerField()
    mask_val_cd = models.CharField(max_length=128)
    opt_lck = models.BigIntegerField()
    mask_trun_cd = models.CharField(max_length=128, blank=True)
    mask_dist_cd = models.CharField(max_length=128, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mask_val_t"'

class MbolDenorm(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mbol_number = models.CharField(max_length=120, blank=True)
    load_leg_id = models.BigIntegerField(null=True, blank=True)
    planned_ship_date = models.DateField(null=True, blank=True)
    carrier_name = models.CharField(max_length=280, blank=True)
    service_description = models.CharField(max_length=280, blank=True)
    terms = models.CharField(max_length=280, blank=True)
    load_commodity_type = models.CharField(max_length=48, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    container_tracking_yn = models.CharField(max_length=1, blank=True)
    total_number_of_skids = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    total_number_of_pieces = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    total_volume = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    total_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    number_of_shipments = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    number_of_urgent_shipments = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    number_of_stops = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    load_description = models.CharField(max_length=280, blank=True)
    equipment_type_description = models.CharField(max_length=280, blank=True)
    max_num_skids_at_any_time = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_num_pieces_at_any_time = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_volume_at_any_time = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_weight_at_any_time = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    currency_in_use = models.CharField(max_length=48, blank=True)
    unit_of_measure_system_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    unit_of_measure_weight_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    unit_of_measure_length_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    unit_of_measure_system = models.CharField(max_length=48, blank=True)
    unit_of_measure_weight = models.CharField(max_length=48, blank=True)
    unit_of_measure_length = models.CharField(max_length=48, blank=True)
    company_name = models.CharField(max_length=280, blank=True)
    company_block_building = models.CharField(max_length=40, blank=True)
    company_unit_number = models.CharField(max_length=24, blank=True)
    company_street_name = models.CharField(max_length=280, blank=True)
    company_municipality = models.CharField(max_length=280, blank=True)
    company_province_state = models.CharField(max_length=16, blank=True)
    company_postal_zip_code = models.CharField(max_length=48, blank=True)
    company_country = models.CharField(max_length=16, blank=True)
    comments = models.CharField(max_length=2000, blank=True)
    driver_name = models.CharField(max_length=32, blank=True)
    trailer_number = models.CharField(max_length=96, blank=True)
    seal_number = models.CharField(max_length=64, blank=True)
    stop_sequence_number = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    stop_shipping_point = models.CharField(max_length=48, blank=True)
    stop_name = models.CharField(max_length=280, blank=True)
    stop_block_building = models.CharField(max_length=40, blank=True)
    stop_street_name = models.CharField(max_length=280, blank=True)
    stop_unit_number = models.CharField(max_length=128, blank=True)
    stop_municipality = models.CharField(max_length=280, blank=True)
    stop_province_state = models.CharField(max_length=16, blank=True)
    stop_postal_zip_code = models.CharField(max_length=48, blank=True)
    stop_country = models.CharField(max_length=16, blank=True)
    pick_stop_confirmed_yn = models.CharField(max_length=1, blank=True)
    pick_stop_confirmed_by_user = models.CharField(max_length=40, blank=True)
    pick_stop_confirmed_on_date = models.DateField(null=True, blank=True)
    stop_appointment_date_from = models.DateField(null=True, blank=True)
    stop_appointment_date_to = models.DateField(null=True, blank=True)
    stop_scheduled_arrival_date = models.DateField(null=True, blank=True)
    stop_scheduled_departure_date = models.DateField(null=True, blank=True)
    shipment_leg_id = models.BigIntegerField(null=True, blank=True)
    shipment_number = models.CharField(max_length=120, blank=True)
    urgent_shipment_yn = models.CharField(max_length=1, blank=True)
    pickup_or_dropoff_pd = models.CharField(max_length=1, blank=True)
    customer_code = models.CharField(max_length=64, blank=True)
    customer_name = models.CharField(max_length=280, blank=True)
    customer_block_building = models.CharField(max_length=40, blank=True)
    customer_unit_number = models.CharField(max_length=128, blank=True)
    customer_street_name = models.CharField(max_length=280, blank=True)
    customer_municipality = models.CharField(max_length=280, blank=True)
    customer_province_state = models.CharField(max_length=16, blank=True)
    customer_postal_zip_code = models.CharField(max_length=48, blank=True)
    customer_country = models.CharField(max_length=16, blank=True)
    shipment_number_of_skids = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shipment_number_of_pieces = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shipment_volume = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shipment_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shipment_order_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shipment_declared_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    consolidation_class = models.CharField(max_length=120, blank=True)
    consolidation_class_sequence = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    component_type_description = models.CharField(max_length=280, blank=True)
    component_freight_class_code = models.CharField(max_length=16, blank=True)
    component_freight_class_desc = models.CharField(max_length=280, blank=True)
    component_id = models.BigIntegerField(null=True, blank=True)
    component_commodity = models.CharField(max_length=48, blank=True)
    component_quantity = models.IntegerField(null=True, blank=True)
    transport_order_uom_length = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    transport_order_uom_weight = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    torder_uom_length_abbrev = models.CharField(max_length=12, blank=True)
    torder_uom_weight_abbrev = models.CharField(max_length=12, blank=True)
    transport_order_currency = models.CharField(max_length=12, blank=True)
    transport_order_exchange_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    component_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    component_width = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    component_height = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    component_volume = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    component_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    sub_component_freight_class = models.CharField(max_length=16, blank=True)
    sub_component_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    load_laden_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    load_total_laden_length = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    load_options = models.CharField(max_length=1024, blank=True)
    load_reference_numbers = models.CharField(max_length=1024, blank=True)
    shipment_reference_numbers = models.CharField(max_length=1024, blank=True)
    component_reference_numbers = models.CharField(max_length=1024, blank=True)
    shipment_base_volume = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shipment_base_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shipment_base_declared_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shipment_base_order_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shipment_cust_volume = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shipment_cust_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    shipment_cust_declared_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shipment_cust_order_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    shipment_cust_currency_tag = models.CharField(max_length=48, blank=True)
    shipment_cust_volume_tag = models.CharField(max_length=48, blank=True)
    shipment_cust_weight_tag = models.CharField(max_length=48, blank=True)
    ild_exists_yn = models.CharField(max_length=1, blank=True)
    shipment_item_id = models.BigIntegerField(null=True, blank=True)
    shipment_item_number = models.CharField(max_length=120, blank=True)
    item_number = models.CharField(max_length=120, blank=True)
    item_group_code = models.CharField(max_length=48, blank=True)
    item_freight_class_code = models.CharField(max_length=16, blank=True)
    item_description = models.CharField(max_length=280, blank=True)
    item_quantity = models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)
    item_nominal_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    item_extended_nominal_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    item_prorated_scaled_weight = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    item_order_value = models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)
    item_extended_order_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    item_declared_value = models.DecimalField(null=True, max_digits=19, decimal_places=6, blank=True)
    item_extended_declared_value = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    item_reference_numbers = models.CharField(max_length=1024, blank=True)
    head_load_counter = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    head_load_yn = models.CharField(max_length=1, blank=True)
    weekend_holiday_break_hours = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    weekend_holiday_start_datetime = models.DateField(null=True, blank=True)
    weekend_holiday_end_datetime = models.DateField(null=True, blank=True)
    weekend_holiday_orientation = models.CharField(max_length=280, blank=True)
    equipment_type_tractor_desc = models.CharField(max_length=280, blank=True)
    tractor_domicile_name = models.CharField(max_length=280, blank=True)
    tractor_number = models.CharField(max_length=96, blank=True)
    trailer_domicile_name = models.CharField(max_length=280, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mbol_denorm"'

class MnftLdGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mnft_ld_grp_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    mnftld_grp_desc = models.CharField(max_length=280)
    stat_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mnft_ld_grp_t"'

class MntrActyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mntr_acty_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    svrty_reeval_yn = models.CharField(max_length=1)
    svrty_last_chngd_dtt = models.DateField(null=True, blank=True)
    ackngd_dtt = models.DateField(null=True, blank=True)
    alrt_svrty_enu = models.BigIntegerField()
    escl_green_dtt = models.DateField(null=True, blank=True)
    escl_yellow_dtt = models.DateField(null=True, blank=True)
    escl_red_dtt = models.DateField(null=True, blank=True)
    alrt_cat_enu = models.BigIntegerField()
    mntr_stat_enu = models.BigIntegerField()
    svrty_eval_bsis_dtt = models.DateField(null=True, blank=True)
    escl_bsis_dtt = models.DateField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    trip_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    stop_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    ackngd_usr_cd = models.CharField(max_length=40, blank=True)
    alrt_typ_cd = models.CharField(max_length=80)
    carr_cd = models.CharField(max_length=64, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    ship_loc_typ_enu = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    last_sec_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mntr_acty_t"'

class MntrBsNlldT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mntr_bs_nlld_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    ld_leg_detl_id = models.BigIntegerField()
    shpm_num = models.CharField(max_length=120)
    scdd_pkup_arvl_dtt = models.DateField(null=True, blank=True)
    scdd_dlvy_arvl_dtt = models.DateField(null=True, blank=True)
    ltst_dlvy_eta_dtt = models.DateField(null=True, blank=True)
    ltst_dlvy_eta_rptd_dtt = models.DateField(null=True, blank=True)
    actl_pkup_dtt = models.DateField(null=True, blank=True)
    actl_dlvy_dtt = models.DateField(null=True, blank=True)
    frm_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    to_tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    scdd_pkup_arvl_pkup_ackngd_dtt = models.DateField(null=True, blank=True)
    scdd_dlvy_arvl_eta_ackngd_dtt = models.DateField(null=True, blank=True)
    ltst_dlvy_eta_eta_ackngd_dtt = models.DateField(null=True, blank=True)
    scdd_dlvy_arvl_dlvy_ackngd_dtt = models.DateField(null=True, blank=True)
    actl_dlvy_dlvy_ackngd_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mntr_bs_nlld_t"'

class MntrBsStopT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mntr_bs_stop_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    stop_id = models.BigIntegerField()
    ld_leg_id = models.BigIntegerField()
    stop_typ_enu = models.BigIntegerField()
    scdd_arvl_dtt = models.DateField(null=True, blank=True)
    ltst_eta_dtt = models.DateField(null=True, blank=True)
    ltst_eta_rptd_dtt = models.DateField(null=True, blank=True)
    actl_dlvy_dtt = models.DateField(null=True, blank=True)
    tm_zn_ofst = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    scdd_arvl_pkup_ackngd_dtt = models.DateField(null=True, blank=True)
    scdd_arvl_eta_ackngd_dtt = models.DateField(null=True, blank=True)
    ltst_eta_eta_ackngd_dtt = models.DateField(null=True, blank=True)
    scdd_arvl_dlvy_ackngd_dtt = models.DateField(null=True, blank=True)
    actl_dlvy_dlvy_ackngd_dtt = models.DateField(null=True, blank=True)
    svrty_bsis_apt_ackngd_dtt = models.DateField(null=True, blank=True)
    escl_bsis_apt_ackngd_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mntr_bs_stop_t"'

class MntrQueT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    que_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    srvr_id = models.BigIntegerField(null=True, blank=True)
    que_dtt = models.DateField()
    strt_dtt = models.DateField()
    cpld_dtt = models.DateField(null=True, blank=True)
    prty = models.DecimalField(max_digits=20, decimal_places=8)
    stat_enu = models.BigIntegerField()
    disd_yn = models.CharField(max_length=1)
    usr_cd = models.CharField(max_length=40, blank=True)
    msg_log_id = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    root_obj_id = models.BigIntegerField()
    root_obj_stat_enu = models.BigIntegerField()
    num_stop = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    trip_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    situatn_stop_id = models.BigIntegerField(null=True, blank=True)
    situatn_stop_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    ld_schd_cmpd_yn = models.CharField(max_length=1)
    ld_strd_dtt = models.DateField(null=True, blank=True)
    ld_end_dtt = models.DateField(null=True, blank=True)
    rptd_dtt = models.DateField(null=True, blank=True)
    etmd1_dtt = models.DateField(null=True, blank=True)
    etmd2_dtt = models.DateField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    frm_pnt_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    frm_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    to_pnt_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    to_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cfmd_dtt = models.DateField(null=True, blank=True)
    pkup_apt_id = models.BigIntegerField(null=True, blank=True)
    drop_apt_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_pod_id = models.BigIntegerField(null=True, blank=True)
    frm_addr_id = models.BigIntegerField(null=True, blank=True)
    to_addr_id = models.BigIntegerField(null=True, blank=True)
    mntr_situatn_cd = models.CharField(max_length=80)
    sec_cd = models.CharField(max_length=64, blank=True)
    scdd_dtt = models.DateField(null=True, blank=True)
    auto_emal_tdr_yn = models.CharField(max_length=1, blank=True)
    auto_fax_tdr_yn = models.CharField(max_length=1, blank=True)
    auto_edi_tdr_yn = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mntr_que_t"'

class MntrSituatnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mntr_situatn_cd = models.CharField(max_length=80)
    opt_lck = models.BigIntegerField()
    mntr_situatn_desc = models.CharField(max_length=280)
    evnt_enu = models.BigIntegerField()
    sys_prvd_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    sec_cd_avail_yn = models.CharField(max_length=1)
    uncond_gen_que_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mntr_situatn_t"'

class MstrChrgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    chrg_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    chrg_desc = models.CharField(max_length=280)
    chrg_cond_yn = models.CharField(max_length=1)
    unit_typ_enu = models.BigIntegerField()
    lkup_unit_enu = models.BigIntegerField()
    mlti_frgt_cls_yn = models.CharField(max_length=1, blank=True)
    gl_typ = models.BigIntegerField()
    data_acmn_lvl = models.BigIntegerField()
    edi_spclhdlg_typ = models.BigIntegerField(null=True, blank=True)
    edi_spclchrg_typ = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    cond_is_tax_yn = models.CharField(max_length=1, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    fuel_schg_yn = models.CharField(max_length=1)
    eqmt_chrg_yn = models.CharField(max_length=1)
    dsbl_cscd_frm_ar_yn = models.CharField(max_length=1)
    eqmt_cat_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    chrg_detl_prsn_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mstr_chrg_t"'

class MstrSrvcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    srvc_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    srvc_desc = models.CharField(max_length=280)
    gl_typ = models.BigIntegerField()
    max_srvc_hrs = models.IntegerField(null=True, blank=True)
    trsi_md_enu = models.BigIntegerField()
    edi_spclhdlg_typ = models.BigIntegerField(null=True, blank=True)
    edi_spclchrg_typ = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mstr_srvc_t"'

class NmfcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    nmfc_cd = models.CharField(max_length=120)
    opt_lck = models.BigIntegerField()
    nmfc_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    rfrc_by_num = models.BigIntegerField(null=True, blank=True)
    frht_cls_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."nmfc_t"'

class NonOpFrhtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    non_op_frht_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    non_op_frht_num = models.CharField(max_length=120)
    non_op_frht_src_enu = models.BigIntegerField()
    non_op_frht_typ_enu = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    carr_frht_trms_enu = models.BigIntegerField()
    carr_pymt_rblt_enu = models.BigIntegerField()
    cdty_cd = models.CharField(max_length=48)
    cust_cd = models.CharField(max_length=64)
    bill_to_cust_cd = models.CharField(max_length=64)
    carr_cd = models.CharField(max_length=64)
    rate_typ_enu = models.BigIntegerField()
    rvnu_trpt_odr_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    max_num_shpm = models.BigIntegerField()
    non_op_frht_desc = models.CharField(max_length=120, blank=True)
    frst_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    frst_shpgpnt_enu = models.BigIntegerField(null=True, blank=True)
    frst_ctry_cd = models.CharField(max_length=16, blank=True)
    frst_sta_cd = models.CharField(max_length=20, blank=True)
    frst_cty_name = models.CharField(max_length=280, blank=True)
    frst_pstl_cd = models.CharField(max_length=52, blank=True)
    last_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    last_shpgpnt_enu = models.BigIntegerField(null=True, blank=True)
    last_ctry_cd = models.CharField(max_length=16, blank=True)
    last_sta_cd = models.CharField(max_length=20, blank=True)
    last_cty_name = models.CharField(max_length=280, blank=True)
    last_pstl_cd = models.CharField(max_length=52, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    shpd_dtt = models.DateField(null=True, blank=True)
    dlvd_dtt = models.DateField(null=True, blank=True)
    wbfctare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    wbfcscle_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    wbfcfrht_cls_cd = models.CharField(max_length=16, blank=True)
    wbfcnumfrhtcls = models.BigIntegerField(null=True, blank=True)
    tot_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    tot_tot_pce = models.BigIntegerField(null=True, blank=True)
    tot_tot_skid = models.BigIntegerField(null=True, blank=True)
    tot_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    max_tot_pce = models.BigIntegerField(null=True, blank=True)
    max_tot_skid = models.BigIntegerField(null=True, blank=True)
    max_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    drct_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    outofrout_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ret_to_orig_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tot_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    elpd_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    lnst_stop_wait_tm = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    comp_typ_id = models.BigIntegerField(null=True, blank=True)
    prf_ctr_typ = models.BigIntegerField(null=True, blank=True)
    invc_stat_id = models.BigIntegerField(null=True, blank=True)
    init_reps_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    vchr_run_excp_id = models.BigIntegerField(null=True, blank=True)
    ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    ap_ratg_info_id = models.BigIntegerField(null=True, blank=True)
    ar_ratg_info_id = models.BigIntegerField(null=True, blank=True)
    tdpy_loc_cd = models.CharField(max_length=64, blank=True)
    tdpy_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    tdpy_addr_ovrd_id = models.BigIntegerField(null=True, blank=True)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    num_stop = models.BigIntegerField(null=True, blank=True)
    ap_srvc_cd = models.CharField(max_length=16, blank=True)
    ar_srvc_cd = models.CharField(max_length=16, blank=True)
    tot_num_shpm = models.BigIntegerField(null=True, blank=True)
    ap_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ar_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    eqmt_typ_cmtd_yn = models.CharField(max_length=1)
    cust_ver_id = models.BigIntegerField(null=True, blank=True)
    bill_to_ver_id = models.BigIntegerField(null=True, blank=True)
    tdpy_addr_id = models.BigIntegerField(null=True, blank=True)
    driving_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_wait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    on_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    off_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tnst_md_enu = models.BigIntegerField(null=True, blank=True)
    mat_rfrc_num = models.CharField(max_length=120, blank=True)
    mat_rfrc_num_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    mat_rfrc_num_qlfr_id = models.BigIntegerField(null=True, blank=True)
    frst_shpg_loc_name = models.CharField(max_length=280, blank=True)
    last_shpg_loc_name = models.CharField(max_length=280, blank=True)
    num_pmy_stop = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dmcl_cd_trctr = models.CharField(max_length=64, blank=True)
    dmcl_cd_trlr = models.CharField(max_length=64, blank=True)
    dmcl_trctr_cmtd_yn = models.CharField(max_length=1)
    dmcl_trlr_cmtd_yn = models.CharField(max_length=1)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    eqmt_typ_trctr_cmtd_yn = models.CharField(max_length=1)
    trctr_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."non_op_frht_t"'

class NonOpStopT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    stop_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    shpm_pick = models.BigIntegerField()
    shpm_drop = models.BigIntegerField()
    addr_id = models.BigIntegerField()
    non_op_frht_id = models.BigIntegerField()
    shpg_pnt_enu = models.BigIntegerField(null=True, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_addr_id = models.BigIntegerField(null=True, blank=True)
    pick_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    pick_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    pick_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pick_dcldval_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pick_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    pick_tottare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    pick_tot_pce = models.BigIntegerField(null=True, blank=True)
    pick_tot_skid = models.BigIntegerField(null=True, blank=True)
    pick_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    drop_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    drop_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    drop_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    drop_dcldval_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    drop_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    drop_tottare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    drop_tot_pce = models.BigIntegerField(null=True, blank=True)
    drop_tot_skid = models.BigIntegerField(null=True, blank=True)
    drop_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    pick_dtt = models.DateField(null=True, blank=True)
    drop_dtt = models.DateField(null=True, blank=True)
    cdty_note = models.CharField(max_length=280, blank=True)
    stop_typ_enu = models.BigIntegerField()
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."non_op_stop_t"'

class NonOpWgtByFrhtclsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    wgt_frht_cls_id = models.BigIntegerField()
    frht_cls_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    non_op_frht_id = models.BigIntegerField()
    tare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    scle_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."non_op_wgt_by_frhtcls_t"'

class Operationaccess(models.Model):
    allow_sync = True
    connection_name = 'tm'
    target = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    groupname = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."operationaccess"'

class OpmrCstrovrdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tab_id = models.BigIntegerField()
    val_enu = models.BigIntegerField()
    opmr_cstrovrd_file = models.CharField(max_length=256)
    class Meta:
        db_table = u'"I2TM_APP"."opmr_cstrovrd_t"'

class OpmrQueT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    que_id = models.BigIntegerField()
    srvr_id = models.BigIntegerField(null=True, blank=True)
    que_dtt = models.DateField()
    strt_dtt = models.DateField()
    cpld_dtt = models.DateField(null=True, blank=True)
    prty = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    plan_id = models.BigIntegerField(null=True, blank=True)
    usr_cd = models.CharField(max_length=40, blank=True)
    disd_yn = models.CharField(max_length=1)
    msg_log_id = models.BigIntegerField(null=True, blank=True)
    trip_bld_yn = models.CharField(max_length=1, blank=True)
    overridefile = models.CharField(max_length=400, blank=True)
    fmxbillrun_id = models.BigIntegerField(null=True, blank=True)
    fmxcollectrun_id = models.BigIntegerField(null=True, blank=True)
    fmxcollectrun_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    num_shpmleg = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    opmz_strd_dtt = models.DateField(null=True, blank=True)
    ld_sel_cta = models.CharField(max_length=4000, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    frht_trm_enu = models.DecimalField(max_digits=20, decimal_places=8)
    csld_cls = models.CharField(max_length=120, blank=True)
    slc_ld_cmpb_shpm_yn = models.CharField(max_length=1)
    incl_elgb_trip_yn = models.CharField(max_length=1)
    slc_trip_cmpb_shpm_yn = models.CharField(max_length=1)
    trip_sel_cta = models.CharField(max_length=4000, blank=True)
    mxd_trip_yn = models.CharField(max_length=1)
    opmr_insn_grp_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."opmr_que_t"'

class OpApStatnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sta_tnst_dtt = models.DateField()
    sec_cd = models.CharField(max_length=64)
    prevstatus_id = models.BigIntegerField()
    rptd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    ovrd1_hrs_op_yn = models.CharField(max_length=1)
    ovrd2_hrs_op_yn = models.CharField(max_length=1)
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    cur_loc_cty_name = models.CharField(max_length=280, blank=True)
    cur_loc_sta_cd = models.CharField(max_length=16, blank=True)
    cur_loc_ctry_cd = models.CharField(max_length=12, blank=True)
    apt1_frm_dtt = models.DateField(null=True, blank=True)
    apt1_to_dtt = models.DateField(null=True, blank=True)
    apt2_frm_dtt = models.DateField(null=True, blank=True)
    apt2_to_dtt = models.DateField(null=True, blank=True)
    etmd1_dtt = models.DateField(null=True, blank=True)
    etmd2_dtt = models.DateField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_lld_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    alt_ld_leg_id = models.BigIntegerField(null=True, blank=True)
    alt_trip_id = models.BigIntegerField(null=True, blank=True)
    alt_ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."op_ap_statnst_t"'

class OpArStatnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sta_tnst_dtt = models.DateField()
    rptd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    sec_cd = models.CharField(max_length=64)
    prevstatus_id = models.BigIntegerField()
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    shpm_itm_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."op_ar_statnst_t"'

class ParmCnstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cnst_id = models.BigIntegerField()
    parm_name = models.CharField(max_length=63, blank=True)
    set_typ_name = models.CharField(max_length=63, blank=True)
    rng_yn = models.CharField(max_length=1, blank=True)
    val_lo = models.CharField(max_length=512, blank=True)
    val_hi = models.CharField(max_length=512, blank=True)
    opt_lck = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."parm_cnst_t"'

class ParmSetT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    set_name = models.CharField(max_length=63)
    set_typ_name = models.CharField(max_length=63, blank=True)
    ver = models.BigIntegerField(null=True, blank=True)
    opt_lck = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."parm_set_t"'

class ParmSetTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    set_typ_name = models.CharField(max_length=63)
    opt_lck = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."parm_set_typ_t"'

class ParmValT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    set_name = models.CharField(max_length=63)
    parm_name = models.CharField(max_length=63)
    val = models.CharField(max_length=512, blank=True)
    dat_typ = models.BigIntegerField(null=True, blank=True)
    dynm_yn = models.CharField(max_length=1, blank=True)
    opt_lck = models.BigIntegerField()
    is_dft_yn = models.CharField(max_length=1, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."parm_val_t"'

class ParmValTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    parm_name = models.CharField(max_length=63)
    set_typ_name = models.CharField(max_length=63)
    dat_typ = models.BigIntegerField(null=True, blank=True)
    dft_val = models.CharField(max_length=512, blank=True)
    dynm_yn = models.CharField(max_length=1, blank=True)
    opt_lck = models.BigIntegerField()
    help = models.CharField(max_length=2000, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."parm_val_typ_t"'

class PayableCarrOvrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    payable_carr_ovr_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    chrg_cd = models.CharField(max_length=64)
    payable_carr_enu = models.BigIntegerField()
    payable_carr_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."payable_carr_ovr_t"'

class PersT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    pers_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    name = models.CharField(max_length=280)
    lang_typ = models.BigIntegerField(null=True, blank=True)
    role_typ = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64, blank=True)
    hub_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ldat_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cnse_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dc_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    dmcl_cd = models.CharField(max_length=64, blank=True)
    pmy_cntc_yn = models.CharField(max_length=1)
    tff_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."pers_t"'

class PlanT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    plan_id = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    opt_lck = models.BigIntegerField()
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    plan_desc = models.CharField(max_length=280, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."plan_t"'

class PodT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    pod_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    pod_desc = models.CharField(max_length=280, blank=True)
    pod_dtt = models.DateField(null=True, blank=True)
    pod_tot_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    pod_tot_pce = models.BigIntegerField(null=True, blank=True)
    pod_tot_skid = models.BigIntegerField(null=True, blank=True)
    pod_sig = models.CharField(max_length=128, blank=True)
    pod_usr_cd = models.CharField(max_length=40, blank=True)
    rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    sec_cd = models.CharField(max_length=64, blank=True)
    extl_cd = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."pod_t"'

class RateCdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_cd = models.CharField(max_length=132)
    tff_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    ratecd_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rate_cd_t"'

class RateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rate_for_shpm_yn = models.CharField(max_length=1)
    bs_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    chrg_cd = models.CharField(max_length=64)
    rng_cd = models.CharField(max_length=16, blank=True)
    num_of_rng_rate = models.BigIntegerField()
    rate_cd = models.CharField(max_length=132)
    frht_cls_cd = models.CharField(max_length=16)
    tff_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16)
    chrg_id = models.BigIntegerField()
    efct_dt = models.DateField(null=True, blank=True)
    expd_dt = models.DateField(null=True, blank=True)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rate_t"'

class RatgInfoT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ratg_info_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    spot_rate_yn = models.CharField(max_length=1)
    cncy_typ = models.BigIntegerField(null=True, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    spot_rate_dtt = models.DateField(null=True, blank=True)
    ratd_dtt = models.DateField(null=True, blank=True)
    rshp_rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    rate_cd = models.CharField(max_length=132, blank=True)
    rate_cd_tff_id = models.BigIntegerField(null=True, blank=True)
    spot_rate_usr_cd = models.CharField(max_length=40, blank=True)
    sys_calc_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    fedl_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    sta_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    loc_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    adtn_chrg_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    precsld_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    last_ratd_tff_id = models.BigIntegerField(null=True, blank=True)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    dmcl_cd_trctr = models.CharField(max_length=64, blank=True)
    dmcl_cd_trlr = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ratg_info_t"'

class ReportRequests(models.Model):
    allow_sync = True
    connection_name = 'tm'
    request_id = models.IntegerField()
    primary_key_numeric = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."report_requests"'

class ReDeleteT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    crtd_dtt = models.DateField(null=True, blank=True)
    delete_type = models.BigIntegerField(null=True, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    geo_area_id = models.BigIntegerField(null=True, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    lane_assc_id = models.BigIntegerField(null=True, blank=True)
    zn_cd = models.CharField(max_length=64, blank=True)
    drvd_val_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    fc_crs_rfrc_id = models.BigIntegerField(null=True, blank=True)
    egin_cd = models.CharField(max_length=40, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    dlvy_schd_cd = models.CharField(max_length=60, blank=True)
    dmcl_cd = models.CharField(max_length=64, blank=True)
    dmcl_eqmt_id = models.BigIntegerField(null=True, blank=True)
    dmcl_vhcl_avblty_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."re_delete_t"'

class ReUpdateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    entity_type = models.CharField(max_length=50, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."re_update_t"'

class RfrcNumCatT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rfrc_num_cat_enu = models.BigIntegerField()
    rfrc_num_qlfr_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    mdy_yn = models.CharField(max_length=1)
    rqrd_by_stat_enu = models.BigIntegerField()
    prt_at_stat_enu = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."rfrc_num_cat_t"'

class RfrcNumQlfrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rfrc_num_qlfr_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rfrc_num_typ = models.BigIntegerField()
    rfrcentyqlfr_enu = models.BigIntegerField()
    auto_pop_flag_yn = models.CharField(max_length=1)
    rfrcnum_prgm_typ = models.BigIntegerField(null=True, blank=True)
    uniq_rfrc_num_yn = models.CharField(max_length=1, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    cnse_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    ldat_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    hub_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    comp_typ_id = models.BigIntegerField(null=True, blank=True)
    ent_cd = models.CharField(max_length=112, blank=True)
    actv_yn = models.CharField(max_length=1)
    rfrcnumfmt_enu = models.BigIntegerField(null=True, blank=True)
    rfrcentyqlfr2_enu = models.BigIntegerField(null=True, blank=True)
    rfrcentyqlfr3_enu = models.BigIntegerField(null=True, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    auto_gen = models.CharField(max_length=1, blank=True)
    length = models.BigIntegerField(null=True, blank=True)
    literal = models.CharField(max_length=120, blank=True)
    str_free_pos = models.BigIntegerField(null=True, blank=True)
    end_free_pos = models.BigIntegerField(null=True, blank=True)
    chk_typ_enu = models.BigIntegerField(null=True, blank=True)
    str_seq_pos = models.BigIntegerField(null=True, blank=True)
    extlgenegin_ver = models.CharField(max_length=60, blank=True)
    seq_cd = models.CharField(max_length=32, blank=True)
    sys_prvd_yn = models.CharField(max_length=1, blank=True)
    enfc_uniq = models.CharField(max_length=1)
    enfc_uniqinent = models.CharField(max_length=1, blank=True)
    link_to_ap_yn = models.CharField(max_length=1)
    rollover_yn = models.CharField(max_length=1)
    min_elpd_days = models.BigIntegerField(null=True, blank=True)
    original_qlfr_id = models.BigIntegerField(null=True, blank=True)
    mirrored_qlfr_id = models.BigIntegerField(null=True, blank=True)
    arch_dltd_yn = models.CharField(max_length=1)
    dpld_ebl_yn = models.CharField(max_length=1)
    empl_auth_enu = models.DecimalField(max_digits=20, decimal_places=8)
    carr_auth_enu = models.DecimalField(max_digits=20, decimal_places=8)
    cust_auth_enu = models.DecimalField(max_digits=20, decimal_places=8)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rfrc_num_qlfr_t"'

class RfrcNumT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rfrc_num_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rfrc_num_typ = models.BigIntegerField()
    rfrc_num = models.CharField(max_length=120)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    stop_id = models.BigIntegerField(null=True, blank=True)
    rfrc_num_qlfr_id = models.BigIntegerField()
    frht_bill_id = models.BigIntegerField(null=True, blank=True)
    invc_id = models.BigIntegerField(null=True, blank=True)
    vchr_num_ap = models.CharField(max_length=48, blank=True)
    vchr_num_ar = models.CharField(max_length=48, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    comp_lld_id = models.BigIntegerField(null=True, blank=True)
    comp_lld_elmt_id = models.BigIntegerField(null=True, blank=True)
    comp_shpm_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    non_op_stop_id = models.BigIntegerField(null=True, blank=True)
    frhtinvc_detl_id = models.BigIntegerField(null=True, blank=True)
    shpm_itm_id = models.BigIntegerField(null=True, blank=True)
    shpm_itm_shpm_id = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_dtt = models.DateField()
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rfrc_num_t"'

class Rightassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    id_field = models.CharField(max_length=254)
    rightid = models.CharField(max_length=254)
    class Meta:
        db_table = u'"I2TM_APP"."rightassoc"'

class Rightvalues(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rightid = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."rightvalues"'

class RngBrkT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rng_brk_id = models.BigIntegerField()
    rng_to = models.DecimalField(max_digits=15, decimal_places=4)
    opt_lck = models.BigIntegerField()
    chrg_typ_enu = models.BigIntegerField()
    clip_yn = models.CharField(max_length=1)
    rng_cd = models.CharField(max_length=16)
    class Meta:
        db_table = u'"I2TM_APP"."rng_brk_t"'

class RngCdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rng_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    rng_desc = models.CharField(max_length=280)
    shrd_cntr = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rng_cd_t"'

class RngRateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rng_rate_id = models.BigIntegerField()
    rng_cd = models.CharField(max_length=16)
    rng_to = models.DecimalField(max_digits=15, decimal_places=4)
    opt_lck = models.BigIntegerField()
    chrg_typ_enu = models.BigIntegerField()
    clip_yn = models.CharField(max_length=1)
    brk_bs_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    brk_amt_dlr = models.DecimalField(max_digits=11, decimal_places=4)
    vlid_yn = models.CharField(max_length=1)
    rate_id = models.BigIntegerField()
    rng_brk_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rng_rate_t"'

class Role(models.Model):
    allow_sync = True
    connection_name = 'tm'
    roleid = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."role'

class Roleassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    roleid = models.CharField(max_length=254)
    roleid_field = models.CharField(max_length=254)
    class Meta:
        db_table = u'"I2TM_APP"."roleassoc"'

class Rolerightassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    roleid = models.CharField(max_length=255)
    rightid = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."rolerightassoc"'

class Roleroleassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    roleid = models.CharField(max_length=255)
    roleid_field = models.CharField(max_length=255)
    class Meta:
        db_table = u'"I2TM_APP"."roleroleassoc"'

class RptDistT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rpt_dist_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rpt_view_enu = models.BigIntegerField()
    distrate = models.BigIntegerField()
    distat_dtt = models.DateField()
    distemty_yn = models.CharField(max_length=1)
    nxt_dist_dtt = models.DateField()
    dist_to = models.CharField(max_length=1000, blank=True)
    dist_cc = models.CharField(max_length=1000, blank=True)
    role_typ = models.BigIntegerField(null=True, blank=True)
    rpt_inst_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rpt_dist_t"'

class RptInputParmT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rptparm_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rptparm_name = models.CharField(max_length=200)
    rptparm_desc = models.CharField(max_length=280)
    prmptusr_yn = models.CharField(max_length=1)
    prmpt_seq = models.BigIntegerField()
    cryprmpt_seq = models.BigIntegerField()
    rptparm_enu = models.BigIntegerField()
    rptparm_value = models.CharField(max_length=400)
    rpt_tplt_id = models.BigIntegerField(null=True, blank=True)
    rpt_inst_id = models.BigIntegerField(null=True, blank=True)
    rpt_dist_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rpt_input_parm_t"'

class RptInstT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rpt_inst_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rpt_inst_name = models.CharField(max_length=76)
    rpt_inst_desc = models.CharField(max_length=280)
    rpt_tplt_id = models.BigIntegerField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rpt_inst_t"'

class RptTpltT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rpt_tplt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rpt_tplt_name = models.CharField(max_length=200)
    rpt_tplt_desc = models.CharField(max_length=280)
    rpt_typ = models.BigIntegerField()
    rpt_dist_view = models.CharField(max_length=50, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    rpt_lvl_enu = models.BigIntegerField(null=True, blank=True)
    dmdrfrsh_yn = models.CharField(max_length=1)
    dmdrfrsh_cmd = models.CharField(max_length=100, blank=True)
    rpt_view_enu = models.BigIntegerField()
    supviewdmnd_yn = models.CharField(max_length=1)
    supviewdist_yn = models.CharField(max_length=1)
    dmstrdistemty_yn = models.CharField(max_length=1)
    dviewdistemty_yn = models.CharField(max_length=1)
    dft_distrate = models.BigIntegerField(null=True, blank=True)
    min_distrate = models.BigIntegerField(null=True, blank=True)
    dft_distat_dtt = models.DateField(null=True, blank=True)
    role_typ = models.BigIntegerField(null=True, blank=True)
    cryrptname = models.CharField(max_length=200)
    div_cd = models.CharField(max_length=16, blank=True)
    cry_file_typ_enu = models.BigIntegerField()
    supinst_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."rpt_tplt_t"'

class RspbCustOvrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rspb_cust_ovr_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    shpm_id = models.BigIntegerField(null=True, blank=True)
    chrg_cd = models.CharField(max_length=64)
    rspb_cust_enu = models.BigIntegerField()
    rspb_cust_cd = models.CharField(max_length=64, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rspb_cust_ovr_t"'

class RstcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rstc_id = models.BigIntegerField()
    rstc_desc = models.CharField(max_length=280)
    max_pces = models.BigIntegerField()
    min_pces = models.BigIntegerField()
    max_comp_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    min_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_comp_len = models.DecimalField(max_digits=9, decimal_places=3)
    max_comp_wdth = models.DecimalField(max_digits=9, decimal_places=3)
    max_comp_hght = models.DecimalField(max_digits=9, decimal_places=3)
    max_vol = models.DecimalField(max_digits=11, decimal_places=4)
    min_vol = models.DecimalField(max_digits=11, decimal_places=4)
    max_grth_size = models.DecimalField(max_digits=9, decimal_places=3)
    max_stop = models.BigIntegerField()
    max_skid = models.BigIntegerField()
    min_skid = models.BigIntegerField()
    max_shpm = models.BigIntegerField()
    min_shpm = models.BigIntegerField()
    max_load = models.BigIntegerField()
    min_load = models.BigIntegerField()
    max_shpm_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_shpm_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_otrt_pct = models.DecimalField(max_digits=6, decimal_places=2)
    max_otrt_dist = models.DecimalField(max_digits=6, decimal_places=1)
    max_dhed_dist = models.DecimalField(max_digits=6, decimal_places=1)
    max_dhed_pct = models.DecimalField(max_digits=5, decimal_places=2)
    max_dhedleg_dist = models.DecimalField(max_digits=6, decimal_places=1)
    opt_lck = models.BigIntegerField()
    m_ldunldstop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mexcswaitstp_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    m_tot_ldunld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mtotexcswait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_elpd_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    m_totwaitstp_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_tot_wait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    min_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_wait_stop_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_ret_to_orig_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_wait_btwn_lds_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_driving_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_on_duty_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_off_duty_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_loading_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_unloading_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_pmy_stop = models.DecimalField(max_digits=20, decimal_places=8)
    max_wknd_hldy_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_ely_wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_lat_wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_reps_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_uldd_trctr_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_uldd_trlr_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    class Meta:
        db_table = u'"I2TM_APP"."rstc_t"'

class RstcTpltT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rstc_cd = models.CharField(max_length=32)
    rstc_desc = models.CharField(max_length=280)
    max_pces = models.BigIntegerField()
    min_pces = models.BigIntegerField()
    max_comp_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    min_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_comp_len = models.DecimalField(max_digits=9, decimal_places=3)
    max_comp_wdth = models.DecimalField(max_digits=9, decimal_places=3)
    max_comp_hght = models.DecimalField(max_digits=9, decimal_places=3)
    max_vol = models.DecimalField(max_digits=11, decimal_places=4)
    min_vol = models.DecimalField(max_digits=11, decimal_places=4)
    max_grth_size = models.DecimalField(max_digits=9, decimal_places=3)
    max_stop = models.BigIntegerField()
    max_skid = models.BigIntegerField()
    min_skid = models.BigIntegerField()
    max_shpm = models.BigIntegerField()
    min_shpm = models.BigIntegerField()
    max_load = models.BigIntegerField()
    min_load = models.BigIntegerField()
    max_shpm_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_shpm_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_otrt_pct = models.DecimalField(max_digits=6, decimal_places=2)
    max_otrt_dist = models.DecimalField(max_digits=6, decimal_places=1)
    max_dhed_dist = models.DecimalField(max_digits=6, decimal_places=1)
    max_dhed_pct = models.DecimalField(max_digits=5, decimal_places=2)
    max_dhedleg_dist = models.DecimalField(max_digits=6, decimal_places=1)
    opt_lck = models.BigIntegerField()
    m_ldunldstop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mexcswaitstp_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    m_tot_ldunld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mtotexcswait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_elpd_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    m_totwaitstp_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_tot_wait_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_odr_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_wait_stop_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_ret_to_orig_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_wait_btwn_lds_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_driving_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_on_duty_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_off_duty_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_loading_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_unloading_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    max_pmy_stop = models.DecimalField(max_digits=20, decimal_places=8)
    max_wknd_hldy_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_ely_wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_lat_wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_reps_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_uldd_trctr_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_uldd_trlr_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    max_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rstc_tplt_t"'

class SalePersT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sale_pers_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    sale_pers_desc = models.CharField(max_length=280)
    agcy_cd_typ = models.BigIntegerField()
    sin_num = models.IntegerField()
    rate_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    paid_cnt = models.IntegerField(null=True, blank=True)
    num_prd_to_pay = models.IntegerField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    lang_typ = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."sale_pers_t"'

class SbsgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sbsg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    sbsg_cd = models.CharField(max_length=60)
    div_cd = models.CharField(max_length=16)
    sbsg_desc = models.CharField(max_length=280, blank=True)
    init_str = models.CharField(max_length=256, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    dest_appl_id = models.BigIntegerField()
    dll_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."sbsg_t"'

class SchgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    schg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    schg_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    amt_dlr = models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    chrg_id = models.BigIntegerField(null=True, blank=True)
    sr_tff_id = models.BigIntegerField(null=True, blank=True)
    rate_cd = models.CharField(max_length=132, blank=True)
    sr_chrg_id = models.BigIntegerField(null=True, blank=True)
    frht_cls_cd = models.CharField(max_length=16, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."schg_t"'

class Secaccessgroup(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_id = models.BigIntegerField()
    sec_name = models.CharField(max_length=123, blank=True)
    sec_combinator = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."secaccessgroup"'

class Secattrattrassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_id = models.BigIntegerField()
    sec_id_field = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."secattrattrassoc"'

class Secattrdict(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_attrtype = models.BigIntegerField()
    sec_definer = models.BigIntegerField()
    sec_family = models.BigIntegerField()
    sec_name = models.CharField(max_length=123, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."secattrdict"'

class Secattrrightassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_id = models.BigIntegerField()
    sec_id_field = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."secattrrightassoc"'

class Secgrouprightassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_id = models.BigIntegerField()
    sec_id_field = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."secgrouprightassoc"'

class Secoperationaccess(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_target = models.CharField(max_length=123)
    sec_operation = models.CharField(max_length=123)
    sec_groupid = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."secoperationaccess"'

class Secright(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_id = models.BigIntegerField()
    sec_name = models.CharField(max_length=123, blank=True)
    sec_definer = models.BigIntegerField(null=True, blank=True)
    sec_family = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."secright"'

class Securityattribute(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_id = models.BigIntegerField()
    sec_name = models.CharField(max_length=123, blank=True)
    sec_attrtype = models.BigIntegerField(null=True, blank=True)
    sec_definer = models.BigIntegerField(null=True, blank=True)
    sec_family = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."securityattribute"'

class Sequence(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sequencename = models.CharField(max_length=120)
    lastnumstring = models.CharField(max_length=46)
    lastnumber = models.BigIntegerField()
    currentlastnumber = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    numdigits = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."sequence"'

class SeqRngT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    seq_rng_id = models.BigIntegerField()
    rng_from = models.CharField(max_length=30)
    rng_to = models.CharField(max_length=30)
    next_value = models.CharField(max_length=30)
    status = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    seq_cd = models.CharField(max_length=32)
    class Meta:
        db_table = u'"I2TM_APP"."seq_rng_t"'

class SeqT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    seq_cd = models.CharField(max_length=32)
    seq_name = models.CharField(max_length=280)
    seq_len = models.BigIntegerField()
    cur_val = models.CharField(max_length=30, blank=True)
    opt_lck = models.BigIntegerField()
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."seq_t"'

class Server(models.Model):
    allow_sync = True
    connection_name = 'tm'
    serverid = models.CharField(max_length=24)
    name = models.CharField(max_length=64, blank=True)
    program = models.CharField(max_length=64, blank=True)
    arguments = models.CharField(max_length=255, blank=True)
    defaultloadmetric = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."server"'

class Serverdeployment(models.Model):
    allow_sync = True
    connection_name = 'tm'
    deplid = models.CharField(max_length=8)
    hostid = models.CharField(max_length=6, blank=True)
    serverid = models.CharField(max_length=24, blank=True)
    rootpath = models.CharField(max_length=160, blank=True)
    arguments = models.CharField(max_length=255, blank=True)
    replargsopt = models.BigIntegerField(null=True, blank=True)
    mininstances = models.BigIntegerField(null=True, blank=True)
    maxinstances = models.BigIntegerField(null=True, blank=True)
    showwindow = models.CharField(max_length=1, blank=True)
    loadmetric = models.BigIntegerField(null=True, blank=True)
    yellowthreshold = models.BigIntegerField(null=True, blank=True)
    redthreshold = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."serverdeployment"'

class Service(models.Model):
    allow_sync = True
    connection_name = 'tm'
    serviceid = models.CharField(max_length=24)
    name = models.CharField(max_length=64, blank=True)
    rootobjectclass = models.CharField(max_length=160, blank=True)
    logname = models.CharField(max_length=32, blank=True)
    type = models.BigIntegerField(null=True, blank=True)
    customconfigpanel = models.CharField(max_length=128, blank=True)
    parameters = models.CharField(max_length=255, blank=True)
    majversionmin = models.BigIntegerField(null=True, blank=True)
    minversionmin = models.BigIntegerField(null=True, blank=True)
    versiontextmin = models.CharField(max_length=32, blank=True)
    majversionmax = models.BigIntegerField(null=True, blank=True)
    minversionmax = models.BigIntegerField(null=True, blank=True)
    versiontextmax = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."service"'

class Serviceassoc(models.Model):
    allow_sync = True
    connection_name = 'tm'
    serverid = models.CharField(max_length=24)
    serviceid = models.CharField(max_length=24)
    class Meta:
        db_table = u'"I2TM_APP"."serviceassoc"'

class Serviceconfig(models.Model):
    allow_sync = True
    connection_name = 'tm'
    implkey = models.CharField(max_length=12)
    deplid = models.CharField(max_length=8, blank=True)
    serviceid = models.CharField(max_length=24, blank=True)
    role = models.BigIntegerField(null=True, blank=True)
    parameters = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."serviceconfig"'

class ShpmItmT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpm_itm_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    shpm_itm_num = models.CharField(max_length=120, blank=True)
    shpm_itm_xref = models.CharField(max_length=120, blank=True)
    itm_gl_cat = models.BigIntegerField(null=True, blank=True)
    excl_cat = models.BigIntegerField(null=True, blank=True)
    itm_desc = models.CharField(max_length=280)
    qnty = models.DecimalField(max_digits=9, decimal_places=2)
    nmnl_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    extd_nmnl_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    proratd_scld_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    extd_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=6, blank=True)
    extd_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    inpt_src_enu = models.BigIntegerField()
    seriallotctrl_enu = models.BigIntegerField()
    op_lst_non_emty_yn = models.CharField(max_length=1)
    cur_optlstat_id = models.BigIntegerField()
    shpm_id = models.BigIntegerField()
    comp_id = models.BigIntegerField()
    itm_num = models.CharField(max_length=120)
    itm_grp_cd = models.CharField(max_length=48, blank=True)
    frht_cls_cd = models.CharField(max_length=16)
    hazmat_cd = models.CharField(max_length=32, blank=True)
    nmfc_cd = models.CharField(max_length=120, blank=True)
    hmn_tff_cd = models.CharField(max_length=120, blank=True)
    orig_ctry_cd = models.CharField(max_length=16)
    num_of_rfrc_nums = models.BigIntegerField(null=True, blank=True)
    rfrc_nums = models.CharField(max_length=2000, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."shpm_itm_t"'

class ShpmSavCalcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpm_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    bs_sys_calc_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_dsc_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_chgd_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_fedl_tax_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_sta_tax_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_lcl_tax_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_adtn_chrg_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_pre_csld_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_sys_calc_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_dsc_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_chgd_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_fedl_tax_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_sta_tax_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_lcl_tax_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_adtn_chrg_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    actl_pre_csld_amt = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."shpm_sav_calc_t"'

class ShpmT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpm_id = models.BigIntegerField()
    shpm_num = models.CharField(max_length=120, blank=True)
    opt_lck = models.BigIntegerField()
    cur_optlstat_id = models.BigIntegerField()
    ret_optlstat_id = models.BigIntegerField()
    cur_fnclstat_id = models.BigIntegerField()
    ret_fnclstat_id = models.BigIntegerField()
    drct_frht_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    frm_pkup_dtt = models.DateField()
    to_pkup_dtt = models.DateField()
    frm_dlvy_dtt = models.DateField()
    to_dlvy_dtt = models.DateField()
    prpd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    cod_to_clct_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    csld_cls = models.CharField(max_length=120, blank=True)
    tot_mile_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    bs_dcld_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_odr_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    bs_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    bs_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    cdty_cd = models.CharField(max_length=48)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    ar_srvc_cd = models.CharField(max_length=16, blank=True)
    rate_cd = models.CharField(max_length=132, blank=True)
    lgst_grp_cd = models.CharField(max_length=16)
    sys_calc_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dsct_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    fedl_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    sta_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    loc_tax_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    adtn_chrg_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    precsld_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    tot_pce = models.BigIntegerField(null=True, blank=True)
    tot_skid = models.BigIntegerField(null=True, blank=True)
    rshp_rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    spot_rate_yn = models.CharField(max_length=1)
    ratg_vlid_yn = models.CharField(max_length=1)
    hold_yn = models.CharField(max_length=1)
    ar_srvc_cmtd_yn = models.CharField(max_length=1, blank=True)
    urgt_yn = models.CharField(max_length=1, blank=True)
    cfmg_usr_cd = models.CharField(max_length=40, blank=True)
    div_cd = models.CharField(max_length=16)
    cfmd_tms = models.BigIntegerField(null=True, blank=True)
    ratd_dtt = models.DateField(null=True, blank=True)
    echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    cncy_typ = models.BigIntegerField(null=True, blank=True)
    rutd_ori_zn_cd = models.CharField(max_length=64, blank=True)
    rutd_dest_zn_cd = models.CharField(max_length=64, blank=True)
    vchr_run_excp_id = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    rout_lane_id = models.BigIntegerField(null=True, blank=True)
    elpd_tm = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mrge_csld_cls_id = models.CharField(max_length=120, blank=True)
    mrge_csld_seq_num = models.BigIntegerField(null=True, blank=True)
    cfmg_by_ld_leg_id = models.BigIntegerField(null=True, blank=True)
    rqrd_eqmt_typ = models.CharField(max_length=20, blank=True)
    ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    bs_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    rate_cd_tff_id = models.BigIntegerField(null=True, blank=True)
    op_lst_non_emty_yn = models.CharField(max_length=1)
    odr_src_enu = models.BigIntegerField()
    rvnu_trpt_odr_yn = models.CharField(max_length=1)
    spfm_apt_rqrd_yn = models.CharField(max_length=1)
    spto_apt_rqrd_yn = models.CharField(max_length=1)
    frht_trms_enu = models.BigIntegerField()
    prf_ctr_typ = models.BigIntegerField()
    inpt_cncy = models.BigIntegerField()
    inpt_echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    inpt_src_enu = models.BigIntegerField()
    odr_val_rqrd_yn = models.CharField(max_length=1)
    dcl_val_rqrd_yn = models.CharField(max_length=1)
    ent_md_enu = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64)
    cust_ver_id = models.BigIntegerField()
    billto_cust_cd = models.CharField(max_length=64)
    billto_cust_ver_id = models.BigIntegerField()
    frm_ship_loc_enu = models.BigIntegerField()
    frm_shpg_loc_cd = models.CharField(max_length=64)
    frm_shpg_addr_id = models.BigIntegerField(null=True, blank=True)
    to_ship_loc_enu = models.BigIntegerField()
    to_shpg_loc_cd = models.CharField(max_length=64)
    to_shpg_addr_id = models.BigIntegerField(null=True, blank=True)
    to_ent_typ_cd = models.CharField(max_length=8)
    to_ent_ver_cd = models.CharField(max_length=40)
    cnse_grp_typ = models.BigIntegerField(null=True, blank=True)
    cust_srvc_rep_typ = models.BigIntegerField(null=True, blank=True)
    rate_ovrd_rsn_typ = models.BigIntegerField(null=True, blank=True)
    rate_ovrd_usr_cd = models.CharField(max_length=40, blank=True)
    rateovrd_dtt = models.DateField(null=True, blank=True)
    jrny_tplt_cd = models.CharField(max_length=32, blank=True)
    inpt_umsr_sys_enu = models.BigIntegerField(null=True, blank=True)
    inpt_umsr_wgt_enu = models.BigIntegerField(null=True, blank=True)
    inpt_umsr_len_enu = models.BigIntegerField(null=True, blank=True)
    inpt_umsr_dist_enu = models.BigIntegerField(null=True, blank=True)
    defr_ap_ratg_yn = models.CharField(max_length=1)
    defr_ar_ratg_yn = models.CharField(max_length=1)
    ar_srvc_mdy_yn = models.CharField(max_length=1, blank=True)
    pro_rate_comps_yn = models.CharField(max_length=1)
    min_odr_val_amt = models.DecimalField(max_digits=15, decimal_places=2)
    max_odr_val_amt = models.DecimalField(max_digits=15, decimal_places=2)
    mxd_ld_yn = models.CharField(max_length=1)
    max_shpm_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    max_shpm_vol = models.DecimalField(max_digits=11, decimal_places=4)
    sale_pers_cd = models.CharField(max_length=40, blank=True)
    chrg_bsd_carr_yn = models.CharField(max_length=1)
    plan_id = models.BigIntegerField(null=True, blank=True)
    prj_cd = models.CharField(max_length=48, blank=True)
    ap_srvc_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    carr_cmtd_yn = models.CharField(max_length=1)
    eqmt_typ_cmtd_yn = models.CharField(max_length=1)
    shpm_desc = models.CharField(max_length=280, blank=True)
    ap_srvc_cmtd_yn = models.CharField(max_length=1)
    ordr_grp_cd = models.CharField(max_length=16, blank=True)
    cdty_pick_seq_num = models.BigIntegerField(null=True, blank=True)
    vldt_itm = models.BigIntegerField(null=True, blank=True)
    itm_grp_cd = models.CharField(max_length=48, blank=True)
    comp_typ_grp_cd = models.CharField(max_length=48, blank=True)
    frm_ctry_cd = models.CharField(max_length=12, blank=True)
    frm_sta_cd = models.CharField(max_length=16, blank=True)
    frm_cty_name = models.CharField(max_length=280, blank=True)
    to_ctry_cd = models.CharField(max_length=12, blank=True)
    to_sta_cd = models.CharField(max_length=16, blank=True)
    to_cty_name = models.CharField(max_length=280, blank=True)
    frm_pstl_cd = models.CharField(max_length=48, blank=True)
    to_pstl_cd = models.CharField(max_length=48, blank=True)
    frm_name = models.CharField(max_length=280)
    to_name = models.CharField(max_length=280)
    full_chk_rqrd_yn = models.CharField(max_length=1)
    cfmg_by_shpmleg_id = models.BigIntegerField(null=True, blank=True)
    inco_ver_enu = models.BigIntegerField(null=True, blank=True)
    inco_terms_cd = models.CharField(max_length=12, blank=True)
    buyer_seller_enu = models.BigIntegerField(null=True, blank=True)
    prepaid_seg_only_yn = models.CharField(max_length=1)
    inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    inco_shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    btch_num = models.BigIntegerField(null=True, blank=True)
    frm_addr_id = models.BigIntegerField()
    to_addr_id = models.BigIntegerField()
    fmxbillrun_id = models.BigIntegerField(null=True, blank=True)
    fmxcollectrun_id = models.BigIntegerField(null=True, blank=True)
    fmxcollectrun_dtt = models.DateField(null=True, blank=True)
    display_status = models.BigIntegerField(null=True, blank=True)
    tender_count = models.BigIntegerField(null=True, blank=True)
    cfmg_count = models.BigIntegerField(null=True, blank=True)
    plan_count = models.BigIntegerField(null=True, blank=True)
    tdracpt_count = models.BigIntegerField(null=True, blank=True)
    tnst_md_enu = models.BigIntegerField(null=True, blank=True)
    tnst_md_cmtd_yn = models.CharField(max_length=1, blank=True)
    inelgb_sel_dltd_yn = models.CharField(max_length=1)
    cust_name = models.CharField(max_length=280)
    billto_cust_name = models.CharField(max_length=280)
    rfrc_num1 = models.CharField(max_length=120, blank=True)
    rfrc_num2 = models.CharField(max_length=120, blank=True)
    rfrc_num3 = models.CharField(max_length=120, blank=True)
    rfrc_num4 = models.CharField(max_length=120, blank=True)
    rfrc_num5 = models.CharField(max_length=120, blank=True)
    rfrc_num6 = models.CharField(max_length=120, blank=True)
    rfrc_num7 = models.CharField(max_length=120, blank=True)
    rfrc_num8 = models.CharField(max_length=120, blank=True)
    rfrc_num9 = models.CharField(max_length=120, blank=True)
    post_cnfn_upd_yn = models.CharField(max_length=1)
    lld_detl_rpt_yn = models.CharField(max_length=1)
    rfrc_num10 = models.CharField(max_length=120, blank=True)
    rfrc_num11 = models.CharField(max_length=120, blank=True)
    rfrc_num12 = models.CharField(max_length=120, blank=True)
    rfrc_num13 = models.CharField(max_length=120, blank=True)
    rfrc_num14 = models.CharField(max_length=120, blank=True)
    rfrc_num15 = models.CharField(max_length=120, blank=True)
    rfrc_num16 = models.CharField(max_length=120, blank=True)
    rfrc_num17 = models.CharField(max_length=120, blank=True)
    rfrc_num18 = models.CharField(max_length=120, blank=True)
    rfrc_num19 = models.CharField(max_length=120, blank=True)
    rfrc_num20 = models.CharField(max_length=120, blank=True)
    plng_yn = models.CharField(max_length=1)
    ret_shpm_yn = models.CharField(max_length=1)
    elgb_div_tsfr_yn = models.CharField(max_length=1)
    elgb_lgst_assn_yn = models.CharField(max_length=1)
    shft_seq = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_vbty_id = models.BigIntegerField(null=True, blank=True)
    tff_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    last_ratd_tff_id = models.BigIntegerField(null=True, blank=True)
    ar_csld_rfrc_num = models.CharField(max_length=120, blank=True)
    fncl_que_id = models.BigIntegerField(null=True, blank=True)
    rqrd_eqmt_typ_trctr = models.CharField(max_length=20, blank=True)
    eqmt_typ_trctr_cmtd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."shpm_t"'

class ShpmThghPntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpm_thgh_pnt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    thgh_pnt_typ_enu = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    carr_cmtd_yn = models.CharField(max_length=1)
    srvc_cmtd_yn = models.CharField(max_length=1)
    trpt_odr_cd = models.CharField(max_length=12, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dc_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    rqrd_eqmt_typ = models.CharField(max_length=20, blank=True)
    eqmt_typ_cmtd_yn = models.CharField(max_length=1)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    eqmt_typ_trctr_cmtd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."shpm_thgh_pnt_t"'

class SlctrlnumT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    slctrlnum_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    shpm_id = models.BigIntegerField()
    comp_id = models.BigIntegerField()
    shpm_itm_id = models.BigIntegerField()
    rfrc_nums = models.CharField(max_length=2000)
    class Meta:
        db_table = u'"I2TM_APP"."slctrlnum_t"'

class SrvcExcpCdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    sec_desc = models.CharField(max_length=280)
    itnt_clm_yn = models.CharField(max_length=1)
    obnd_api_file_yn = models.CharField(max_length=1, blank=True)
    rptg_flg_yn = models.CharField(max_length=1, blank=True)
    pnlz_stat_yn = models.CharField(max_length=1, blank=True)
    edi_sta_cd_typ = models.BigIntegerField(null=True, blank=True)
    edi_rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    actv_yn = models.CharField(max_length=1, blank=True)
    sec_rqrd_yn = models.CharField(max_length=1, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."srvc_excp_cd_t"'

class SrvrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    srvr_id = models.BigIntegerField()
    strt_dtt = models.DateField()
    ping_dtt = models.DateField()
    srvc_name = models.CharField(max_length=33)
    host_name = models.CharField(max_length=132)
    log_file = models.CharField(max_length=260, blank=True)
    pid = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    actv_srvr_id = models.BigIntegerField(null=True, blank=True)
    prty = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."srvr_t"'

class StatT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    stat_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    stat_typ_enu = models.BigIntegerField()
    stat_cd = models.CharField(max_length=48)
    stat_desc = models.CharField(max_length=280)
    sys_rqrd_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    gen_mvmt_yn = models.CharField(max_length=1)
    sec_rqrd_yn = models.CharField(max_length=1)
    stat_shrt_desc = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."stat_t"'

class StaT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_cd = models.CharField(max_length=16)
    ctry_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    sta_name = models.CharField(max_length=280)
    sys_prvd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."sta_t"'

class StopT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    stop_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    shpg_pnt_enu = models.BigIntegerField()
    shpm_pick = models.BigIntegerField()
    shpm_drop = models.BigIntegerField()
    frmprevstop_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ld_leg_id = models.BigIntegerField()
    pod_id = models.BigIntegerField(null=True, blank=True)
    shpg_addr_id = models.BigIntegerField(null=True, blank=True)
    addr_id = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64)
    hubrgn_zn_cd = models.CharField(max_length=64, blank=True)
    cmpd_arvl_dtt = models.DateField(null=True, blank=True)
    cmpd_dptr_dtt = models.DateField(null=True, blank=True)
    tnstprevstop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    pick_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    pick_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    pick_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pick_dcldval_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    pick_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    pick_tottare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    pick_tot_pce = models.BigIntegerField(null=True, blank=True)
    pick_tot_skid = models.BigIntegerField(null=True, blank=True)
    drop_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    drop_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    drop_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    drop_dcldval_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    drop_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    drop_tottare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    drop_tot_pce = models.BigIntegerField(null=True, blank=True)
    drop_tot_skid = models.BigIntegerField(null=True, blank=True)
    apt_id = models.BigIntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    pick_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    drop_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    pick_cfmd_yn = models.CharField(max_length=1)
    pick_cfmd_dtt = models.DateField(null=True, blank=True)
    pick_cfmd_usr_cd = models.CharField(max_length=40, blank=True)
    ldng_inst_id = models.BigIntegerField(null=True, blank=True)
    waiting_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    pick_arvl_rptd_dtt = models.DateField(null=True, blank=True)
    pick_dptr_rptd_dtt = models.DateField(null=True, blank=True)
    drop_arvl_rptd_dtt = models.DateField(null=True, blank=True)
    drop_dptr_rptd_dtt = models.DateField(null=True, blank=True)
    pick_arvl_sec_cd = models.CharField(max_length=64, blank=True)
    pick_dptr_sec_cd = models.CharField(max_length=64, blank=True)
    drop_arvl_sec_cd = models.CharField(max_length=64, blank=True)
    drop_dptr_sec_cd = models.CharField(max_length=64, blank=True)
    dock_schd_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    shpg_loc_name = models.CharField(max_length=280, blank=True)
    apt_rqrd_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    last_cmpd_arvl_dtt = models.DateField(null=True, blank=True)
    last_cmpd_dptr_dtt = models.DateField(null=True, blank=True)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    wknd_hldy_prev_stop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    strd_wknd_hldy_dtt = models.DateField(null=True, blank=True)
    end_wknd_hldy_dtt = models.DateField(null=True, blank=True)
    wknd_hldy_ortn_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."stop_t"'

class TaxAccT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tax_cd = models.CharField(max_length=32)
    div_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    gl_acrl_tax_exps = models.CharField(max_length=96, blank=True)
    gl_acrl_tax_lblt = models.CharField(max_length=96, blank=True)
    gl_tax_exps = models.CharField(max_length=96, blank=True)
    gl_tax_lblt = models.CharField(max_length=96, blank=True)
    gl_acrl_tax_rvnu = models.CharField(max_length=96, blank=True)
    gl_acrl_tax_asst = models.CharField(max_length=96, blank=True)
    gl_tax_rnvu = models.CharField(max_length=96, blank=True)
    gl_tax_asst = models.CharField(max_length=96, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tax_acc_t"'

class TaxCdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tax_cd = models.CharField(max_length=32)
    opt_lck = models.BigIntegerField()
    taxcd_desc = models.CharField(max_length=280)
    tax_lvl_enu = models.BigIntegerField()
    tax_type_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    arrel_enu = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tax_cd_t"'

class TaxRateT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tax_rate_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    tax_rate_pct = models.DecimalField(max_digits=5, decimal_places=2)
    min_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_val_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    tax_on_tax_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    efct_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    tax_cd = models.CharField(max_length=32)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    orig_zn_cd = models.CharField(max_length=64, blank=True)
    dest_zn_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tax_rate_t"'

class TaxRegNumT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tax_reg_num_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    tax_reg_num = models.CharField(max_length=120)
    tax_reg_ety_enu = models.BigIntegerField()
    tax_cd = models.CharField(max_length=32, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    lgst_sys_cd = models.CharField(max_length=8, blank=True)
    tax_zn_cd = models.CharField(max_length=64)
    class Meta:
        db_table = u'"I2TM_APP"."tax_reg_num_t"'

class TffChrgCmmnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    chrg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    mdy_rate_yn = models.CharField(max_length=1)
    unit_typ_enu = models.BigIntegerField()
    lkup_unit_enu = models.BigIntegerField()
    unit_divd_fctr = models.DecimalField(max_digits=11, decimal_places=6)
    rndg_rule_enu = models.BigIntegerField()
    chrg_by_rng_yn = models.CharField(max_length=1)
    spsd_rule_enu = models.BigIntegerField()
    lgst_free_yn = models.CharField(max_length=1)
    min_lgst_free = models.BigIntegerField()
    neft_unt_mul_enu = models.BigIntegerField(null=True, blank=True)
    neftunt_divd_enu = models.BigIntegerField(null=True, blank=True)
    neft_unt_add_enu = models.BigIntegerField(null=True, blank=True)
    neft_unt_sub_enu = models.BigIntegerField(null=True, blank=True)
    neft_amt_mul_enu = models.BigIntegerField(null=True, blank=True)
    neftamt_divd_enu = models.BigIntegerField(null=True, blank=True)
    neft_amt_add_enu = models.BigIntegerField(null=True, blank=True)
    neft_amt_sub_enu = models.BigIntegerField(null=True, blank=True)
    mlti_frgt_cls_yn = models.CharField(max_length=1, blank=True)
    extl_ratg_cd_typ = models.BigIntegerField(null=True, blank=True)
    mlticomp_lvl_enu = models.BigIntegerField()
    lkup_unitlvl_enu = models.BigIntegerField()
    umsr_dst_enu = models.BigIntegerField(null=True, blank=True)
    extl_rate_egin_ver_cd = models.CharField(max_length=60, blank=True)
    tfflkahd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    unit_divd_mlt_yn = models.CharField(max_length=1)
    apply_unit_divd_lk_up_yn = models.CharField(max_length=1)
    min_ratg_units_rate_sel = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_ratg_units_rate_sel = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_ratg_units_rate_appl = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_ratg_units_rate_appl = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rate_dt_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."tff_chrg_cmmn_t"'

class TffChrgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    chrg_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_desc = models.CharField(max_length=280)
    chrg_cond_yn = models.CharField(max_length=1)
    max_runt_aply = models.DecimalField(max_digits=15, decimal_places=4)
    min_runt_aply = models.DecimalField(max_digits=15, decimal_places=4)
    max_runt_slc = models.DecimalField(max_digits=15, decimal_places=4)
    min_runt_slc = models.DecimalField(max_digits=15, decimal_places=4)
    bs_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    dsc_min_yn = models.CharField(max_length=1)
    min_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    gl_typ = models.BigIntegerField(null=True, blank=True)
    pre_pchd_yn = models.CharField(max_length=1)
    tax_chrg_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    alert = models.CharField(max_length=1)
    max_min_pce_yn = models.CharField(max_length=1)
    fc_crs_rfrc_yn = models.CharField(max_length=1)
    amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    prty = models.BigIntegerField()
    spsd_chrg_id = models.BigIntegerField(null=True, blank=True)
    chrg_cd = models.CharField(max_length=64)
    rng_cd = models.CharField(max_length=16, blank=True)
    partof_chrg_id = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tff_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16)
    dim_wgt_fctr = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    min_dim_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    eqiv_ovsz_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_ovsz_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    chrg_backcust_yn = models.CharField(max_length=1, blank=True)
    gl_acc1 = models.CharField(max_length=120, blank=True)
    gl_acc2 = models.CharField(max_length=120, blank=True)
    gl_acc3 = models.CharField(max_length=120, blank=True)
    gl_acc4 = models.CharField(max_length=120, blank=True)
    er_egin_ver_cd = models.CharField(max_length=60, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    extlrateegin_ver = models.CharField(max_length=60, blank=True)
    dim_wgt_mlt_yn = models.CharField(max_length=1, blank=True)
    ldn_len_fctr = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    ldn_len_min_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    chrg_bsd_carr_yn = models.CharField(max_length=1)
    rspb_cust_enu = models.BigIntegerField(null=True, blank=True)
    rspb_cust_cd = models.CharField(max_length=64, blank=True)
    payable_carr_enu = models.BigIntegerField(null=True, blank=True)
    payable_carr_cd = models.CharField(max_length=64, blank=True)
    trip_lvl_rtng_yn = models.CharField(max_length=1)
    frht_cls_dfc_cd = models.CharField(max_length=16, blank=True)
    eqmt_crs_rfrc_yn = models.CharField(max_length=1)
    incl_frht_amt_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."tff_chrg_t"'

class TffSrvcEqmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tff_srvc_eqmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    eqmt_typ_cd = models.CharField(max_length=20)
    prty = models.BigIntegerField()
    crtd_dtt = models.DateField()
    tff_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    op_zn_cd = models.CharField(max_length=64, blank=True)
    rstc_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tff_srvc_eqmt_t"'

class TffSrvcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tff_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    tff_srvc_desc = models.CharField(max_length=280)
    cust_chrg_cd = models.CharField(max_length=96, blank=True)
    gl_typ = models.BigIntegerField()
    bs_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    min_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    max_chrg_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    tax_chrg_yn = models.CharField(max_length=1)
    rstd_use_yn = models.CharField(max_length=1)
    carrcsld_ctl_enu = models.BigIntegerField()
    csld_prcnlvl_enu = models.BigIntegerField()
    custcsld_ctl_enu = models.BigIntegerField()
    prnt_lbl_yn = models.CharField(max_length=1)
    prnt_bol_yn = models.CharField(max_length=1)
    bol_num_fmt = models.CharField(max_length=96, blank=True)
    bol_fmt_typ = models.BigIntegerField(null=True, blank=True)
    ship_lbl_fmt_typ = models.BigIntegerField(null=True, blank=True)
    mnft_fmt_typ = models.BigIntegerField(null=True, blank=True)
    invc_fmt_typ = models.BigIntegerField(null=True, blank=True)
    alw_stop_yn = models.CharField(max_length=1)
    team_drvr_yn = models.CharField(max_length=1)
    pre_pchd_yn = models.CharField(max_length=1)
    dsc_min_yn = models.CharField(max_length=1)
    alrt_apt_yn = models.CharField(max_length=1)
    alrt_carr_yn = models.CharField(max_length=1)
    assn_to_ld_yn = models.CharField(max_length=1)
    bol_num_ent_yn = models.CharField(max_length=1)
    rate_typ_enu = models.BigIntegerField(null=True, blank=True)
    amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    num_of_chrg = models.BigIntegerField()
    tnst_md_enu = models.BigIntegerField()
    auto_acpt_tdr_yn = models.CharField(max_length=1)
    lkup_unitlvl_enu = models.BigIntegerField(null=True, blank=True)
    tdr_rqrd_yn = models.CharField(max_length=1)
    comp_trkg_yn = models.CharField(max_length=1)
    rstc_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mnft_ld_grp_cd = models.CharField(max_length=16, blank=True)
    chrg_backcust_yn = models.CharField(max_length=1, blank=True)
    gl_acc1 = models.CharField(max_length=120, blank=True)
    gl_acc2 = models.CharField(max_length=120, blank=True)
    gl_acc3 = models.CharField(max_length=120, blank=True)
    gl_acc4 = models.CharField(max_length=120, blank=True)
    extl_ds_egin_ver = models.CharField(max_length=60, blank=True)
    dlvy_schd_cd = models.CharField(max_length=60, blank=True)
    schd_mthd_enu = models.BigIntegerField(null=True, blank=True)
    lane_perf_bs_enu = models.BigIntegerField(null=True, blank=True)
    tsusrdfd_srvcgrd = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    tssysgen_srvcgrd = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    usr_grd_hdlg_enu = models.BigIntegerField(null=True, blank=True)
    tsnum_of_trans = models.BigIntegerField(null=True, blank=True)
    trkg_lvl_enu = models.BigIntegerField(null=True, blank=True)
    auto_fax_tdr_yn = models.CharField(max_length=1)
    auto_emal_tdr_yn = models.CharField(max_length=1)
    auto_edi_tdr_yn = models.CharField(max_length=1)
    non_live_ld_yn = models.CharField(max_length=1)
    cea_actv_yn = models.CharField(max_length=1)
    cea_min_lds = models.BigIntegerField(null=True, blank=True)
    cea_max_lds = models.BigIntegerField(null=True, blank=True)
    cea_pnltymin_lds_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    cea_pnltymax_lds_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ctrc_carr_yn = models.CharField(max_length=1)
    cea_cstr_pct_yn = models.CharField(max_length=1)
    extlsrvctyp = models.DecimalField(max_digits=20, decimal_places=8)
    bus_hrs_ofst_id = models.BigIntegerField(null=True, blank=True)
    wknd_hldy_schd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    opmz_excl_yn = models.CharField(max_length=1)
    frht_auct_elgb_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."tff_srvc_t"'

class TffT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tff_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    tff_cd = models.CharField(max_length=64)
    tff_desc = models.CharField(max_length=280)
    tff_grp_typ = models.BigIntegerField()
    tff_attr_enu = models.BigIntegerField()
    tff_stat_enu = models.BigIntegerField()
    cnse_grp_typ = models.BigIntegerField()
    prj_cd = models.CharField(max_length=48, blank=True)
    efct_dt = models.DateField()
    expd_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    rout_prcn_enu = models.BigIntegerField()
    rstd_use_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    shrd_cntr = models.BigIntegerField()
    vlmt_yn = models.CharField(max_length=1)
    sav_yn = models.CharField(max_length=1)
    elst_efct_dt = models.DateField(null=True, blank=True)
    ltst_expd_dt = models.DateField(null=True, blank=True)
    rfrnlane_exst_yn = models.CharField(max_length=1)
    rfrnrate_exst_yn = models.CharField(max_length=1)
    rfrnschg_exst_yn = models.CharField(max_length=1)
    fi_pymt_md_enu = models.BigIntegerField()
    mstr_tff_id = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    rate_typ_enu = models.BigIntegerField()
    pymnt_cncy_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    minmax_chrg_calc_md_enu = models.BigIntegerField()
    srvc_grd_typ_mstr_tff_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tff_t"'

class ThghPntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    thgh_pnt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    seq_num = models.BigIntegerField()
    thgh_pnt_typ_enu = models.BigIntegerField()
    jrny_tplt_cd = models.CharField(max_length=32)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dc_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."thgh_pnt_t"'

class TmpSchg(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tff_id = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tmp_schg"'

class TolLvlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tol_lvl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    tol_green_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    tol_yellow_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    tol_red_hrs = models.DecimalField(max_digits=6, decimal_places=2)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    alrt_typ_cd = models.CharField(max_length=80)
    div_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    ship_loc_typ_enu = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tol_lvl_t"'

class ToEntTypT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    to_ent_typ_cd = models.CharField(max_length=8)
    opt_lck = models.BigIntegerField()
    to_typ_desc = models.CharField(max_length=280)
    cdt_chk_rqrd_yn = models.CharField(max_length=1)
    qte_yn = models.CharField(max_length=1)
    defr_ap_ratg_yn = models.CharField(max_length=1)
    rvnu_trpt_odr_yn = models.CharField(max_length=1)
    defr_ar_ratg_yn = models.CharField(max_length=1)
    ar_srvc_mdy_yn = models.CharField(max_length=1)
    trpt_odr_md_enu = models.BigIntegerField()
    odr_val_rqrd_yn = models.CharField(max_length=1)
    dcl_val_rqrd_yn = models.CharField(max_length=1)
    frht_trm_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    post_cnfn_upd_yn = models.CharField(max_length=1)
    lld_detl_rpt_yn = models.CharField(max_length=1)
    plng_yn = models.CharField(max_length=1)
    ret_shpm_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."to_ent_typ_t"'

class ToEntVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    to_ent_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    to_ent_ver_desc = models.CharField(max_length=280)
    statuponacpt_enu = models.BigIntegerField()
    csld_cls = models.CharField(max_length=120)
    cur_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    drct_frht_yn = models.CharField(max_length=1)
    acss_la_cnse_yn = models.CharField(max_length=1)
    acss_cust_yn = models.CharField(max_length=1)
    acss_prj_yn = models.CharField(max_length=1)
    pkup_dt_mdy_yn = models.CharField(max_length=1, blank=True)
    dlvy_dt_mdy_yn = models.CharField(max_length=1, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    to_ent_typ_cd = models.CharField(max_length=8, blank=True)
    prorate_comps_yn = models.CharField(max_length=1)
    crt_indv_comp_yn = models.CharField(max_length=1)
    rfrc_num_typ = models.BigIntegerField(null=True, blank=True)
    ordr_grp_cd = models.CharField(max_length=16, blank=True)
    frmpkuprule = models.BigIntegerField()
    topkuprule = models.BigIntegerField()
    frmdlvyrule = models.BigIntegerField()
    todlvyrule = models.BigIntegerField()
    frmpkupadj = models.DecimalField(max_digits=6, decimal_places=2)
    topkupadj = models.DecimalField(max_digits=6, decimal_places=2)
    frmdlvyadj = models.DecimalField(max_digits=6, decimal_places=2)
    todlvyadj = models.DecimalField(max_digits=6, decimal_places=2)
    elgb_div_tsfr_yn = models.CharField(max_length=1)
    elgb_lgst_assn_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."to_ent_ver_t"'

class TripT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    trip_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    elgb_cnts_mv_yn = models.CharField(max_length=1)
    carr_pymt_terms_enu = models.BigIntegerField()
    tot_ld_leg = models.BigIntegerField()
    num_cdty_cmtd_lds = models.BigIntegerField()
    cdty_cmtd_yn = models.CharField(max_length=1)
    num_carr_cmtd_lds = models.BigIntegerField()
    carr_cmtd_yn = models.CharField(max_length=1)
    srvc_cmtd_yn = models.CharField(max_length=1)
    num_srvc_cmtd_lds = models.BigIntegerField()
    ratg_vlid_yn = models.CharField(max_length=1)
    max_num_shpm = models.BigIntegerField()
    num_stop = models.BigIntegerField()
    crtd_dtt = models.DateField()
    lgst_grp_cd = models.CharField(max_length=16)
    cur_optlstat_id = models.BigIntegerField()
    cur_fnclstat_id = models.BigIntegerField()
    far_pnt_ld_id = models.BigIntegerField(null=True, blank=True)
    trip_strd_dtt = models.DateField(null=True, blank=True)
    cncy_typ = models.BigIntegerField(null=True, blank=True)
    echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    drct_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    outofrout_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    lnst_unldd_leg_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    ret_to_orig_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tot_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    in_tnst_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    frst_shpgpnt_enu = models.BigIntegerField(null=True, blank=True)
    frst_shpg_loc_cd = models.CharField(max_length=68, blank=True)
    frst_ctry_cd = models.CharField(max_length=16, blank=True)
    frst_sta_cd = models.CharField(max_length=20, blank=True)
    frst_cty_name = models.CharField(max_length=280, blank=True)
    frst_pstl_cd = models.CharField(max_length=52, blank=True)
    last_shpgpnt_enu = models.BigIntegerField(null=True, blank=True)
    last_shpg_loc_cd = models.CharField(max_length=68, blank=True)
    last_ctry_cd = models.CharField(max_length=16, blank=True)
    last_sta_cd = models.CharField(max_length=20, blank=True)
    last_cty_name = models.CharField(max_length=280, blank=True)
    last_pstl_cd = models.CharField(max_length=52, blank=True)
    elpd_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_wait_at_stop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_wait_btwn_lds_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    sus_rsn_enu = models.BigIntegerField(null=True, blank=True)
    far_pnt_stop_id = models.BigIntegerField(null=True, blank=True)
    tot_num_shpm = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    scdd_dtt = models.DateField(null=True, blank=True)
    rate_id = models.CharField(max_length=132, blank=True)
    rate_cd_tff_id = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    rfrc_num_qlfr_id = models.BigIntegerField(null=True, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    plan_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    vchr_run_excp_ap_id = models.BigIntegerField(null=True, blank=True)
    opmr_que_id = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    rout_lane_id = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField(null=True, blank=True)
    umsrwgt_enu = models.BigIntegerField(null=True, blank=True)
    umsrlen_enu = models.BigIntegerField(null=True, blank=True)
    umsrdist_enu = models.BigIntegerField(null=True, blank=True)
    max_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    max_tot_pce = models.BigIntegerField(null=True, blank=True)
    max_tot_skid = models.BigIntegerField(null=True, blank=True)
    max_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tot_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    tot_tot_pce = models.BigIntegerField(null=True, blank=True)
    tot_tot_skid = models.BigIntegerField(null=True, blank=True)
    tot_ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    cur_optl_stat_id = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    cur_fncl_stat_id = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rshp_rsn_cd_typ = models.BigIntegerField(null=True, blank=True)
    op_lst_non_emty_yn = models.CharField(max_length=1)
    driving_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tot_waiting_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    on_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    off_duty_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    frst_shpg_loc_name = models.CharField(max_length=280, blank=True)
    last_shpg_loc_name = models.CharField(max_length=280, blank=True)
    num_carr_soft_cmtd_lds = models.DecimalField(max_digits=20, decimal_places=8)
    num_srvc_soft_cmtd_lds = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    num_pmy_stop = models.DecimalField(max_digits=20, decimal_places=8)
    extl_egin_ver_cd = models.CharField(max_length=60, blank=True)
    last_ratd_tff_id = models.BigIntegerField(null=True, blank=True)
    wknd_hldy_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    schd_actv_yn = models.CharField(max_length=1)
    frst_addr_id = models.BigIntegerField(null=True, blank=True)
    last_addr_id = models.BigIntegerField(null=True, blank=True)
    csld_cls = models.CharField(max_length=120, blank=True)
    dmcl_cd_trctr = models.CharField(max_length=64, blank=True)
    dmcl_trctr_cmtd_yn = models.CharField(max_length=1)
    eqmt_trctr_cmtd_yn = models.CharField(max_length=1)
    eqmt_typ_cd_trctr = models.CharField(max_length=64, blank=True)
    num_dmcl_trctr_cmtd_lds = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    num_eqmt_trctr_cmtd_lds = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tot_reps_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    in_tnst_unldd_tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    trctr_unldd_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tdr_req_id = models.BigIntegerField(null=True, blank=True)
    wgt_dist_extd = models.DecimalField(null=True, max_digits=15, decimal_places=4, blank=True)
    trip_mrgn_yn = models.CharField(max_length=1)
    trip_mrgn_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    trip_mrgn_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    trip_mrgn_per_hour_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    tot_ld_cost_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."trip_t"'

class TrnsRunT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    run_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    num_enty_crtd = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    sent_to_tms = models.BigIntegerField()
    ap_trns_ver_cd = models.CharField(max_length=40, blank=True)
    ar_trns_ver_cd = models.CharField(max_length=40, blank=True)
    endd_dtt = models.DateField(null=True, blank=True)
    iniprtd_crtd_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    prly_prgd_yn = models.CharField(max_length=1)
    que_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=4000, blank=True)
    excl_carr_yn = models.CharField(max_length=1)
    cust_cd = models.CharField(max_length=4000, blank=True)
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."trns_run_t"'

class UpdtShpmRfrcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpm_id = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."updt_shpm_rfrc_t"'

class Useridentity(models.Model):
    allow_sync = True
    connection_name = 'tm'
    name = models.CharField(max_length=255)
    password = models.TextField(blank=True) # This field type is a guess.
    roleid = models.CharField(max_length=127, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."useridentity"'

class UsrGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_grp_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    usr_grp_desc = models.CharField(max_length=280)
    prof_id = models.BigIntegerField()
    usr_grp_typ_enu = models.BigIntegerField()
    cust_cd = models.CharField(max_length=64, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    mrkt_prof_yn = models.CharField(max_length=1)
    rstd_loc_yn = models.CharField(max_length=1)
    alw_cnfg_lst_yn = models.CharField(max_length=1, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    ebl_div_rstd_usr_yn = models.CharField(max_length=1)
    dock_cmtm_elgb_viol_yn = models.CharField(max_length=1)
    dock_cmtm_dtt_acss_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dock_cmtm_elgb_edit_unassd_yn = models.CharField(max_length=1)
    dock_cmtm_enfc_min_led_tm_yn = models.CharField(max_length=1)
    dock_cmtm_enfc_cutoff_tm_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."usr_grp_t"'

class UsrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    name = models.CharField(max_length=280)
    usr_athy_lvl_enu = models.BigIntegerField()
    lang_typ = models.BigIntegerField()
    csld_cls = models.CharField(max_length=120)
    addr_chk_enu = models.BigIntegerField()
    dis_rshp_yn = models.CharField(max_length=1)
    stat_enu = models.BigIntegerField()
    fbilladt_rqrd_yn = models.CharField(max_length=1)
    dft_prt_sel_enu = models.BigIntegerField()
    prof_id = models.BigIntegerField()
    usr_grp_cd = models.CharField(max_length=40)
    frht_cls_cd = models.CharField(max_length=16)
    to_ent_ver_cd = models.CharField(max_length=40)
    cdty_cd = models.CharField(max_length=48)
    lgst_grp_cd = models.CharField(max_length=16)
    div_cd = models.CharField(max_length=16)
    plan_id = models.BigIntegerField(null=True, blank=True)
    ld_bult_ver_cd = models.CharField(max_length=40, blank=True)
    acptinvlidaddr_yn = models.CharField(max_length=1)
    div_sel_enu = models.BigIntegerField()
    lgst_grp_sel_enu = models.BigIntegerField()
    mnft_vchr_ver_cd = models.CharField(max_length=40)
    apmiscvchrver_cd = models.CharField(max_length=40)
    ap_pschrgver_cd = models.CharField(max_length=40)
    apschdvchrver_cd = models.CharField(max_length=40, blank=True)
    apadhcvchrver_cd = models.CharField(max_length=40)
    adhoc_fb_ver_cd = models.CharField(max_length=40)
    schd_fb_ver_cd = models.CharField(max_length=40, blank=True)
    matpay_fb_ver_cd = models.CharField(max_length=40)
    edi_fb_ver_cd = models.CharField(max_length=10, blank=True)
    adhoc_ap_ver_cd = models.CharField(max_length=40)
    schd_ap_ver_cd = models.CharField(max_length=40, blank=True)
    apschdacrlver_cd = models.CharField(max_length=40, blank=True)
    apadhcacrlver_cd = models.CharField(max_length=40)
    armiscvchrver_cd = models.CharField(max_length=40)
    arpschrg_ver_cd = models.CharField(max_length=40)
    arschdvchrver_cd = models.CharField(max_length=40, blank=True)
    aradhcvchrver_cd = models.CharField(max_length=40)
    aradhcacrlver_cd = models.CharField(max_length=40)
    arschdacrlver_cd = models.CharField(max_length=40, blank=True)
    adhoc_invc_ver_cd = models.CharField(max_length=40)
    schd_invc_ver_cd = models.CharField(max_length=40, blank=True)
    adhoc_ar_ver_cd = models.CharField(max_length=40)
    schd_ar_ver_cd = models.CharField(max_length=40, blank=True)
    edi_invc_ver_cd = models.CharField(max_length=10, blank=True)
    mat_invc_ver_cd = models.CharField(max_length=40)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    frht_adt_vchr_verap_cd = models.CharField(max_length=40, blank=True)
    frht_adt_athz_enu = models.BigIntegerField()
    rstd_acss_yn = models.CharField(max_length=1)
    onescrn_fb_ent_yn = models.CharField(max_length=1)
    ctry_cd = models.CharField(max_length=16)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=256, blank=True)
    cust_srvcrep_typ = models.BigIntegerField(null=True, blank=True)
    umsrsys_enu = models.BigIntegerField()
    umsrwgt_enu = models.BigIntegerField()
    umsrlen_enu = models.BigIntegerField()
    umsrdist_enu = models.BigIntegerField()
    cncy_typ = models.BigIntegerField()
    evnt_notf_acss_yn = models.CharField(max_length=1, blank=True)
    dft_scrn_hght = models.DecimalField(max_digits=20, decimal_places=8)
    dft_scrn_wdth = models.DecimalField(max_digits=20, decimal_places=8)
    emal_apvl_alrt_yn = models.CharField(max_length=1)
    alw_cnfg_lst_chrt_yn = models.CharField(max_length=1)
    alw_srch_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."usr_t"'

class ValidLegsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    instance = models.DecimalField(max_digits=20, decimal_places=8)
    ld_leg_detl_id = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."valid_legs_t"'

class VarLdUnldHrsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    var_ld_unld_hrs_id = models.DecimalField(max_digits=20, decimal_places=8)
    opt_lck = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    var_hrs_cat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    ld_unit_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    unit_divd_fctr = models.DecimalField(max_digits=11, decimal_places=6)
    var_hrs_fctr = models.DecimalField(max_digits=9, decimal_places=5)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    dock_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."var_ld_unld_hrs_t"'

class VchrApT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    vchr_num = models.CharField(max_length=48)
    crtd_dtt = models.DateField()
    frhtchrg_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    eftv_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    hold_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    cur_stat_id = models.BigIntegerField()
    vchr_lvl_enu = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rfrc_num_typ_enu = models.BigIntegerField()
    rfrc_num = models.CharField(max_length=120)
    carr_cd = models.CharField(max_length=64)
    vchr_ver_cd = models.CharField(max_length=40)
    held_yn = models.CharField(max_length=1)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    frht_invc_id = models.BigIntegerField(null=True, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    ori_frht_invc_id = models.BigIntegerField(null=True, blank=True)
    init_vchr_num = models.CharField(max_length=48, blank=True)
    run_id = models.BigIntegerField(null=True, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    prf_ctr_typ = models.BigIntegerField(null=True, blank=True)
    ori_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    dest_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    ori_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dest_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    to_ent_typ_cd = models.CharField(max_length=8, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    vchr_typ = models.BigIntegerField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    carr_acc_num = models.CharField(max_length=136, blank=True)
    rtng_cncy_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rtng_echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    rtng_frhtchrg_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    carr_pymt_rblt_enu = models.BigIntegerField()
    bill_to_cust_cd = models.CharField(max_length=64, blank=True)
    frht_bill_num = models.CharField(max_length=120, blank=True)
    ori_frht_bill_num = models.CharField(max_length=120, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."vchr_ap_t"'

class VchrArT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    vchr_num = models.CharField(max_length=48)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    frhtchrg_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amt_dlr = models.DecimalField(max_digits=15, decimal_places=2)
    vchr_typ = models.BigIntegerField(null=True, blank=True)
    eftv_dt = models.DateField()
    cncy_typ = models.BigIntegerField()
    echg_rate = models.DecimalField(max_digits=11, decimal_places=6)
    hold_yn = models.CharField(max_length=1)
    held_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    cur_stat_id = models.BigIntegerField()
    mmo_id = models.BigIntegerField(null=True, blank=True)
    tff_id = models.BigIntegerField()
    vchr_lvl_enu = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    rfrc_num_typ_enu = models.BigIntegerField()
    rfrc_num = models.CharField(max_length=120)
    vchr_ver_cd = models.CharField(max_length=40)
    frht_invc_id = models.BigIntegerField(null=True, blank=True)
    cust_cd = models.CharField(max_length=64)
    bill_to_cust_cd = models.CharField(max_length=64)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    ori_frht_invc_id = models.BigIntegerField(null=True, blank=True)
    init_vchr_num = models.CharField(max_length=48, blank=True)
    run_id = models.BigIntegerField(null=True, blank=True)
    cost_ctr_typ = models.BigIntegerField(null=True, blank=True)
    prf_ctr_typ = models.BigIntegerField(null=True, blank=True)
    ori_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    dest_loc_typ_enu = models.BigIntegerField(null=True, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    ori_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dest_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    to_ent_typ_cd = models.CharField(max_length=8, blank=True)
    rtng_cncy_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rtng_echg_rate = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    rtng_frhtchrg_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    invc_num = models.CharField(max_length=120, blank=True)
    ori_invc_num = models.CharField(max_length=120, blank=True)
    shpm_num = models.CharField(max_length=120, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."vchr_ar_t"'

class VchrRunExcpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    vchr_run_excp_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    vchr_lvl_enu = models.BigIntegerField()
    rfrc_num_typ_enu = models.BigIntegerField()
    rfrc_num = models.CharField(max_length=120)
    rsn_cd_enu = models.BigIntegerField()
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    run_id = models.BigIntegerField()
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    classid = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    non_op_frht_id = models.BigIntegerField(null=True, blank=True)
    chrg_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."vchr_run_excp_t"'

class VchrRunT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    run_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    num_enty_crtd = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    ap_vchr_ver_cd = models.CharField(max_length=40, blank=True)
    ar_vchr_ver_cd = models.CharField(max_length=40, blank=True)
    endd_dtt = models.DateField(null=True, blank=True)
    iniprtd_crtd_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    prtdnotcrtd_dtt = models.DateField(null=True, blank=True)
    prly_prgd_yn = models.CharField(max_length=1)
    carr_cd = models.CharField(max_length=4000, blank=True)
    excl_carr_yn = models.CharField(max_length=1)
    cust_cd = models.CharField(max_length=4000, blank=True)
    excl_cust_yn = models.CharField(max_length=1)
    num_excp_crtd = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."vchr_run_t"'

class VchrVerApT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    vchr_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    vchr_ver_desc = models.CharField(max_length=280)
    vchr_typ = models.BigIntegerField(null=True, blank=True)
    cut_off_adj_day = models.BigIntegerField()
    shpm_rqrd_yn = models.CharField(max_length=1)
    crte_zerovchr_yn = models.CharField(max_length=1)
    prt_rgst_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=4000, blank=True)
    rvnu_trpt_odr_yn = models.CharField(max_length=1)
    strt_adj_day = models.BigIntegerField()
    excl_carr_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."vchr_ver_ap_t"'

class VchrVerArT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    vchr_ver_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    vchr_ver_desc = models.CharField(max_length=280)
    vchr_typ = models.BigIntegerField(null=True, blank=True)
    cut_off_adj_day = models.BigIntegerField()
    shpm_rqrd_yn = models.CharField(max_length=1)
    crte_zerovchr_yn = models.CharField(max_length=1)
    prt_rgst_yn = models.CharField(max_length=1)
    div_cd = models.CharField(max_length=16, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    rutgsucc_rqrd_yn = models.CharField(max_length=1, blank=True)
    cust_cd = models.CharField(max_length=4000, blank=True)
    strt_adj_day = models.BigIntegerField()
    excl_cust_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."vchr_ver_ar_t"'

class WgtByFrhtclsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    wgt_frht_cls_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    frht_cls_cd = models.CharField(max_length=16)
    elmt_id = models.BigIntegerField()
    tare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    scle_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."wgt_by_frhtcls_t"'

class ZnGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    zn_grp_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    zn_grp_desc = models.CharField(max_length=280)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    cls_id = models.BigIntegerField(null=True, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."zn_grp_t"'

class ZnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    zn_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    zn_desc = models.CharField(max_length=280)
    sta_cd = models.CharField(max_length=16, blank=True)
    shrd_cntr = models.BigIntegerField()
    ctry_cd = models.CharField(max_length=16)
    cls_id = models.BigIntegerField(null=True, blank=True)
    hubrgn_grp_cd = models.CharField(max_length=48, blank=True)
    csldarea_grp_cd = models.CharField(max_length=48, blank=True)
    glrgn_grp_cd = models.CharField(max_length=48, blank=True)
    tm_zn_ofst_typ = models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)
    daylgt_ofst_typ = models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)
    taxrgn_grp_cd = models.CharField(max_length=48, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    shrt_desc = models.CharField(max_length=48, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."zn_t"'

class LaneTpltT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    lane_tplt_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    lane_tplt_desc = models.CharField(max_length=280)
    div_cd = models.CharField(max_length=16)
    num_stop = models.BigIntegerField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."lane_tplt_t"'

class LaneThghPntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    lane_thgh_pnt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    lane_tplt_cd = models.CharField(max_length=48, blank=True)
    seq_num = models.BigIntegerField()
    shpg_loc_typ_enu = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."lane_thgh_pnt_t"'

class UsrGrpLocT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_grp_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    shpg_loc_typ_enu = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64)
    class Meta:
        db_table = u'"I2TM_APP"."usr_grp_loc_t"'

class EqmtCrsRfrcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    eqmt_crs_rfrc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    chrg_id = models.BigIntegerField()
    eqmt_typ_cd = models.CharField(max_length=20)
    ratd_as_eqmt_typ_cd = models.CharField(max_length=20)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."eqmt_crs_rfrc_t"'

class AutoTdrRspsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    auto_tdr_rsps_id = models.BigIntegerField()
    to_carrsrvc_seq_num = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    full_tdr_rsps_yn = models.CharField(max_length=1)
    avail_tm_pct = models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."auto_tdr_rsps_t"'

class EqmtCdtyExclT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    eqmt_cdty_excl_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    eqmt_typ_cd = models.CharField(max_length=20)
    cdty_cd = models.CharField(max_length=48)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    class Meta:
        db_table = u'"I2TM_APP"."eqmt_cdty_excl_t"'

class AlrtWachGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    alrt_wach_grp_cd = models.CharField(max_length=80)
    opt_lck = models.BigIntegerField()
    alrt_wach_grp_desc = models.CharField(max_length=280)
    dis_alrt_svrty_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    alrt_typ_cd = models.CharField(max_length=80, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    cust_cd = models.CharField(max_length=64, blank=True)
    ship_loc_typ_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."alrt_wach_grp_t"'

class AlrtWachGrpRcpnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    alrt_wach_grp_rcpn_id = models.DecimalField(max_digits=20, decimal_places=8)
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    alrt_wach_grp_cd = models.CharField(max_length=80)
    role_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    emal = models.CharField(max_length=100, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."alrt_wach_grp_rcpn_t"'

class DeleteShpmT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpm_id = models.BigIntegerField()
    shpm_num = models.CharField(max_length=120)
    cur_optlstat_id = models.DecimalField(max_digits=20, decimal_places=8)
    cur_fnclstat_id = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."delete_shpm_t"'

class ShpgLocEqmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpg_loc_eqmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64)
    shpgpnt_enu = models.BigIntegerField()
    eqmt_typ_cd = models.CharField(max_length=20)
    rstd_eqmt_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."shpg_loc_eqmt_t"'

class RateCalcVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_calc_ver_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    usr_cd = models.CharField(max_length=40)
    rate_calc_ver_name = models.CharField(max_length=280)
    itnr_fmt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    rtng_mthd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    opmz_cstrovrd_id = models.DecimalField(max_digits=20, decimal_places=8)
    drct_frht_yn = models.CharField(max_length=1)
    rate_qte_ebl_yn = models.CharField(max_length=1)
    desc_rqrd_yn = models.CharField(max_length=1)
    expd_dt_adj_day = models.DecimalField(max_digits=20, decimal_places=8)
    umsrsys_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrwgt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrlen_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrdist_enu = models.DecimalField(max_digits=20, decimal_places=8)
    cncy_typ = models.DecimalField(max_digits=20, decimal_places=8)
    rate_calc_md_enu = models.DecimalField(max_digits=20, decimal_places=8)
    stop_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    ori_loc_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    dest_loc_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    jrny_loc_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    frmpkuprule = models.DecimalField(max_digits=20, decimal_places=8)
    topkuprule = models.DecimalField(max_digits=20, decimal_places=8)
    frmdlvyrule = models.DecimalField(max_digits=20, decimal_places=8)
    todlvyrule = models.DecimalField(max_digits=20, decimal_places=8)
    frmpkupadj = models.DecimalField(max_digits=6, decimal_places=2)
    topkupadj = models.DecimalField(max_digits=6, decimal_places=2)
    frmdlvyadj = models.DecimalField(max_digits=6, decimal_places=2)
    todlvyadj = models.DecimalField(max_digits=6, decimal_places=2)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    cntr_typ_ebl_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."rate_calc_ver_t"'

class RateQteT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_qte_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    rate_qte_desc = models.CharField(max_length=280, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    crtd_dtt = models.DateField()
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    div_cd = models.CharField(max_length=16)
    lgst_grp_cd = models.CharField(max_length=16)
    rate_calc_md_enu = models.DecimalField(max_digits=20, decimal_places=8)
    cust_cd = models.CharField(max_length=64, blank=True)
    cust_name = models.CharField(max_length=280, blank=True)
    cdty_cd = models.CharField(max_length=48, blank=True)
    ar_srvc_cd = models.CharField(max_length=16, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    ap_srvc_cd = models.CharField(max_length=16, blank=True)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    pkup_dt = models.DateField(null=True, blank=True)
    frm_pkup_dtt = models.DateField(null=True, blank=True)
    to_pkup_dtt = models.DateField(null=True, blank=True)
    frm_dlvy_dtt = models.DateField(null=True, blank=True)
    to_dlvy_dtt = models.DateField(null=True, blank=True)
    scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    nmnl_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    tot_tare_wgt = models.DecimalField(null=True, max_digits=17, decimal_places=4, blank=True)
    vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    ldn_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    tot_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    tot_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    odr_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    dcld_val_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    num_shpm = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    umsrsys_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrwgt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrlen_enu = models.DecimalField(max_digits=20, decimal_places=8)
    umsrdist_enu = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_cncy_typ = models.DecimalField(max_digits=20, decimal_places=8)
    inpt_echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    ori_loc_typ_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ori_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ori_loc_name = models.CharField(max_length=280, blank=True)
    ori_ctry_cd = models.CharField(max_length=16, blank=True)
    ori_sta_cd = models.CharField(max_length=16, blank=True)
    ori_cty_name = models.CharField(max_length=280, blank=True)
    ori_pstl_cd = models.CharField(max_length=48, blank=True)
    ori_addr_id = models.BigIntegerField(null=True, blank=True)
    dest_loc_typ_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dest_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dest_loc_name = models.CharField(max_length=280, blank=True)
    dest_ctry_cd = models.CharField(max_length=16, blank=True)
    dest_sta_cd = models.CharField(max_length=16, blank=True)
    dest_cty_name = models.CharField(max_length=280, blank=True)
    dest_pstl_cd = models.CharField(max_length=48, blank=True)
    dest_addr_id = models.BigIntegerField(null=True, blank=True)
    cur_stat_id = models.DecimalField(max_digits=20, decimal_places=8)
    wbfctare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    wbfcscle_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    wbfcfrht_cls_cd = models.CharField(max_length=16, blank=True)
    wbfcnumfrhtcls = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ar_ratg_info_id = models.BigIntegerField(null=True, blank=True)
    ap_ratg_info_id = models.BigIntegerField(null=True, blank=True)
    num_stop = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    jrny_tplt_cd = models.CharField(max_length=32, blank=True)
    expd_dt = models.DateField(null=True, blank=True)
    jrny_ovrd_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    itnr_fmt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    rtng_mthd_enu = models.DecimalField(max_digits=20, decimal_places=8)
    opmz_cstrovrd_id = models.DecimalField(max_digits=20, decimal_places=8)
    drct_frht_yn = models.CharField(max_length=1)
    desc_rqrd_yn = models.CharField(max_length=1)
    ap_chgd_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    ap_cncy_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ap_echg_rate_prce = models.DecimalField(null=True, max_digits=11, decimal_places=6, blank=True)
    num_legs = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ori_rate_qte_id = models.DecimalField(max_digits=20, decimal_places=8)
    comp_typ_id = models.BigIntegerField(null=True, blank=True)
    comp_typ_grp_cd = models.CharField(max_length=64, blank=True)
    num_pmy_stop = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    eqmt_typ_cd_trctr = models.CharField(max_length=20, blank=True)
    dmcl_cd_trctr = models.CharField(max_length=64, blank=True)
    dmcl_cd_trlr = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rate_qte_t"'

class RateQteItnrT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_qte_itnr_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    rate_qte_id = models.BigIntegerField()
    seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    stop_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    shpg_pnt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ctry_cd = models.CharField(max_length=16, blank=True)
    sta_cd = models.CharField(max_length=16, blank=True)
    cty_name = models.CharField(max_length=280, blank=True)
    pstl_cd = models.CharField(max_length=48, blank=True)
    addr_id = models.BigIntegerField(null=True, blank=True)
    shpg_loc_name = models.CharField(max_length=280, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rate_qte_itnr_t"'

class RateQteSchdT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_qte_schd_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    rate_qte_id = models.BigIntegerField()
    leg_seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    stop_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    shpg_pnt_enu = models.DecimalField(max_digits=20, decimal_places=8)
    shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ctry_cd = models.CharField(max_length=16, blank=True)
    sta_cd = models.CharField(max_length=16, blank=True)
    cty_name = models.CharField(max_length=280, blank=True)
    pstl_cd = models.CharField(max_length=48, blank=True)
    addr_id = models.BigIntegerField(null=True, blank=True)
    shpg_loc_name = models.CharField(max_length=280, blank=True)
    frmprevstop_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    cmpd_arvl_dtt = models.DateField(null=True, blank=True)
    cmpd_dptr_dtt = models.DateField(null=True, blank=True)
    tnstprevstop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    waiting_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    loading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    unloading_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    wknd_hldy_prev_stop_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    strd_wknd_hldy_dtt = models.DateField(null=True, blank=True)
    end_wknd_hldy_dtt = models.DateField(null=True, blank=True)
    wknd_hldy_ortn_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."rate_qte_schd_t"'

class RateQteLegT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rate_qte_leg_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    rate_qte_id = models.BigIntegerField()
    leg_seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    ap_ratg_info_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rate_qte_leg_t"'

class RateQteWgtByFrhtclsT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    wgt_frht_cls_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    frht_cls_cd = models.CharField(max_length=16)
    rate_qte_id = models.BigIntegerField(null=True, blank=True)
    tare_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    scle_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rate_qte_wgt_by_frhtcls_t"'

class UsrPlanT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_plan_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    usr_cd = models.CharField(max_length=40)
    plan_id = models.BigIntegerField()
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    class Meta:
        db_table = u'"I2TM_APP"."usr_plan_t"'

class LdlegdetlCompT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ldlegdetl_comp_id = models.BigIntegerField()
    comp_elmt_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    opt_lck = models.BigIntegerField()
    cur_optlstat_id = models.BigIntegerField()
    ret_optlstat_id = models.BigIntegerField()
    cur_fnclstat_id = models.BigIntegerField()
    ret_fnclstat_id = models.BigIntegerField()
    pknglbl_prtd_tms = models.BigIntegerField()
    shpglbl_prtd_tms = models.BigIntegerField()
    custlbl_prtd_tms = models.BigIntegerField()
    pod_id = models.BigIntegerField(null=True, blank=True)
    vchrrunexcpap_id = models.BigIntegerField(null=True, blank=True)
    vchrrunexcpar_id = models.BigIntegerField(null=True, blank=True)
    rfrc_num = models.CharField(max_length=120, blank=True)
    rfrc_num_id = models.BigIntegerField(null=True, blank=True)
    op_lst_non_emty_yn = models.CharField(max_length=1)
    comp_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    qnty = models.IntegerField(null=True, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ldlegdetl_comp_t"'

class MdulT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mdul_id = models.BigIntegerField()
    usr_grp_cd = models.CharField(max_length=40)
    mdul_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    mdul_desc = models.CharField(max_length=280, blank=True)
    lbl = models.CharField(max_length=120)
    seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    empl_empl_elgb_yn = models.CharField(max_length=1)
    empl_gnrc_carr_yn = models.CharField(max_length=1)
    empl_spfc_carr_yn = models.CharField(max_length=1)
    empl_gnrc_cust_yn = models.CharField(max_length=1)
    empl_spfc_cust_yn = models.CharField(max_length=1)
    carr_elgb_yn = models.CharField(max_length=1)
    cust_elgb_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    ebl_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tag_cd = models.CharField(max_length=60, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    crtd_rls_enu = models.DecimalField(max_digits=20, decimal_places=8)
    mdul_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."mdul_t"'

class MdulCtntT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mdul_ctnt_id = models.BigIntegerField()
    usr_grp_cd = models.CharField(max_length=40)
    mdul_cd = models.CharField(max_length=64)
    mdul_ctnt_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    mdul_ctnt_desc = models.CharField(max_length=280, blank=True)
    lbl = models.CharField(max_length=120)
    seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    lvl_num = models.DecimalField(max_digits=20, decimal_places=8)
    ctnt_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    actv_yn = models.CharField(max_length=1)
    func_athz_enu = models.DecimalField(max_digits=20, decimal_places=8)
    parn_mdul_ctnt_cd = models.CharField(max_length=64, blank=True)
    func_cd = models.CharField(max_length=64, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    tag_cd = models.CharField(max_length=60, blank=True)
    parn_mdul_ctnt_id = models.BigIntegerField(null=True, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    mdul_id = models.BigIntegerField(null=True, blank=True)
    crtd_rls_enu = models.DecimalField(max_digits=20, decimal_places=8)
    is_dft_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."mdul_ctnt_t"'

class SupPurgeT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    num_id1 = models.BigIntegerField(null=True, blank=True)
    num_id2 = models.BigIntegerField(null=True, blank=True)
    num_id3 = models.BigIntegerField(null=True, blank=True)
    char_id1 = models.CharField(max_length=100, blank=True)
    char_id2 = models.CharField(max_length=100, blank=True)
    char_id3 = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."sup_purge_t"'

class ScrnElmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    scrn_elmt_cd = models.CharField(max_length=200)
    opt_lck = models.BigIntegerField()
    scrn_elmt_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    scrn_elmt_typ_enu = models.BigIntegerField()
    sys_prvd_yn = models.CharField(max_length=1)
    func_grp_enu = models.BigIntegerField()
    actv_yn = models.CharField(max_length=1)
    enty_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    crtd_rls_enu = models.DecimalField(max_digits=20, decimal_places=8)
    alw_emph_yn = models.CharField(max_length=1)
    scrn_cd = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."scrn_elmt_t"'

class ScrnElmtVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    scrn_elmt_ver_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    scrn_elmt_cd = models.CharField(max_length=200)
    src_mdul_ctnt_cd = models.CharField(max_length=64, blank=True)
    usr_grp_typ_enu = models.BigIntegerField()
    scrn_elmt_ver_desc = models.CharField(max_length=280)
    sys_prvd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    crtd_rls_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."scrn_elmt_ver_t"'

class ScrnElmtVerOprT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    scrn_elmt_ver_opr_id = models.BigIntegerField()
    scrn_elmt_cd = models.CharField(max_length=200)
    scrn_elmt_ver_opr_cd = models.CharField(max_length=120)
    opt_lck = models.BigIntegerField()
    scrn_elmt_ver_opr_desc = models.CharField(max_length=280)
    crtd_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    sel_rqrd_enu = models.BigIntegerField()
    url_parms = models.CharField(max_length=1024, blank=True)
    url = models.CharField(max_length=256, blank=True)
    avty_enu = models.BigIntegerField(null=True, blank=True)
    elgb_deactv_yn = models.CharField(max_length=1)
    scrn_elmt_ver_id = models.BigIntegerField()
    ebl_yn = models.CharField(max_length=1)
    alw_acss_ovrd_yn = models.CharField(max_length=1)
    crtd_rls_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."scrn_elmt_ver_opr_t"'

class UsrGrpVerOprT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_grp_ver_opr_id = models.BigIntegerField()
    scrn_elmt_ver_opr_id = models.BigIntegerField()
    scrn_elmt_cd = models.CharField(max_length=200)
    scrn_elmt_ver_opr_cd = models.CharField(max_length=120)
    opt_lck = models.BigIntegerField()
    usr_grp_cd = models.CharField(max_length=40)
    lbl = models.CharField(max_length=120, blank=True)
    tag_cd = models.CharField(max_length=60, blank=True)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    acss_mthd_enu = models.BigIntegerField()
    parn_id = models.BigIntegerField(null=True, blank=True)
    emph_yn = models.CharField(max_length=1)
    seq_num = models.BigIntegerField()
    actv_yn = models.CharField(max_length=1)
    sub_menu_hdr_yn = models.CharField(max_length=1)
    scrn_elmt_ver_id = models.BigIntegerField()
    show_vrfc_msg_yn = models.CharField(max_length=1)
    avty_enu = models.DecimalField(max_digits=20, decimal_places=8)
    ovrd_acss_yn = models.CharField(max_length=1)
    usr_grp_scrn_elmt_ver_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."usr_grp_ver_opr_t"'

class UsrGrpScrnElmtVerT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_grp_scrn_elmt_ver_id = models.BigIntegerField()
    scrn_elmt_cd = models.CharField(max_length=200)
    usr_grp_cd = models.CharField(max_length=40)
    opt_lck = models.BigIntegerField()
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    scrn_elmt_ver_id = models.BigIntegerField()
    lst_chrt_ctl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    expr_data_ctl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    srch_ctl_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."usr_grp_scrn_elmt_ver_t"'

class OpmrLock(models.Model):
    allow_sync = True
    connection_name = 'tm'
    opmr_lock_id = models.BigIntegerField(null=True, blank=True)
    opmr_grp_cd = models.CharField(max_length=64, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."opmr_lock"'

class TempRfrcNumVbty(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ent_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    rfrc_vbty_desc = models.CharField(max_length=280)
    rfrc_num_typ1 = models.BigIntegerField()
    rfrc_num_typ2 = models.BigIntegerField()
    rfrc_num_typ3 = models.BigIntegerField()
    rfrc_num_typ4 = models.BigIntegerField()
    rfrc_num_typ5 = models.BigIntegerField()
    rfrc_num_typ6 = models.BigIntegerField()
    rfrc_num_typ7 = models.BigIntegerField()
    rfrc_num_typ8 = models.BigIntegerField()
    rfrc_num_typ9 = models.BigIntegerField()
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    rfrc_num_typ10 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ11 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ12 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ13 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ14 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ15 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ16 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ17 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ18 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ19 = models.BigIntegerField(null=True, blank=True)
    rfrc_num_typ20 = models.BigIntegerField(null=True, blank=True)
    upd_proc_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."temp_rfrc_num_vbty"'

class RfrcNumVbtyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rfrc_num_vbty_id = models.BigIntegerField()
    ent_cd = models.CharField(max_length=48)
    opt_lck = models.BigIntegerField()
    rfrc_vbty_desc = models.CharField(max_length=280)
    rfrc_num_typ1 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ2 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ3 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ4 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ5 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ6 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ7 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ8 = models.DecimalField(max_digits=20, decimal_places=8)
    rfrc_num_typ9 = models.DecimalField(max_digits=20, decimal_places=8)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    rfrc_num_typ10 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ11 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ12 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ13 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ14 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ15 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ16 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ17 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ18 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ19 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    rfrc_num_typ20 = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    upd_proc_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."rfrc_num_vbty_t"'

class EvntCtlT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_enu = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evnt_desc = models.CharField(max_length=280)
    ebl_yn = models.CharField(max_length=1)
    usr_rsn_cd_alwd_yn = models.CharField(max_length=1)
    evnt_grp_cd = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_ctl_t"'

class AssEvntCtlStatT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ass_evnt_ctl_stat_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    evnt_enu = models.BigIntegerField()
    stat_id = models.BigIntegerField()
    ebl_yn = models.CharField(max_length=1)
    usr_rsn_cd_alwd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."ass_evnt_ctl_stat_t"'

class AssEvntStatSecT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_stat_sec_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    ass_evnt_ctl_stat_id = models.BigIntegerField()
    evnt_enu = models.BigIntegerField()
    stat_id = models.BigIntegerField()
    sec_cd = models.CharField(max_length=64)
    ebl_yn = models.CharField(max_length=1)
    sec_rqrd_yn = models.CharField(max_length=1)
    empl_usg_enu = models.DecimalField(max_digits=20, decimal_places=8)
    carr_usg_enu = models.DecimalField(max_digits=20, decimal_places=8)
    cust_usg_enu = models.DecimalField(max_digits=20, decimal_places=8)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ass_evnt_stat_sec_t"'

class PrtrAssnT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_cd = models.CharField(max_length=40)
    rpt_tplt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    prtr_name = models.CharField(max_length=128, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."prtr_assn_t"'

class AssQlfrRptT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rfrc_num_qlfr_id = models.BigIntegerField()
    rpt_tplt_id = models.BigIntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."ass_qlfr_rpt_t"'

class DmclVhclAvbltyT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    dmcl_vhcl_avblty_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dmcl_cd = models.CharField(max_length=64)
    vhcl_cd = models.CharField(max_length=96)
    eqmt_typ_cd = models.CharField(max_length=20)
    vhcl_cnt = models.BigIntegerField()
    reuse_yn = models.CharField(max_length=1)
    vhcl_availstrt_dtt = models.DateField(null=True, blank=True)
    vhcl_strtby_dtt = models.DateField(null=True, blank=True)
    pnlt_yn = models.CharField(max_length=1)
    pnltymax_vhcl_amt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    btwn_reuse_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    vhcl_endby_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dmcl_vhcl_avblty_t"'

class ShpgLocT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    shpg_loc_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    shpg_loc_cd = models.CharField(max_length=64)
    name = models.CharField(max_length=280)
    shpg_loc_typ_enu = models.BigIntegerField()
    addr_id = models.BigIntegerField()
    alw_dcon_yn = models.CharField(max_length=1, blank=True)
    apt_rqrd_yn = models.CharField(max_length=1)
    bdry_rule_enu = models.BigIntegerField(null=True, blank=True)
    bus_hrs_ofst_id = models.BigIntegerField()
    carr_cd = models.CharField(max_length=64, blank=True)
    cnse_grp_typ = models.BigIntegerField(null=True, blank=True)
    corp1_id = models.CharField(max_length=120, blank=True)
    corp2_id = models.CharField(max_length=120, blank=True)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    daylgt_ofst = models.DecimalField(max_digits=3, decimal_places=2)
    div_cd = models.CharField(max_length=16, blank=True)
    dock_cntr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    drpf_enu = models.BigIntegerField(null=True, blank=True)
    drtn_mmo_id = models.BigIntegerField(null=True, blank=True)
    extl_cd1 = models.CharField(max_length=120, blank=True)
    extl_cd2 = models.CharField(max_length=120, blank=True)
    fax_phn = models.CharField(max_length=23, blank=True)
    fixd_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    frst_pick_yn = models.CharField(max_length=1)
    full_srvc_yn = models.CharField(max_length=1, blank=True)
    gl_cat_typ = models.BigIntegerField(null=True, blank=True)
    glrgn_zn_cd = models.CharField(max_length=64)
    inco_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    inco_shpg_loc_enu = models.BigIntegerField(null=True, blank=True)
    lang_typ = models.BigIntegerField()
    last_drp_yn = models.CharField(max_length=1)
    lgst_grp_cd = models.CharField(max_length=16, blank=True)
    live_ld_typ_enu = models.BigIntegerField()
    loc_emal = models.CharField(max_length=100, blank=True)
    max_eqmt_hght = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_len = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_eqmt_wdth = models.DecimalField(null=True, max_digits=9, decimal_places=3, blank=True)
    max_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    max_shpm_vol = models.DecimalField(max_digits=11, decimal_places=4)
    max_shpm_wgt = models.DecimalField(max_digits=11, decimal_places=4)
    min_drp_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_ld_unld_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_lead_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    mmo_id = models.BigIntegerField(null=True, blank=True)
    near_tail_unld_rqrd_yn = models.CharField(max_length=1, blank=True)
    odr_grp_ebl_yn = models.CharField(max_length=1, blank=True)
    pkup_enu = models.BigIntegerField(null=True, blank=True)
    pmy_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    pmy_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    sde_dr_unld_rqrd_yn = models.CharField(max_length=1, blank=True)
    shpgloc_pick_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    stat_enu = models.BigIntegerField()
    stor_num = models.CharField(max_length=40, blank=True)
    tdr_rsps_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    tel1_phn = models.CharField(max_length=23, blank=True)
    tel2_phn = models.CharField(max_length=23, blank=True)
    tm_zn_ofst = models.DecimalField(max_digits=4, decimal_places=2)
    tsfr_oly_yn = models.CharField(max_length=1, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    url = models.CharField(max_length=256, blank=True)
    min_opmz_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_opmz_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_opmz_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_opmz_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    min_opmz_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_pce = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_skid = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_ibnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_ibnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_opmz_obnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    max_opmz_obnd_ld = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    min_pnlt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_pnlt_dlr = models.DecimalField(null=True, max_digits=15, decimal_places=2, blank=True)
    max_shpm_hold_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    min_shpm_hold_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    alw_emty_ld_yn = models.CharField(max_length=1)
    ld_tm_calc_enu = models.DecimalField(max_digits=20, decimal_places=8)
    live_unld_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    trlr_swap_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."shpg_loc_t"'

class CnfgVrblT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    cnfg_vrbl_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    cnfg_vrbl_desc = models.CharField(max_length=280)
    cnfg_vrbl_val = models.CharField(max_length=240, blank=True)
    func_yn = models.CharField(max_length=1)
    scrn_elmt_ver_opr_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    sys_prvd_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."cnfg_vrbl_t"'

class OpmrInsnGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    opmr_insn_grp_cd = models.CharField(max_length=64)
    opt_lck = models.BigIntegerField()
    opmr_insn_grp_desc = models.CharField(max_length=280, blank=True)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    is_dflt_yn = models.CharField(max_length=1)
    actv_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."opmr_insn_grp_t"'

class WorkflowCompT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    work_flow_comp_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField(null=True, blank=True)
    page_name = models.CharField(max_length=200, blank=True)
    action = models.CharField(max_length=100, blank=True)
    flow_typ = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ctrl_parm_clsname = models.CharField(max_length=200, blank=True)
    ctrl_parm_sesnname = models.CharField(max_length=100, blank=True)
    parm_rqrd_yn = models.CharField(max_length=1, blank=True)
    mlti_sel_yn = models.CharField(max_length=1, blank=True)
    rsltparm_sesn_name = models.CharField(max_length=100, blank=True)
    workflow_desc = models.CharField(max_length=200, blank=True)
    workflow_usg = models.CharField(max_length=4000, blank=True)
    enty_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    workflow_comp_cd = models.CharField(max_length=100)
    avty_enu = models.DecimalField(max_digits=20, decimal_places=8)
    parn_enty_typ_enu = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."workflow_comp_t"'

class AssEqmtT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    ass_eqmt_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    eqmt_typ_cd_trctr = models.CharField(max_length=20)
    eqmt_typ_cd_trlr = models.CharField(max_length=20)
    rstd_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."ass_eqmt_t"'

class RsrcT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    rsrc_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    carr_cd = models.CharField(max_length=64, blank=True)
    cmtd_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    cum_brk_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    cum_drvr_hrs = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    dest_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    dest_shpg_loc_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    div_cd = models.CharField(max_length=16)
    dmcl_addr_id = models.BigIntegerField(null=True, blank=True)
    dmcl_cd = models.CharField(max_length=64, blank=True)
    end_dtt = models.DateField(null=True, blank=True)
    eqmt_cat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    eqmt_typ_cd = models.CharField(max_length=20, blank=True)
    is_over_used_yn = models.CharField(max_length=1)
    lane_dest_zn_cd = models.CharField(max_length=64, blank=True)
    lane_dest_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    lane_div_cd = models.CharField(max_length=16, blank=True)
    lane_orig_zn_cd = models.CharField(max_length=64, blank=True)
    lane_orig_shpg_loc_cd = models.CharField(max_length=64, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    lgst_grp_cd = models.CharField(max_length=16)
    mvmt_id = models.BigIntegerField(null=True, blank=True)
    mvmt_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    mvmt_sgmt_strd_dtt = models.DateField(null=True, blank=True)
    ret_to_orig_dtt = models.DateField(null=True, blank=True)
    ret_to_orig_ovrd_yn = models.CharField(max_length=1)
    reuse_yn = models.CharField(max_length=1)
    rsrc_tp_id = models.CharField(max_length=280, blank=True)
    rsrc_typ_enu = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16, blank=True)
    strd_dtt = models.DateField(null=True, blank=True)
    tff_id = models.BigIntegerField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    vhcl_cd = models.CharField(max_length=96, blank=True)
    vhcl_seq_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rsrc_t"'

class VhclSeqT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    vhcl_seq_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    dmcl_cd = models.CharField(max_length=64)
    eqmt_typ_cd = models.CharField(max_length=20)
    carr_cd = models.CharField(max_length=64)
    eqmt_cat_enu = models.BigIntegerField()
    vhcl_cd = models.CharField(max_length=96)
    vhcl_seq_num = models.DecimalField(max_digits=20, decimal_places=8)
    actv_yn = models.CharField(max_length=1)
    class Meta:
        db_table = u'"I2TM_APP"."vhcl_seq_t"'

class UsrChrtCnfgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_chrt_cnfg_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    usr_cd = models.CharField(max_length=40)
    chrt_name = models.CharField(max_length=200)
    days_shft = models.IntegerField(null=True, blank=True)
    day_of_week_shft = models.BigIntegerField(null=True, blank=True)
    day_hrzn = models.IntegerField()
    hrs_itvl = models.IntegerField()
    class Meta:
        db_table = u'"I2TM_APP"."usr_chrt_cnfg_t"'

class TdrReqT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tdr_req_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    carr_cd = models.CharField(max_length=64)
    cdty_cd = models.CharField(max_length=48, blank=True)
    cplt_yn = models.CharField(max_length=1)
    crtd_dtt = models.DateField()
    crtd_usr_cd = models.CharField(max_length=40)
    div_cd = models.CharField(max_length=64)
    dmcl_cd_trctr = models.CharField(max_length=64, blank=True)
    dmcl_cd_trlr = models.CharField(max_length=64, blank=True)
    end_dtt = models.DateField(null=True, blank=True)
    eqmt_typ_trctr = models.CharField(max_length=20, blank=True)
    eqmt_typ_trlr = models.CharField(max_length=20, blank=True)
    frst_addr_id = models.BigIntegerField(null=True, blank=True)
    frst_ctry_cd = models.CharField(max_length=16, blank=True)
    frst_cty_name = models.CharField(max_length=280, blank=True)
    frst_pstl_cd = models.CharField(max_length=52, blank=True)
    frst_shpg_loc_cd = models.CharField(max_length=68, blank=True)
    frst_shpg_loc_name = models.CharField(max_length=280, blank=True)
    frst_shpgpnt_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    frst_sta_cd = models.CharField(max_length=20, blank=True)
    last_addr_id = models.BigIntegerField(null=True, blank=True)
    last_ctry_cd = models.CharField(max_length=16, blank=True)
    last_cty_name = models.CharField(max_length=280, blank=True)
    last_pstl_cd = models.CharField(max_length=52, blank=True)
    last_shpg_loc_cd = models.CharField(max_length=68, blank=True)
    last_shpg_loc_name = models.CharField(max_length=280, blank=True)
    last_shpgpnt_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    last_sta_cd = models.CharField(max_length=20, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    lgst_grp_cd = models.CharField(max_length=16)
    max_scld_wgt = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    max_vol = models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)
    req_stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    req_updt_sec_cd = models.CharField(max_length=64, blank=True)
    rsps_sec_cd = models.CharField(max_length=64, blank=True)
    srvc_cd = models.CharField(max_length=16, blank=True)
    strd_dtt = models.DateField(null=True, blank=True)
    tdr_acpd_by_name = models.CharField(max_length=280, blank=True)
    tdr_rsps_by_dtt = models.DateField(null=True, blank=True)
    tdr_updt_dtt = models.DateField(null=True, blank=True)
    tot_dist = models.DecimalField(null=True, max_digits=6, decimal_places=1, blank=True)
    tot_ld_leg = models.DecimalField(max_digits=20, decimal_places=8)
    trip_id = models.BigIntegerField(null=True, blank=True)
    updt_dtt = models.DateField(null=True, blank=True)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tdr_req_t"'

class TffSrvcCeaGrpT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    tff_srvc_cea_grp_id = models.BigIntegerField()
    tff_id = models.BigIntegerField()
    srvc_cd = models.CharField(max_length=16)
    opt_lck = models.BigIntegerField()
    cea_grp_typ = models.DecimalField(max_digits=20, decimal_places=8)
    crtd_dtt = models.DateField()
    updt_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40)
    updt_usr_cd = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."tff_srvc_cea_grp_t"'

class DomColT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    table_cd = models.CharField(max_length=30)
    column_cd = models.CharField(max_length=30)
    tab_cd = models.CharField(max_length=20, blank=True)
    col_desc = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."dom_col_t"'

class UsrScrnCnfgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_scrn_cnfg_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    usr_cd = models.CharField(max_length=40)
    scrn_name = models.CharField(max_length=200)
    pagng_yn = models.CharField(max_length=1)
    pag_sz = models.IntegerField()
    all_alwd_yn = models.CharField(max_length=1)
    fixd_scrn_cnfg_num = models.IntegerField()
    upd_tbl_yn = models.CharField(max_length=1)
    init_row_num = models.IntegerField()
    row_num = models.IntegerField()
    fixd_hdr_yn = models.CharField(max_length=1)
    func_grp_enu = models.BigIntegerField(null=True, blank=True)
    scrn_cnfg = models.TextField(blank=True)
    sort_cnfg = models.TextField(blank=True)
    num_row_rqrd_hdr = models.DecimalField(max_digits=20, decimal_places=8)
    class Meta:
        db_table = u'"I2TM_APP"."usr_scrn_cnfg_t"'

class UsrSrchCnfgT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    usr_srch_cnfg_id = models.BigIntegerField()
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    usr_cd = models.CharField(max_length=40)
    scrn_name = models.CharField(max_length=200)
    srch_name = models.CharField(max_length=70)
    srch_cls_vldt = models.CharField(max_length=100)
    func_grp_enu = models.BigIntegerField(null=True, blank=True)
    srch_tip = models.CharField(max_length=128, blank=True)
    srch_cnfg = models.TextField(blank=True)
    cur_srch_name = models.CharField(max_length=70, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."usr_srch_cnfg_t"'

class EvntCisDataT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    evnt_que_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    data = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'"I2TM_APP"."evnt_cis_data_t"'

class EvntQueT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    que_id = models.BigIntegerField()
    srvr_id = models.BigIntegerField(null=True, blank=True)
    que_dtt = models.DateField()
    strt_dtt = models.DateField()
    cpld_dtt = models.DateField(null=True, blank=True)
    prty = models.BigIntegerField()
    stat_enu = models.BigIntegerField()
    disd_yn = models.CharField(max_length=1)
    usr_cd = models.CharField(max_length=40, blank=True)
    msg_log_id = models.BigIntegerField(null=True, blank=True)
    opt_lck = models.BigIntegerField()
    data = models.TextField(blank=True) # This field type is a guess.
    updt_dtt = models.DateField(null=True, blank=True)
    evnt_notf_id = models.BigIntegerField()
    evnt_enu = models.BigIntegerField(null=True, blank=True)
    root_obj_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."evnt_que_t"'

class MmoT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    mmo_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    prtb_ctnt = models.CharField(max_length=2000, blank=True)
    non_prtb_ctnt = models.TextField(blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."mmo_t"'

class QueMsgLogT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    msg_log_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    msg = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'"I2TM_APP"."que_msg_log_t"'

class RptPrtQueT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    que_id = models.BigIntegerField()
    srvr_id = models.BigIntegerField(null=True, blank=True)
    que_dtt = models.DateField()
    strt_dtt = models.DateField()
    cpld_dtt = models.DateField(null=True, blank=True)
    prty = models.DecimalField(max_digits=20, decimal_places=8)
    stat_enu = models.DecimalField(max_digits=20, decimal_places=8)
    disd_yn = models.CharField(max_length=1)
    usr_cd = models.CharField(max_length=44, blank=True)
    msg_log_id = models.BigIntegerField(null=True, blank=True)
    opt_lck = models.DecimalField(max_digits=20, decimal_places=8)
    rpt_name = models.CharField(max_length=320)
    copies = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dvr_name = models.CharField(max_length=320, blank=True)
    prtr_name = models.CharField(max_length=128, blank=True)
    port_name = models.CharField(max_length=320, blank=True)
    dev_name = models.CharField(max_length=80, blank=True)
    spec_ver = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dvr_ver = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    sz = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dvr_extr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    fields = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    orntn = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    papr_size = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    papr_len = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    papr_wdth = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    scle = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dev_cpy = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dft_src = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    prt_qlty = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    color = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    duplex = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    yrsltn = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ttopt = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    collate = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    form_name = models.CharField(max_length=80, blank=True)
    unused_pad = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    bits_per_pel = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    pels_wdth = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    pels_hght = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dis_flgs = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    dis_frq = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    parms = models.CharField(max_length=1200, blank=True)
    rpt_ctl = models.TextField(blank=True)
    div_cd = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."rpt_prt_que_t"'

class UsrProfT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    prof_id = models.BigIntegerField()
    opt_lck = models.BigIntegerField()
    usr_prof_fetr = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'"I2TM_APP"."usr_prof_t"'

class Secidentity(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sec_attrid = models.DecimalField(max_digits=20, decimal_places=8)
    sec_password = models.TextField(blank=True) # This field type is a guess.
    dateentered = models.DateField(null=True, blank=True)
    sec_pswd_expr = models.DateField(null=True, blank=True)
    sec_pswd_ntvl = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    sec_cred_expr = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."secidentity"'

class GlobalTempT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    num_id = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    char_id = models.CharField(max_length=200, blank=True)
    row_num = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."global_temp_t"'

class GlobalTempAparT(models.Model):
    allow_sync = True
    connection_name = 'tm'
    sta_tnst_id = models.BigIntegerField(null=True, blank=True)
    sec_cd = models.CharField(max_length=16, blank=True)
    evnt_enu = models.DecimalField(null=True, max_digits=20, decimal_places=8, blank=True)
    ld_leg_id = models.BigIntegerField(null=True, blank=True)
    alt_ld_leg_id = models.BigIntegerField(null=True, blank=True)
    shpm_id = models.BigIntegerField(null=True, blank=True)
    ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    alt_ld_leg_detl_id = models.BigIntegerField(null=True, blank=True)
    trip_id = models.BigIntegerField(null=True, blank=True)
    alt_trip_id = models.BigIntegerField(null=True, blank=True)
    ldlegdetl_comp_id = models.BigIntegerField(null=True, blank=True)
    carr_cd = models.CharField(max_length=64, blank=True)
    cur_loc_cty_name = models.CharField(max_length=280, blank=True)
    cur_loc_sta_cd = models.CharField(max_length=16, blank=True)
    cur_loc_ctry_cd = models.CharField(max_length=12, blank=True)
    rptd_dtt = models.DateField(null=True, blank=True)
    etmd1_dtt = models.DateField(null=True, blank=True)
    etmd2_dtt = models.DateField(null=True, blank=True)
    crtd_usr_cd = models.CharField(max_length=40, blank=True)
    sta_tnst_dtt = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'"I2TM_APP"."global_temp_apar_t"'

