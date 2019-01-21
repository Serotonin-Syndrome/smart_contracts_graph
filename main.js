const CLIENT_COMPATIBILITY = "0.1.0"

const LAST_COMPATIBILITY = localStorage.getItem("client_compatibility")
if (CLIENT_COMPATIBILITY != LAST_COMPATIBILITY) {
    localStorage.clear();
    localStorage.setItem("client_compatibility", CLIENT_COMPATIBILITY)
}

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
}

initEditor("editor-left")
initEditor("editor-right")


// function callSmartMethod(action, attrs) {
//     let callString = action + '\n' + attrs.join(' ');
//     let file = new File(selectedFile);
//     $.ajax("/api/communicate-maintain", {
//         data: {
//             'id': file.maintainId,
//             'line': callString
//         },
//         method: "POST"
//     }).done(function (result) {
//         console.log(result);
//         InterfaceConsole.appendData(result);
//         if (result.stderr) {
//             file.maintainId = null;
//             fileSelected(file.name);
//         }
//     });
// }


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

function openViewer() {
    window.open("http://" + location.hostname + ":8080", "_blank");
}

$('.simulate-button').on('click', function() {
    runCode();
    openViewer();
});

$('.demo-button').on('click', function (ev) {
   let el = ev.target;
   let demoid = el.dataset.demoid;
   runDemo(demoid);
   openViewer();
});

// $('.create-button').on('click', function () {
//     swal({
//         content: {
//             element: 'input',
//             attributes: {
//                 placeholder: 'Type file name here'
//             }
//         },
//         title: 'Create new file',
//         text: 'Use .c, .cpp or .ll extension.',
//         buttons: {
//             cancel: true,
//             confirm: true
//         }
//     }).then(function (value) {
//         if (value)
//             tryCreateFile(value);
//     });
// });
