tinymce.PluginManager.add('hgfblogimg', function (editor, url) {
    // Add a button that opens a window
    editor.addButton('hgfblogimg', {
        text: 'My button',
        icon: false,
        onclick: function () {
            // Open window
            alert('hi');
        }
    });

    // Adds a menu item to the tools menu
    editor.addMenuItem('hgfblogimg', {
        text: 'Insert Image',
        context: 'tools',
        onclick: function () {
            // Open window with a specific url
            editor.windowManager.open({
                title: 'TinyMCE site',
                url: 'http://www.tinymce.com',
                width: 800,
                height: 600,
                buttons: [{
                        text: 'Close',
                        onclick: 'close'
                    }]
            });
        }
    });
});