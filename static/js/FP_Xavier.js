/**
 * Created by Xavier on 2017/7/30.
 */
(function (scope) {

'use strict';

    var browserData;

    // ClientJS constructor which sets the browserData object and returs the client object.
    var FP = function () {
        var parser = new UAParser();
        browserData = parser.getResult();
        return this;
    };

    FP.prototype = {

        // Get OS information
        OSDetection: function (){
            var UAS = navigator.userAgent;
            var isWindows = (navigator.platform === "Win32") || (navigator.platform === "Windows") ||(navigator.platform === "Win64");
            var isMac = (navigator.platform === "Mac68K") || (navigator.platform === "MacPPC") || (navigator.platform === "Macintosh") || (navigator.platform === "MacIntel");
            var isUnix = (navigator.platform === "X11")&&(String(navigator.platform).indexOf("Linux") == -1);
            var isLinux = (String(navigator.platform).indexOf("Linux") > -1);
            var isAndroid = UAS.indexOf("Android") > -1 || UAS.indexOf("Adr") > -1;
            var isiOS = UAS.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/);
            var isWinPhone = UAS.indexOf("Windows Phone") > -1;
            if (isAndroid) {
                var reAndroid = /Android\s[A-Za-z0-9._]+/gi;
                var Android_Version = UAS.match(reAndroid)[0].replace("Android ",'');
                return { out: "Android" , version:Android_Version}}
            if (isiOS) {
                var reiOS = /iPhone\sOS\s[A-Za-z0-9._]+/gi;
                var iOS_version = UAS.match(reiOS)[0].replace("iPhone OS ",'');
                return {out :"iOS",version :iOS_version}}
            if (isWinPhone) return {out: "Windows Phone"};

            if (isMac) {
                var reMac = /Mac\sOS\sX\s[A-Za-z0-9._]+/gi;
                var Mac_Version = UAS.match(reMac)[0].replace("Mac OS X ",'');
                return {out : "Mac" ,version:Mac_Version}}

            if (isUnix) return {out : "Unix"};
            if (isLinux) {
                var reLinux = /Linux\s[A-Za-z0-9._]+/;
                var Linux_Version = UAS.match(reLinux)[0].replace("Linux ",'');
                return {out : "Linux",version:Linux_Version}}

            if (isWindows) {
                var isWin2K = UAS.indexOf("Windows NT 5.0") > -1 ||UAS.indexOf("Windows 2000") > -1;
                if (isWin2K) return {out: "Win2000", version :"NT 5.0"};
                var isWinXP = UAS.indexOf("Windows NT 5.1") > -1 || UAS.indexOf("Windows XP") > -1;
                if (isWinXP) return {out: "WinXP", version :"NT 5.1"};
                var isWin2003 = UAS.indexOf("Windows NT 5.2") > -1 || UAS.indexOf("Windows 2003") > -1;
                if (isWin2003) return {out: "Win2003", version :"NT 5.2"};
                var isWinVista= UAS.indexOf("Windows NT 6.0") > -1 || UAS.indexOf("Windows Vista") > -1;
                if (isWinVista) return {out: "WinVista", version :"NT 6.0"};
                var isWin7 = UAS.indexOf("Windows NT 6.1") > -1 || UAS.indexOf("Windows 7") > -1;
                if (isWin7) return {out: "Win7", version :"NT 6.1"};
                var isWin8 = UAS.indexOf("Windows NT 6.2") > -1 || UAS.indexOf("Windows 8") > -1;
                if (isWin8) return {out: "Win8", version :"NT 6.2"};
                var isWin81 = UAS.indexOf("Windows NT 6.3") > -1 || UAS.indexOf("Windows 8.1") > -1;
                if (isWin81) return {out:"Win8.1", version :"NT 6.3"};
                var isWin10 =  UAS.indexOf("Windows NT 10.0") > -1 || UAS.indexOf("Windows 10");
                if (isWin10) return {out:"Win10", version :"NT 10.0"};
            }
            return {out: "other"};
        },

        // Get browser information
        browserDetection: function (){
            var UAS = navigator.userAgent;
            var isChrome = UAS.indexOf("Chrome") > -1 && UAS.indexOf("Safari") > -1 && UAS.indexOf("Edge") === -1; //To check if the browser is Chrome
            var isSafari = UAS.indexOf("Safari") > -1 && UAS.indexOf("Chrome") === -1; //To check if the browser is Safari
            var isFireFox = UAS.indexOf("Firefox") > -1 ; //To check if the browser is Firefox
            var isOpera = UAS.indexOf("Opera") > -1; // To check if the browser is Opera
            var isIE = UAS.indexOf("MSIE") > -1 || UAS.indexOf("Trident") ; //To check if the browser is IE
            var isEdge = UAS.indexOf("Edge") > -1; //To check if the browser is Edge

            var reIE = new RegExp("MSIE (\\d+\\.\\d+);");
            var reChrome = /Chrome\/[A-Za-z0-9.]+/gi;
            var reSafari = /Safari\/[A-Za-z0-9.]+/gi;
            var reFirefox = /Firefox\/[A-Za-z0-9.]+/gi;
            var reEdge = /Edge\/[A-Za-z0-9.]+/gi;
            var reOpera = /Opera\/[A-Za-z0-9.]+/gi;

            if (isChrome) {
                var Chrome_version = UAS.match(reChrome)[0].replace("Chrome/",'');
                return {b:"Chrome",v:Chrome_version};}
            else if (isFireFox) {
                var Firefox_version = UAS.match(reFirefox)[0].replace("Firefox/",'');
                return {b:"Firefox",v:Firefox_version};}
            else if (isOpera) {
                var Opera_version = UAS.match(reOpera)[0].replace("Opera/",'');
                return {b:"Opera",v:Opera_version};}
            else if (isSafari) {
                var Safari_version = UAS.match(reSafari)[0].replace("Safari/",'');
                return {b:"Safari",v:Safari_version};}
            else if (isEdge) {
                var Edge_version = UAS.match(reEdge)[0].replace("Edge/",'');
                return {b:"Edge",v:Edge_version};}
            if (isIE) {
                if(reIE.test(UAS)) {
                    var IEVersion = parseFloat(RegExp["$1"]);
                    if (IEVersion === 6) {
                        return  {b:"IE",v:"6"};
                    }
                    if (IEVersion === 7) {
                        return  {b:"IE",v:"7"};
                    }
                    else if (IEVersion === 8) {
                        return  {b:"IE",v:"8"};
                    }
                    else if (IEVersion === 9) {
                        return  {b:"IE",v:"9"};
                    }
                    else if (IEVersion === 10) {
                        return  {b:"IE",v:"10"};
                    }
                }
                //To check if the browser is IE 11
                else if (UAS.indexOf("Trident") > -1 && UAS.indexOf("rv") > -1){
                    return  {b:"IE",v:"11"};
                }
                return  {b:"IE",v:"unknown"};
            }//isIE end
        },

        // Get Zoom ratio
        detectZoom: function (){
            var ratio = 0 ,
                screen = window.screen,
                UAS = navigator.userAgent.toLowerCase();

            if (window.devicePixelRatio !== undefined) {
                if (this.OSDetection().out==='Mac'||(this.OSDetection().out==='iOS')){
                    ratio = window.devicePixelRatio/2;
                }
                else {
                    ratio = window.devicePixelRatio;}
                // alert(1);
            }
            else if (~UAS.indexOf('msie')) {
                if (screen.deviceXDPI && screen.logicalXDPI) {
                    ratio = screen.deviceXDPI / screen.logicalXDPI;
                    //alert(2);
                }
            }
            else if (window.outerWidth !== undefined && window.innerWidth !== undefined) {
                ratio = window.outerWidth / window.innerWidth;
                //alert(3);
            }
            //else {alert(4)}
            return ratio;
        },

        // if the browser enable flash
        isFlash: function (){
            var hasFlash = 0;
            var flashVersion = 0;
            if (document.all) {
                var swf = new ActiveXObject('ShockwaveFlash.ShockwaveFlash');
                if (swf) {
                    hasFlash = 1;
                    VSwf = swf.GetVariable("$version");
                    flashVersion = parseInt(VSwf.split(" ")[1].split(",")[0]);
                }
            } else {
                if (navigator.plugins && navigator.plugins.length > 0) {
                    var swf = navigator.plugins["Shockwave Flash"];
                    if (swf) {
                        hasFlash = 1;
                        var words = swf.description.split(" ");
                        for (var i = 0; i < words.length; ++i) {
                            if (isNaN(parseInt(words[i]))) continue;
                            flashVersion = parseInt(words[i]);
                        }
                    }
                }
            }
            return { f: hasFlash, v: flashVersion };
        },

        //Get font list
        getFont: function() {
            var detective = new Detector();
            var fontArray = [
                "Andale Mono", "Arial", "Arial Black", "Arial Hebrew", "Arial MT", "Arial Narrow", "Arial Rounded MT Bold", "Arial Unicode MS",
                "Bitstream Vera Sans Mono", "Book Antiqua", "Bookman Old Style",
                "Calibri", "Cambria", "Cambria Math", "Century", "Century Gothic", "Century Schoolbook", "Comic Sans", "Comic Sans MS", "Consolas", "Courier", "Courier New",
                "Garamond", "Geneva", "Georgia",
                "Helvetica", "Helvetica Neue",
                "Impact",
                "Lucida Bright", "Lucida Calligraphy", "Lucida Console", "Lucida Fax", "LUCIDA GRANDE", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter", "Lucida Sans Unicode",
                "Microsoft Sans Serif", "Monaco", "Monotype Corsiva", "MS Gothic", "MS Outlook", "MS PGothic", "MS Reference Sans Serif", "MS Sans Serif", "MS Serif", "MYRIAD", "MYRIAD PRO",
                "Palatino", "Palatino Linotype",
                "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Symbol",
                "Tahoma", "Times", "Times New Roman", "Times New Roman PS", "Trebuchet MS",
                "Verdana", "Wingdings", "Wingdings 2", "Wingdings 3"
            ];
            var fontString = "";

            for (var i=0; i<fontArray.length; i++) {
                if ( detective.detect( fontArray[i] ) ) {
                    if( i == fontArray.length-1 ) {
                        fontString += fontArray[i];
                    }else{
                        fontString += fontArray[i] + ", ";
                    }
                }
            }
            return fontString;
        },

        getTouchSupport: function () {
            var maxTouchPoints = 0;
            var touchEvent = false;
            if(typeof navigator.maxTouchPoints !== "undefined") {
                maxTouchPoints = navigator.maxTouchPoints;
            } else if (typeof navigator.msMaxTouchPoints !== "undefined") {
                maxTouchPoints = navigator.msMaxTouchPoints;
            }
            try {
                document.createEvent("TouchEvent");
                touchEvent = true;
            } catch(_) {}
            var touchStart = "ontouchstart" in window;
            return [maxTouchPoints, touchEvent, touchStart];
        },

        //Get Plugins
        getPlugins:function () {
            var pluginsLength = navigator.plugins.length;
                var plugins = new Array;
                for(var i = 0; i < pluginsLength; i++) {
                   plugins[i]= navigator.plugins[i].name;
                }
                var pluginString = plugins.join(",");
                return pluginString
        },

        //Get Timezone
        getTimezone:function () {
            var date=new Date();
            var timeZone = date.getTimezoneOffset(); // Get Time Zone
            return timeZone
        },

    };
    if (typeof module === 'object' && typeof exports === 'object') {
        module.exports = FP;
    }
    scope.FP = FP;
})(window);