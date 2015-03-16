function App() { };


App.fullPage = function (selector) {
  $(selector).fullpage({
    //Navigation
    menu: false,
    // anchors:['firstSlide', 'secondSlide'],
    navigation: false,
    // navigationPosition: 'right',
    // navigationTooltips: ['firstSlide', 'secondSlide'],
    slidesNavigation: true,
    // slidesNavPosition: 'bottom',

    //Scrolling
    css3: true,
    scrollingSpeed: 500,
    autoScrolling: true,
    fitToSection: true,
    scrollBar: false,
    easing: 'easeInOutCubic',
    easingcss3: 'ease',
    loopBottom: false,
    loopTop: false,
    loopHorizontal: true,
    continuousVertical: false,
    normalScrollElements: null,
    scrollOverflow: false,
    touchSensitivity: 15,
    normalScrollElementTouchThreshold: 5,

    //Accessibility
    keyboardScrolling: true,
    animateAnchor: true,
    recordHistory: true,

    //Design
    controlArrows: true,
    verticalCentered: false,
    resize : true,
    sectionsColor : ['#fff'],
    paddingTop: '20px',
    paddingBottom: '20px',
    // fixedElements: 'body, body',
    responsive: 0,

    //Custom selectors
    sectionSelector: '.section',
    slideSelector: '.slide',

    //events
    onLeave: function(index, nextIndex, direction){},
    afterLoad: function(anchorLink, index){},
    afterRender: function(){},
    afterResize: function(){},
    afterSlideLoad: function(anchorLink, index, slideAnchor, slideIndex){},
    onSlideLeave: function(anchorLink, index, slideIndex, direction){}
  });

}


App.clickPost = function() {
  $("#post-btn").click(function() {
    var cp = ctrack.getCurrentParameters();
    var er = ec.predict(cp);
    var major = $('#angry').val();
    var majorname = "angry";
    $('#angry').val(er[0].value.toString());
    $('#sad').val(er[1].value.toString());
    $('#surprised').val(er[2].value.toString());
    $('#happy').val(er[3].value.toString());
    var majorindex=0;
    for(var i = 1;i < 4; i++) {
      if(er[i].value > er[majorindex].value)
        majorindex = i;
    }

    for(var i = 0; i < 4; i++) {
      if(i != majorindex)
        $('#' + er[i].emotion).addClass('hide');
    }

    var postMood = {
      img: imgUrl,
      text: $('#text').val(),
      emotion: er[majorindex].emotion
    }
    $.post('/post/', postMood, function(ret) {
      // console.log(ret);
      location.reload();
    })
  });
};


