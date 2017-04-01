define([
    'legacyRegistry',
	'./src/controllers/TodoController'
], function (
    legacyRegistry,
	TodoController
) {
    legacyRegistry.register("tutorials/todo", {
    "name": "TLE Reader",
    "description": "Allows reading of TLEs",
    "extensions": {
        "types": [
            {
                "key": "example.todo",
                "name": "TLE Reader",
                "glyph": "2",
                "description": "Reads TLEs",
                "features": ["creation"],
               "model": {
                   "tasks": [
                       { "description": "   " }
                   ]
                }
            }
        ],
        "views": [
            {
                "key": "example.todo",
                "type": "example.todo",
                "glyph": "2",
                "name": "List",
                "templateUrl": "templates/todo.html",
                "editable": true
            }
        ],
		
		    "controllers": [
            {
                "key": "TodoController",
                "implementation": TodoController,
                "depends": [ "$scope" ]
            }
        ]

    }
    });
});