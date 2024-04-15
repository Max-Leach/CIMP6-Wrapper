import cdsapi

c = cdsapi.Client()
years = ['{}'.format(i) for i in range(2015, 2101)] # future years
months = ['{}'.format(i) for i in range(1, 13)]

variables = ['surface_temperature']
experiments = ['ssp5_8_5']

models = ['access_cm2']

# all models
"""

models = ['access_cm2', 'access_esm1_5', 'awi_cm_1_1_mr', 'awi_esm_1_1_lr', 'bcc_csm2_mr', 'bcc_esm1', 'cams_csm1_0', 'canesm5', 'canesm5_canoe', 'cesm2',
          'cesm2_fv2', 'cesm2_waccm', 'cesm2_waccm_fv2','ciesm', 'cmcc_cm2_hr4', 'cmcc_cm2_sr5', 'cmcc_esm2', 'cnrm_cm6_1', 'cnrm_cm6_1_hr', 'cnrm_esm2_1',
          'e3sm_1_0', 'e3sm_1_1', 'e3sm_1_1_eca', 'ec_earth3', 'ec_earth3_aerchem', 'ec_earth3_cc', 'ec_earth3_veg', 'ec_earth3_veg_lr',
          'fgoals_f3_l', 'fgoals_g3', 'fio_esm_2_0', 'gfdl_esm4', 'giss_e2_1_g', 'giss_e2_1_h', 'hadgem3_gc31_ll', 'hadgem3_gc31_mm', 'iitm_esm',
          'inm_cm4_8', 'inm_cm5_0', 'ipsl_cm5a2_inca','ipsl_cm6a_lr', 'kace_1_0_g','kiost_esm', 'mcm_ua_1_0', 'miroc6', 'miroc_es2h', 'miroc_es2l',
          'mpi_esm_1_2_ham', 'mpi_esm1_2_hr', 'mpi_esm1_2_lr', 'mri_esm2_0', 'nesm3', 'norcpm1', 'noresm2_lm', 'noresm2_mm', 'sam0_unicon', 'taiesm1', 'ukesm1_0_ll']
"""

#variables = ['surface_temperature', 'air_temperature', ...]
#experiments = ['ssp5_8_5', 'ssp1_2_6', ...]


for experiment in experiments:
    for model in models:
        for variable in variables:
            try:
                c.retrieve(
                    'projections-cmip6',
                    {
                        'temporal_resolution': 'monthly',
                        'experiment': experiment,
                        'variable': variable,
                        'model': model,
                        'year': years,
                        'month': months,
                        'format': 'zip',
                    },
                    '{}.zip'.format(model + '_model_' + experiment + '_' + variable))
            except:
                print("Invalid parameters: ", model, experiment, variable, " Starting year: ", years[0], " Ending year: ", years[-1])