App.emotionDection = function () {
  var imgUrl = '';
  var ec = new emotionClassifier();
  ec.init(emotionModel);
  var emotionData = ec.getBlank();  
  
  var cc = document.getElementById('image').getContext('2d'); 
  $('#image').click(function(){
    $('#img').click();
  })

  var ctrack = new clm.tracker({stopOnConvergence : true});
  ctrack.init(pModel);
  
  var drawRequest;
  
  function animateClean() {
    ctrack.start(document.getElementById('image'));
    drawLoop();
  }

  function animate(box) {
    ctrack.start(document.getElementById('image'), box);
    drawLoop();
  }
  
  function drawLoop() {
    drawRequest = requestAnimFrame(drawLoop);
    overlayCC.clearRect(0, 0, 720, 576);
    if (ctrack.getCurrentPosition()) {
      ctrack.draw(overlay);
    }
  }
  
  // detect if tracker fails to find a face
  document.addEventListener("clmtrackrNotFound", function(event) {
    ctrack.stop();
    console.log("to late")
  }, false);
  
  // detect if tracker loses tracking of face
  // detect if tracker has converged
  document.addEventListener("clmtrackrConverged", function(event) {
    // stop drawloop
    cancelRequestAnimFrame(drawRequest);
  }, false);
  
  // update stats on iteration
  // document.addEventListener("clmtrackrIteration", function(event) {
  //   stats.update();
  // }, false);

  // manual selection of faces (with jquery imgareaselect plugin)
  function selectBox() {
    document.getElementById('convergence').innerHTML = "";
    ctrack.reset();
    $('#overlay').addClass('hide');
    $('#image').imgAreaSelect({
      handles : true,
      onSelectEnd : function(img, selection) {
        // create box
        var box = [selection.x1, selection.y1, selection.width, selection.height];
        
        // do fitting
        animate(box);
      },
      autoHide : true
    });
  }

  // function to start showing images
  function loadImage() {
    if (fileList.indexOf(fileIndex) < 0) {
      var reader = new FileReader();
      reader.onload = (function(theFile) {
        return function(e) {
          // check if positions already exist in storage
        
          // Render thumbnail.
          var canvas = document.getElementById('image')
          var cc = canvas.getContext('2d');
          var img = new Image();
          img.onload = function() {
            if (img.height > 500 || img.width > 550) {
              var rel = parseFloat(img.height)/img.width;
              var neww = 550 * rel;
              var newh = 500 * rel;
              if (img.height <= 500 && neww > 550) {
                neww = 550;
                // newh = newh * neww/rel;
              }
            }
            // canvas.setAttribute('width', img.width);
            // canvas.setAttribute('height', img.height);
            console.log(parseFloat(550-img.width)/2,
              parseFloat(500-img.height)/2,
              img.width,
              img.height)
            cc.drawImage(img,0,
              0,550, 500);
          }
           
          // console.log(e.target.result)
          imgUrl = e.target.result;
          img.src = e.target.result;
        };
      })(fileList[fileIndex]);
      reader.readAsDataURL(fileList[fileIndex]);
      ctrack.reset();
    }

  }

  // set up file selector and variables to hold selections
  var fileList, fileIndex = 0;
  if (window.File && window.FileReader && window.FileList) {
    function handleFileSelect(evt) {
      var files = evt.target.files;
      fileList = [];
      for (var i = 0;i < files.length;i++) {
        if (!files[i].type.match('image.*')) {
          continue;
        }
        fileList.push(files[i]);
      }
      if (files.length > 0) {
        fileIndex = 0;
      }
      
      loadImage();
      ctrack.start(document.getElementById('image'));
    }
    document.getElementById('img').addEventListener('change', handleFileSelect, false);
  } else {
    // $('#img').addClass("hide");
    $('#loadimagetext').addClass("hide");
  }
}

App.addImageListener = function () {
  $('#img-real').change(function() {
    var $self = $(this);
    var file = $self.get(0).files[0];
    var reader = new FileReader();  
    reader.onload = function(e){  
      render(e.target.result);  
    };  
    reader.readAsDataURL(file); 
  });

};

App.setTagListener = function () {
  $('.mood-type').click(function() {
    var $self = $(this);//, $siblings = $self.siblings();
    $('.mood-type').removeClass('btn-success').addClass('btn-default');
    $self.removeClass('btn-default').addClass('btn-success');
  });
};


App.postListener = function () {
  $('#postBtn').click(function () {
    var file = $('#img-real').get(0).files[0];
    var tag = $('.mood-type.btn-success').text();
    var text = $('textarea').val();
    var formData = new FormData()
    formData.append('image', file, file.name);
    formData.append('tag', tag);
    formData.append('text', text);
    $.ajax({
      url: '/mood/',
      type: 'POST',
      data: formData,
      cache: false,
      contentType: false,
      processData: false,
      success: function(ret) {if(ret)console.log(ret)}
    });
  });
};


function render(src) {
  MAX_HEIGHT = 568;
  var image = new Image();  
  image.onload = function(){  
    var $canvas = $('canvas'); 
    if(image.height > MAX_HEIGHT) {  
        image.width *= MAX_HEIGHT / image.height;  
        image.height = MAX_HEIGHT;  
    }  
    var ctx = $canvas.get(0).getContext('2d');  
    ctx.clearRect(0, 0, $canvas.width(), $canvas.height());  
    $canvas.attr('width', image.width);
    $canvas.attr('height', image.height);
    ctx.drawImage(image, 0, 0, image.width, image.height);  
  };  
  image.src = src;  
}