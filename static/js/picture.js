;(function($){


  var LightBox = function(settings){
    var self = this;

    this.settings = {
      speed:500,
      maxWidth:null,
      maxHeight:null,
      maskOpacity:0.5,
      scalePic:0
    };

    $.extend(this.settings,settings || {});

    //创建遮罩和弹出框
    this.popupMask = $('<div id="G-lightbox-mask">');

    this.popupMask.css('opacity',this.settings.maskOpacity);

    this.popupWin = $('<div id="G-lightbox-popup">');

    //保存body
    this.bodyNode = $(document.body);

    //渲染剩余的DOM,并且插入到body
    this.renderDOM();

    this.picViewArea = this.popupWin.find('div.lightbox-pic-view');//图片预览区域
    this.popupPic = this.popupWin.find('img.lightbox-image'); //图片
    this.picCaptionArea = this.popupWin.find('div.lightbox-pic-caption');//图片描述区
    this.nextBtn = this.popupWin.find('span.lightbox-next-btn');
    this.prevBtn = this.popupWin.find('span.lightbox-prev-btn');

    this.captionText = this.popupWin.find('p.lightbox-pic-desc');  //图片描述
    this.currentIndex = this.popupWin.find('span.lightbox-of-index');//图片索引
    this.closeBtn = this.popupWin.find('span.lightbox-close-btn'); //关闭按钮

    //准备开发事件委托 获取数组数据
    this.groupName = null;
    this.groupData = [];

    this.bodyNode.delegate("*[data-role=lightbox]","click",function(e){
      //阻止事件冒泡
      e.stopPropagation();

      var currentGroupName = $(this).attr("data-group");

      if (currentGroupName != self.groupName){
        self.groupName = currentGroupName;
        //根据当前组名获取同一组数据
        self.getGroup();
      }

      //初始化弹框
      self.initPoptup($(this));
    });

    //关闭弹出
    this.popupMask.click(function(){
      $(this).fadeOut();
      self.popupWin.fadeOut();
      self.clear = false;
    });
    this.closeBtn.click(function(){

      self.popupMask.fadeOut();
      self.popupWin.fadeOut();
      self.clear = false;
    });
    //绑定上下切换按钮事件
    this.flag = true;
    this.nextBtn.hover(function(){

      if(!$(this).hasClass("disable") && self.groupData.length>1){
         $(this).addClass("lightbox-next-btn-show");
      }

    },function(){

      if(!$(this).hasClass("disable") && self.groupData.length>1){
        $(this).removeClass("lightbox-next-btn-show");
      }

    }).click(function(e){
      if (!$(this).hasClass("disable")&&self.flag){
        //阻止事件冒泡
        e.stopPropagation();
        self.flag = false;
        self.goto("next");
      }
    });

    this.prevBtn.hover(function(){

      if(!$(this).hasClass("disable") && self.groupData.length>1){
        $(this).addClass("lightbox-prev-btn-show");
      }

    },function(){

      if(!$(this).hasClass("disable") && self.groupData.length>1){
        $(this).removeClass("lightbox-prev-btn-show");
      }

    }).click(function(e){
      if (!$(this).hasClass("disable")&&self.flag){
        //阻止事件冒泡
        e.stopPropagation();
        self.flag = false;
        self.goto("prev");
      }
    });

    //绑定窗口调整时间
    var timer = null;
    this.clear = false;
    $(window).resize(function(){
      if (self.clear){
        window.clearTimeout(timer);
        timer = window.setTimeout(function(){
          self.loadPicSize(self.groupData[self.index].src);
        },500);
      }
    }).keyup(function(e){
      var keyValue = e.which
      if (self.clear){
        if (keyValue == 39 || keyValue == 40){
          self.nextBtn.click();
        }
        if (keyValue == 38 || keyValue == 37){
          self.prevBtn.click();
        }
        if (keyValue == 27){
          self.popupMask.fadeOut();
          self.popupWin.fadeOut();
          self.clear = false;
        }
      }

    })
  };

  LightBox.prototype={
    goto:function(dir){

      if (dir === 'next'){

        this.index++;
        if (this.index >= this.groupData.length-1){
          this.nextBtn.addClass("disable").removeClass("lightbox-next-btn-show");
        }
        if (this.index != 0){

          this.prevBtn.removeClass("disable");
        }
        var src = this.groupData[this.index].src;
        this.loadPicSize(src);

      }else if (dir === 'prev'){
        this.index--;
        if (this.index <= 0){
          this.prevBtn.addClass("disable").removeClass("lightbox-prev-btn-show");
        }
        if (this.index != this.groupData.length-1){
          this.nextBtn.removeClass("disable");
        }
        var src = this.groupData[this.index].src;
        this.loadPicSize(src);
      }
    },
    initPoptup:function(currentObj){

      var self = this,
          sourceSrc = currentObj.attr("data-source"),
          currentId = currentObj.attr("data-id");

      this.showMaskAndPopup(sourceSrc,currentId);


    },
    showMaskAndPopup:function(sourceSrc,currentId){
      var self = this;

      this.popupPic.hide();
      this.picCaptionArea.hide();
      this.popupMask.fadeIn();

      var winWidth = $(window).width(),
          winHeight = $(window).height();

      this.picViewArea.css({
        width:winWidth/2,
        height:winHeight/2
      });

      this.popupWin.fadeIn();

      var viewHeight = winHeight/2 + 10;

      this.popupWin.css({
        width:winWidth/2 + 10,
        height:winHeight/2 + 10,
        marginLeft:-(winWidth/2 + 10)/2,
        top:-viewHeight
      }).animate({
        top:(winHeight-viewHeight)/2
      },self.settings.speed,function(){
        //加载图片
        self.loadPicSize(sourceSrc);
      });

      //根据当前点击的元素ID获取在当前组别里的索引
      this.index = this.getIndexOf(currentId);
      var groupDataLength = this.groupData.length;
      if (groupDataLength>1){
        if (this.index === 0){
          this.prevBtn.addClass("disable");
          this.nextBtn.removeClass("disable");
        }else if (this.index === groupDataLength - 1){
          this.nextBtn.addClass("disable");
          this.prevBtn.removeClass("disable");
        }else{
          this.nextBtn.removeClass("disable");
          this.prevBtn.removeClass("disable");
        }
      }

    },
    loadPicSize:function(sourceSrc){
      var self= this;
      self.popupPic.css({
        width:"auto",
        height:"auto"
      }).hide();
      self.picCaptionArea.hide();
      this.preLoadImg(sourceSrc,function(){
        self.popupPic.attr("src",sourceSrc);

        //拿宽高
        var picWidth = self.popupPic.width(),
            picHeight = self.popupPic.height();

        self.changPic(picWidth,picHeight);
      })
    },
    changPic:function(width,height){

      var self = this,
          winWidth = $(window).width(),
          winHeight = $(window).height();

      //如果图片的宽高大雨流浪器的,要缩放比
      var scale = Math.min(winWidth/(width+10),winHeight/(height+10),1);

      if (self.settings.maxWidth == 'auto' && self.settings.maxHeight == 'auto'){

        width = width*scale * self.settings.scalePic;
        height = height*scale * self.settings.scalePic;

      }else{
        width = self.settings.maxWidth;
        height = self.settings.maxHeight;
      }


      this.picViewArea.animate({
        width:width -10,
        height:height -10
      },self.settings.speed);

      this.popupWin.animate({
        width:width,
        height:height,
        marginLeft:-(width/2),
        top:(winHeight-height)/2
      },self.settings.speed,function(){
        self.popupPic.css({
          width:width -10,
          height:height -10
        }).fadeIn();

        self.picCaptionArea.fadeIn();
        self.flag = true;
        self.clear = true;
      });

      //设置描述文字和当前索引
      this.captionText.text(this.groupData[this.index].caption);
      this.currentIndex.text("当前索引: " + (this.index+1)+" of " + this.groupData.length);

    },
    preLoadImg:function(src,callbcak){
      //判断图片是否加载完
      var img =new Image();
      //IE
      if(!!window.ActiveXObject){
        img.onreadystatechange = function(){
          if (this.readyState == 'complete'){
            callbcak();
          }
        }
      }else{
        img.onload = function(){
          callbcak();
        }
      }

      img.src = src;

    },
    getIndexOf:function(currentId){
      var index = 0 ;

      $(this.groupData).each(function(i){
        index = i;
        if (this.id === currentId){
          return false;
        }
      });

      return index;
    },
    getGroup:function(){
      var self = this;
      //根据当前的组别名称获取页面中相同组名的对象
      var groupList = this.bodyNode.find("*[data-group="+this.groupName+"]");

      //清空数组数据 添加数据
      self.groupData.length = 0;
      groupList.each(function(){
        self.groupData.push({
          src:$(this).attr("data-source"),
          id:$(this).attr("data-id"),
          caption:$(this).attr("data-caption")
        });
      });



    },
    renderDOM:function(){
      var strDom = '<div class="lightbox-pic-view">'+
        '<span class="lightbox-btn lightbox-prev-btn"></span>'+
        '<img class="lightbox-image" src="" >'+
        '<span class="lightbox-btn lightbox-next-btn"></span>'+

        '</div>'+

        '<div class="lightbox-pic-caption">'+
        '<div class="lightbox-caption-area">'+
        '<p class="lightbox-pic-desc">FFFF</p>'+
        '<span class="lightbox-of-index">当前索引: 0 of 0</span>'+
      '</div>'+
      '<span class="lightbox-close-btn"></span>'+
        '</div>';

      //插入到popupWin中
      this.popupWin.html(strDom);
      //把 遮罩和弹出框插入到body中
      this.bodyNode.append(this.popupMask,this.popupWin);
    }
  };

  window['LightBox'] = LightBox;

})(jQuery);