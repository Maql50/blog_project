KindEditor.ready(function(K){
    K.create('textarea[name=content]', {
        with:'700px',
        height:'100px',
        uploadJson: '/admin/upload/kindeditor',
    });
});