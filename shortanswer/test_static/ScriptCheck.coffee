ScriptCheck = require '../static/ScriptCheck.coffee'

exports.testScriptCheck = (test) ->
    text = "original"
    dummy =
        text: (modified) ->
            text = modified
    new ScriptCheck(dummy).check()
    test.notEqual "original", text,
        "Text should change."
    test.done()
