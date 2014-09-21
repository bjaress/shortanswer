class ScriptCheck
    constructor: (element) ->
        @element = element

    check: () ->
        @element.text 'Scripts working'

module.exports = ScriptCheck
