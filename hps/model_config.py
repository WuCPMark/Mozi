from jobman import DD, flatten

model_config = DD({

        'AE_Testing' : DD({

            'model' : DD({
                    'rand_seed'             : None
                    }), # end mlp

            'log' : DD({
                    'experiment_name'         : 'AE_Testing_Mnist',
                    'description'           : '',
                    'save_outputs'          : True,
                    'save_hyperparams'      : True,
                    'save_model'            : True,
                    'save_to_database_name' : 'Database_Name.db'
                    }), # end log


            'learning_rule' : DD({
                    'max_col_norm'          : (1, 10, 50),
                    'learning_rate'         : (1e-4, 1e-3, 1e-2, 1e-1, 0.9),
                    'momentum'              : (1e-2, 1e-1, 0.5, 0.9),
                    'momentum_type'         : 'normal',
                    'L1_lambda'             : None,
                    'L2_lambda'             : None,
                    'cost'                  : 'mse',
                    'stopping_criteria'     : DD({
                                                'max_epoch'         : 100,
                                                'epoch_look_back'   : 10,
                                                'cost'              : 'mse',
                                                'percent_decrease'  : 0.005
                                                }) # end stopping_criteria
                    }), # end learning_rule

            'dataset' : DD({

                    'type'                  : 'Mnist_Blocks',
                    'train_valid_test_ratio': [8, 1, 1],
                    'preprocessor'          : None,
                    'feature_size'          : 784,
        #                     'preprocessor'          : 'Scale',
                    # 'preprocessor'          : 'GCN',
                            # 'preprocessor'          : 'LogGCN',
        #                     'preprocessor'          : 'Standardize',
                    'batch_size'            : 100,
                    'num_batches'           : None,
                    'iter_class'            : 'SequentialSubsetIterator',
                    'rng'                   : None
                    }), # end dataset

            #============================[ Layers ]===========================#
            'hidden1' : DD({
                    'name'                  : 'hidden1',
                    'type'                  : 'RELU',
                    'dim'                   : 500,
                    'dropout_below'         : (0.05, 0.1, 0.15, 0.2)
                    }), # end hidden_layer

            'h1_mirror' : DD({
                    'name'                  : 'h1_mirror',
                    'type'                  : 'Sigmoid',
                    # 'dim'                   : 2049, # dim = input.dim
                    'dropout_below'         : None
                    }) # end output_layer
            }), # end autoencoder


        #############################[Laura]##############################
        ##################################################################

        'Laura' : DD({

            'model' : DD({
                    'rand_seed'             : None
                    }), # end mlp

            'log' : DD({
                    # 'experiment_name'       : 'AE0829_Blocks_2049_500_tanh_gpu',
                    # 'experiment_name'       : 'AE0829_Warp_Standardize_GCN_Blocks_2049_500_tanh_gpu',

                    # 'experiment_name'       : 'AE0829_Standardize_GCN_Blocks_2049_500_tanh_gpu',
                    'experiment_name'       : 'AE0901_Warp_Blocks_500_180_tanh_gpu_clean',
                    'description'           : '',
                    'save_outputs'          : True,
                    'save_hyperparams'      : True,
                    'save_model'            : True,
                    'save_to_database_name' : 'Database_Name.db'
                    }), # end log


            'learning_rule' : DD({
                    'max_col_norm'          : (1, 10, 50),
                    'learning_rate'         : (1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.5),
                    # 'learning_rate'         : ((1e-5, 9e-1), float),
                    # 'learning_rate'         : 0.01,
                    'momentum'              : (1e-3, 1e-2, 1e-1, 0.5, 0.9),
                    # 'momentum'              : 0.05,
                    'momentum_type'         : 'normal',
                    'L1_lambda'             : None,
                    'L2_lambda'             : None,
                    'cost'                  : 'mse',
                    'stopping_criteria'     : DD({
                                                'max_epoch'         : 100,
                                                'epoch_look_back'   : 10,
                                                'cost'              : 'mse',
                                                'percent_decrease'  : 0.05
                                                }) # end stopping_criteria
                    }), # end learning_rule

            #===========================[ Dataset ]===========================#
            'dataset' : DD({
                    # 'type'                  : 'Laura_Warp_Blocks_500_Tanh',
                    # 'type'                  : 'Laura_Cut_Warp_Blocks_300',
                    # 'type'                  : 'Laura_Blocks_500',
                    # 'type'                  : 'Laura_Blocks',
                    'type'                  : 'Laura_Warp_Blocks',
                    # 'type'                  : 'Laura_Warp_Standardize_Blocks',
                    # 'type'                  : 'Laura_Standardize_Blocks',

                    'feature_size'          : 2049,
                    'train_valid_test_ratio': [8, 1, 1],

                    # 'preprocessor'          : None,
                    # 'preprocessor'          : 'Scale',
                    'preprocessor'          : 'GCN',
                    # 'preprocessor'          : 'LogGCN',
                    # 'preprocessor'          : 'Standardize',

                    'batch_size'            : (50, 100, 150, 200),
                    'num_batches'           : None,
                    'iter_class'            : 'SequentialSubsetIterator',
                    'rng'                   : None
                    }), # end dataset

            # #============================[ Layers ]===========================#
            'num_layers' : 1,

            'hidden1' : DD({
                    'name'                  : 'hidden1',
                    'type'                  : 'Tanh',
                    'dim'                   : 180,
                    # 'dropout_below'         : (0.1, 0.2, 0.3, 0.4, 0.5)
                    'dropout_below'         : None
                    }), # end hidden_layer

            'hidden2' : DD({
                    'name'                  : 'hidden2',
                    'type'                  : 'RELU',
                    'dim'                   : 100,
                    'dropout_below'         : None
                    }), # end hidden_layer

            'h2_mirror' : DD({
                    'name'                  : 'h2_mirror',
                    'type'                  : 'RELU',
                    # 'dim'                   : 2049, # dim = input.dim
                    'dropout_below'         : None
                    }), # end output_layer

            'h1_mirror' : DD({
                    'name'                  : 'h1_mirror',
                    'type'                  : 'Sigmoid',
                    # 'dim'                   : 2049, # dim = input.dim
                    'dropout_below'         : None
                    }) # end output_layer


            #========================[ 2-4-6 Layers ]=========================#
            # 'num_layers' : 1,
            #
            # 'hidden1' : DD({
            #         'name'                  : 'hidden1',
            #         'type'                  : 'Tanh',
            #         'dim'                   : 64,
            #         'dropout_below'         : (0.05, 0.1, 0.15, 0.2)
            #         # 'dropout_below'         : 0.1
            #         }), # end hidden_layer
            #
            #
            # 'h1_mirror' : DD({
            #         'name'                  : 'h1_mirror',
            #         'type'                  : 'RELU',
            #         # 'dim'                   : 2049, # dim = input.dim
            #         'dropout_below'         : None
            #         }) # end output_layer

            #========================[ 1-3-5 Layers ]=========================#
            # 'num_layers' : 1,
            #
            # 'hidden1' : DD({
            #         'name'                  : 'hidden1',
            #         'type'                  : 'RELU',
            #         'dim'                   : 150,
            #         'dropout_below'         : (0.1, 0.2, 0.3, 0.4, 0.5)
            #         # 'dropout_below'         : 0.1
            #         }), # end hidden_layer
            #
            #
            # 'h1_mirror' : DD({
            #         'name'                  : 'h1_mirror',
            #         'type'                  : 'RELU',
            #         # 'dim'                   : 2049, # dim = input.dim
            #         'dropout_below'         : None
            #         }) # end output_layer



            }), # end autoencoder

    ########################[Laura_Two_Layers]########################
    ##################################################################

    'Laura_Two_Layers' : DD({
        'model' : DD({
                'rand_seed'             : None
                }), # end mlp

        'log' : DD({
                # 'experiment_name'         : 'AE0730_2layers_finetune_Laura_Blocks',
                'experiment_name'       : 'AE0906_Warp_Blocks_2layers_finetune_2049_180_gpu',

                'description'           : '',
                'save_outputs'          : True,
                'save_hyperparams'      : True,
                'save_model'            : True,
                'save_to_database_name' : 'Database_Name.db'
                }), # end log


        'learning_rule' : DD({
                'max_col_norm'          : (1, 10, 50),
                'learning_rate'         : (1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.5),
                # 'learning_rate'         : ((1e-5, 9e-1), float),
                # 'learning_rate'         : 0.01,
                'momentum'              : (1e-3, 1e-2, 1e-1, 0.5, 0.9),
                # 'momentum'              : 0.05,
                'momentum_type'         : 'normal',
                'L1_lambda'             : None,
                'L2_lambda'             : None,
                'cost'                  : 'mse',
                'stopping_criteria'     : DD({
                                            'max_epoch'         : 100,
                                            'epoch_look_back'   : 5,
                                            'cost'              : 'mse',
                                            'percent_decrease'  : 0.025
                                            }) # end stopping_criteria
                }), # end learning_rule

        #===========================[ Dataset ]===========================#
        'dataset' : DD({
                # 'type'                  : 'Laura_Warp_Blocks_500',
                # 'type'                  : 'Laura_Blocks_500',
                # 'type'                  : 'Laura_Blocks',
                'type'                  : 'Laura_Warp_Blocks',
                'feature_size'          : 2049,
                'train_valid_test_ratio': [8, 1, 1],

                # 'preprocessor'          : None,
                # 'preprocessor'          : 'Scale',
                'preprocessor'          : 'GCN',
                # 'preprocessor'          : 'LogGCN',
                # 'preprocessor'          : 'Standardize',

                'batch_size'            : (50, 100, 150, 200),
                'num_batches'           : None,
                'iter_class'            : 'SequentialSubsetIterator',
                'rng'                   : None
                }), # end dataset

        # #============================[ Layers ]===========================#

        'hidden1' : DD({
                'name'                  : 'hidden1',
                'model'                 : 'AE0830_Warp_Blocks_2049_500_tanh_gpu_20140902_0012_36590657',
                'dropout_below'         : 0.5,
                # 'dropout_below'         : 0.1
                }), # end hidden_layer

        'hidden2' : DD({
                'name'                  : 'hidden2',
                'model'                 : 'AE0829_Warp_Blocks_500_180_tanh_20140906_0954_36649151',
                'dropout_below'         : None
                }), # end hidden_layer


        }), # end autoencoder

    ########################[Laura_Three_Layers]########################
    ##################################################################

    'Laura_Three_Layers' : DD({
        'model' : DD({
                'rand_seed'             : None
                }), # end mlp

        'log' : DD({
                'experiment_name'         : 'AE0729_warp_3layers_finetune',
                'description'           : '',
                'save_outputs'          : True,
                'save_hyperparams'      : True,
                'save_model'            : True,
                'save_to_database_name' : 'Database_Name.db'
                }), # end log


        'learning_rule' : DD({
                'max_col_norm'          : (1, 10, 50),
                'learning_rate'         : (1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.5),
                # 'learning_rate'         : ((1e-5, 9e-1), float),
                # 'learning_rate'         : 0.01,
                'momentum'              : (1e-3, 1e-2, 1e-1, 0.5, 0.9),
                # 'momentum'              : 0.05,
                'momentum_type'         : 'normal',
                'L1_lambda'             : None,
                'L2_lambda'             : None,
                'cost'                  : 'mse',
                'stopping_criteria'     : DD({
                                            'max_epoch'         : 100,
                                            'epoch_look_back'   : 10,
                                            'cost'              : 'mse',
                                            'percent_decrease'  : 0.05
                                            }) # end stopping_criteria
                }), # end learning_rule

        #===========================[ Dataset ]===========================#
        'dataset' : DD({
                # 'type'                  : 'Laura_Warp_Blocks_500',
                # 'type'                  : 'Laura_Blocks_500',
                # 'type'                  : 'Laura_Blocks',
                'type'                  : 'Laura_Warp_Blocks',
                'feature_size'          : 2049,
                'train_valid_test_ratio': [8, 1, 1],
                # 'preprocessor'          : None,
                'preprocessor'          : 'Scale',
                # 'preprocessor'          : 'GCN',
                # 'preprocessor'          : 'LogGCN',
#                     'preprocessor'          : 'Standardize',
                'batch_size'            : (50, 100, 150, 200),
                'num_batches'           : None,
                'iter_class'            : 'SequentialSubsetIterator',
                'rng'                   : None
                }), # end dataset

        # #============================[ Layers ]===========================#

        'hidden1' : DD({
                'name'                  : 'hidden1',
                'model'                 : 'AE0713_Warp_500_20140714_1317_43818059',
                'dropout_below'         : (0.1, 0.2, 0.3, 0.4, 0.5),
                # 'dropout_below'         : 0.1
                }), # end hidden_layer

        'hidden2' : DD({
                'name'                  : 'hidden2',
                'model'                 : 'AE0721_Warp_Blocks_500_180_20140723_0131_16567449',
                'dropout_below'         : None
                }), # end hidden_layer

        'hidden3' : DD({
                'name'                  : 'hidden3',
                'model'                 : 'AE0726_Warp_Blocks_180_120_20140727_1631_00459828',
                'dropout_below'         : None
                }), # end hidden_layer


        }), # end autoencoder

    #####################[Two_Layers_No_Transpose]######################
    ####################################################################

    'Laura_Two_Layers_No_Transpose' : DD({

        'model' : DD({
                'rand_seed'             : None
                }), # end mlp

        'log' : DD({
                'experiment_name'       : 'AE0730_No_Transpose_Warp_Blocks_180_64',
                'description'           : '',
                'save_outputs'          : True,
                'save_hyperparams'      : True,
                'save_model'            : True,
                'save_to_database_name' : 'Database_Name.db'
                }), # end log


        'learning_rule' : DD({
                'max_col_norm'          : (1, 10, 50),
                'learning_rate'         : (1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 0.5),
                # 'learning_rate'         : ((1e-5, 9e-1), float),
                # 'learning_rate'         : 0.01,
                'momentum'              : (1e-3, 1e-2, 1e-1, 0.5, 0.9),
                # 'momentum'              : 0.05,
                'momentum_type'         : 'normal',
                'L1_lambda'             : None,
                'L2_lambda'             : None,
                'cost'                  : 'mse',
                'stopping_criteria'     : DD({
                                            'max_epoch'         : 100,
                                            'epoch_look_back'   : 10,
                                            'cost'              : 'mse',
                                            'percent_decrease'  : 0.05
                                            }) # end stopping_criteria
                }), # end learning_rule

        #===========================[ Dataset ]===========================#
        'dataset' : DD({
                'type'                  : 'Laura_Warp_Blocks_180',
                # 'type'                  : 'Laura_Cut_Warp_Blocks_300',
                # 'type'                  : 'Laura_Blocks_500',
                # 'type'                  : 'Laura_Blocks',
                # 'type'                  : 'Laura_Warp_Blocks',
                'feature_size'          : 180,
                'train_valid_test_ratio': [8, 1, 1],
                'preprocessor'          : None,
                # 'preprocessor'          : 'Scale',
                # 'preprocessor'          : 'GCN',
                # 'preprocessor'          : 'LogGCN',
#                     'preprocessor'          : 'Standardize',
                'batch_size'            : (50, 100, 150, 200),
                'num_batches'           : None,
                'iter_class'            : 'SequentialSubsetIterator',
                'rng'                   : None
                }), # end dataset

        # #============================[ Layers ]===========================#
        'num_layers' : 1,

        'hidden1' : DD({
                'name'                  : 'hidden1',
                'type'                  : 'Tanh',
                'dim'                   : 64,
                'dropout_below'         : (0.1, 0.2, 0.3, 0.4, 0.5)
                # 'dropout_below'         : 0.1
                }), # end hidden_layer


        'h1_mirror' : DD({
                'name'                  : 'h1_mirror',
                'type'                  : 'RELU',
                # 'dim'                   : 2049, # dim = input.dim
                'dropout_below'         : None
                }) # end output_layer


        }), # end autoencoder

    }) # end model_config