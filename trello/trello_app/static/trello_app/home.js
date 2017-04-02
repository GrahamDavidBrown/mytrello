function Display(category){
    console.log("stuff");
    $.ajax({
      url: "http://127.0.0.1:8000/api/"+category+"/",
      success: function(data){
        console.log(data);
        // json = JSON.parse(data);
        console.log(data.results[0]);
        $('#myBoard').append('<div id='+ data.results[0].title.replace(/\s/g, '') +'><a onclick="Display(\''+data.results[0].child+'\')">' + data.results[0].title + '</a><br></div>');
        // $('div'+key).append('<div'+ data.name.replace(/\s/g, '') +'><a onclick="Display(\''+url+'\',\''+data.name+'\')">' + data.name + '</a><br><//div>');

      }
      // .replace(/\s/g, '')
      // return data.results[0];

    });
}
Display('boards')
