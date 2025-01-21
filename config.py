# Bot Configuration
BOT_CONFIG = {
    'MEMORY_SETTINGS': {
        'MAX_MEMORY_SIZE': 1000,  # Maximum number of conversations to store
        'SESSION_TIMEOUT': 3600,  # Session timeout in seconds (1 hour)
        'MEMORY_CLEANUP_INTERVAL': 300  # Cleanup interval in seconds (5 minutes)
    },
    
    'MODEL_SETTINGS': {
        'MIN_CONFIDENCE': 0.7,  # Minimum confidence threshold for ML responses
        'MAX_INPUT_LENGTH': 500,  # Maximum input text length
        'MIN_WORDS': 2,  # Minimum number of words required in input
        'CROSS_VALIDATION_FOLDS': 5  # Number of folds for cross-validation
    },
    
    'PREPROCESSING': {
        'MAX_NGRAM_RANGE': 3,
        'MAX_FEATURES': 10000,
        'MIN_DF': 2,
        'MAX_DF': 0.95
    }
}

# Logging Configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'nextopson_bot.log',
            'mode': 'a'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}