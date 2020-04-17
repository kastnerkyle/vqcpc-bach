from pathlib import Path


config = {
    # the legacy
    # 'config_encoder':              'models/encoder_sameSeq_config_2020-04-10_17-25-49_bkp/config'
    #                                '.py',
    'config_encoder': 'models/encoder_sameSeq_config_2020-04-16_12-51-51/config'
                      '.py',
    'training_method':             'decoder',
    'dataset':                     'bach',

    # --- Dataloader ---
    'dataloader_generator_kwargs': dict(
        sequences_size=24
    ),  # Can be different from the encoder's data loader

    # --- DataProcessor ---
    'data_processor_type':         'bach',  # can be used to filter out some channels
    'data_processor_kwargs':       dict(
        embedding_size=32
    ),  # Can be different from the encoder's data processor

    # --- Decoder ---
    'decoder_type':                'transformer_relative_diagonal',
    # 'transformer' = not relative, dumb positional embeddings,
    # 'transformer_relative' = AC //AC // C,
    # 'transformer_relative_full' = F // F // C
    # transformer_relative_diagonal = cross-attention mask is the identity = AC // D // C
    'decoder_kwargs':              dict(
        d_model=512,
        n_head=8,
        num_encoder_layers=3,
        num_decoder_layers=3,
        dim_feedforward=1024,
        positional_embedding_size=8,
        dropout=0.2,
    ),
    # ======== Training ========
    'lr':                          1e-4,
    'batch_size':                  16,
    'num_batches':                 256,
    'num_epochs':                  20000,

    # ======== model ID ========
    'timestamp':                   None,
    'savename':                    Path(__file__).stem,
}
