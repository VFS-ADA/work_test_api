MONGO_URI = "mongodb://127.0.0.1:27017/visma_work_test"
MONGO_DB = "visma_work_test"

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'secret_documents': {
        'item_title': 'Secret-Document',
        'schema': {
            'headline': {
                'type': 'string',
                'required': True,
            },
            'description': {
                'type': 'string',
            },
            'parent': {
                'type': 'objectid',
                'nullable': True,
                'data_relation': {
                    'resource': 'secret_documents',
                    'embeddable': True
                },
            },
            'is_enabled': {'type': 'boolean', 'default': True},
        },
    },

    'wiki_documents': {
        'item_title': 'Wiki-Document',
        'schema': {
            'headline': {
                'type': 'string',
                'required': True,
            },
            'description': {
                'type': 'string',
            },
            'parent': {
                'type': 'objectid',
                'nullable': True,
                'data_relation': {
                    'resource': 'wiki_documents',
                    'embeddable': True
                },
            },
            'is_enabled': {'type': 'boolean', 'default': True},
        },
    },

    'users': {
        'item_title': 'User',
        'schema': {
            'username': {
                'type': 'string',
                'unique': True,
                'required': True,
            },
            'password': {
                'type': 'string',
                'required': True,
            },
            'view_access': {
                'type': 'list',
                'allowed': ["users", "secret_documents", "wiki_documents"]
            },
            'edit_access': {
                'type': 'list',
                'allowed': ["users", "secret_documents", "wiki_documents"]
            },
            'is_enabled': {'type': 'boolean', 'default': True},
        },
    }
}
