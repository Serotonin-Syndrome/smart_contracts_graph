const CLIENT_COMPATIBILITY = "0.1.5";

const LAST_COMPATIBILITY = localStorage.getItem("client_compatibility")
if (CLIENT_COMPATIBILITY != LAST_COMPATIBILITY) {
    localStorage.clear();
    localStorage.setItem("client_compatibility", CLIENT_COMPATIBILITY)
}

examples = {
    "contract": {
        "code": "class MyContract:\n    def __init__(self, testnet, creator_addr, my_addr, amount):\n        self._testnet = testnet\n\n    def ping(self, who, amount):\n        self._testnet.pay(who, amount)\n"
    },
    "tests": {
        "code": "from time import sleep\n\ndef run_tests(generators, TestNet, MyContract):\n    creator_addr = generators.gen_addr()\n    contract_addr = generators.gen_addr()\n    users = [generators.gen_addr() for _ in range(7)]\n\n    balances = {creator_addr: 2001}\n    for user in users:\n        balances[user] = 952\n\n    testnet = TestNet(balances)\n    testnet.deploy(MyContract, contract_addr=contract_addr, creator_addr=creator_addr, amount=10)\n    for user in users:\n        for i in range(3):\n            sleep(0.5)\n            testnet.call_method('ping', user, i + 1, ())"
    }
};

function initEditor(id) {
    let editor = ace.edit(id);
    editor.setTheme("ace/theme/dracula");
    editor.session.setMode("ace/mode/python");

    let code = localStorage.getItem(id)
    if (code)
        editor.setValue(code);

    editor.session.on('change', function () {
        let code = editor.getValue();
        localStorage.setItem(id, code);
    });
    return editor;
}

let leftEditor = initEditor("editor-left");
let rightEditor = initEditor("editor-right");

if (!leftEditor.getValue() && !rightEditor.getValue()) {
    leftEditor.setValue(examples['contract']['code'])
    rightEditor.setValue(examples['tests']['code'])
}

function runDemo(demoId) {
    $.ajax("/api/simulate-demo", {
        data: {
            'demoid': demoId
        },
        method: "POST"
    }).done(function (result) {
        console.log(result);
        // InterfaceConsole.appendData(result);
        // if (result.stderr) {
        //     file.maintainId = null;
        //     fileSelected(file.name);
        // }
    });
}

function runCode() {
    $.ajax("/api/simulate", {
        data: {
            'code': localStorage.getItem("editor-left"),
            'test': localStorage.getItem("editor-right")
        },
        method: "POST"
    }).done(function (result) {
        console.log(result);
        // InterfaceConsole.appendData(result);
        // if (result.stderr) {
        //     file.maintainId = null;
        //     fileSelected(file.name);
        // }
    });
}

function openViewer(port) {
    if (!port)
        port = 8080
    window.open("http://" + location.hostname + ":" + port, "_blank");
}

$('.simulate-button').on('click', function() {
    runCode();
    openViewer();
});

$('.demo-button').on('click', function (ev) {
   let el = ev.target;
   let demoid = el.dataset.demoid;
   if (demoid == 'gossip') {
       openViewer(8035);
   } else if (!isNaN(demoid)) {
       runDemo(demoid);
       openViewer();
   }
});

