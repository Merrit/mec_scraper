from src.mec_product import MECProduct


def get_product(mocker):
    mocker.patch('src.mec_product.MECProduct._get_page', return_value=example_html)
    return MECProduct('')


def test_get_soup(mocker):
    product = get_product(mocker)
    soup = product._get_soup()
    assert str(soup) is not None


def test_get_data(mocker):
    product = get_product(mocker)
    data = product._get_data()
    assert data['productID'] == '5050-315'


def test_get_name(mocker):
    product = get_product(mocker)
    data = product._get_data()
    assert data['name'] == 'Patagonia Quandary Pants - Women\'s'


def test_get_offers(mocker):
    product = get_product(mocker)
    offers = product._get_offers()
    assert len(offers) > 0


def test_get_prices(mocker):
    product = get_product(mocker)
    prices = product._get_prices()
    assert len(prices) > 0


def test_get_price(mocker):
    mocker.patch('src.mec_product.MECProduct._get_page', return_value=example_html)
    mocker.patch('src.mec_product.MECProduct._get_prices', return_value=[1.29, 5.99, 9.99])
    product = MECProduct('')
    price = product._get_price()
    assert price == 1.29


def test_name(mocker):
    product = get_product(mocker)
    assert product.name == 'Patagonia Quandary Pants - Women\'s'


def test_price(mocker):
    product = get_product(mocker)
    assert product.price == 99.00


example_html: str = '''
<!DOCTYPE html>
<html lang="en">
<head>

	<title>
		Patagonia Quandary Pants - Women&#039;s | MEC</title>

	<meta name="twitter:title" content="Patagonia Quandary Pants - Women&#039;s | MEC">
	<meta property="og:title" content="Patagonia Quandary Pants - Women&#039;s | MEC">

	<meta property="fb:page_id" content="39354016609">
	<meta property="og:site_name" content="MEC">
	<meta name="twitter:card" content="summary">
	<meta name="twitter:site" content="@mec">
	<meta name="twitter:creator" content="@MEC">

	<meta property="og:type" content="product">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="keywords">
<meta name="description" content="Quandary Pants: On the trail, on your bike, on the street &ndash; these light, tough pants are everything you need for summer action. The breathable stretch fabric moves with you, so you&rsquo;re al">
<meta property="og:image" content="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8992982892574/5050315-FRG00-fallback.jpg">
<meta name="robots" content="index,follow">
<meta property="og:url" content="https://www.mec.ca/en/product/5050-315/Quandary-Pants">
<meta name="twitter:description" content="Quandary Pants: On the trail, on your bike, on the street &ndash; these light, tough pants are everything you need for summer action. The breathable stretch fabric moves with you, so you&rsquo;re al">
<meta property="og:description" content="Quandary Pants: On the trail, on your bike, on the street &ndash; these light, tough pants are everything you need for summer action. The breathable stretch fabric moves with you, so you&rsquo;re al">
<link hreflang="fr" rel="alternate" href="https://www.mec.ca/fr/product/5050-315/Pantalon-Quandary"/>
<link hreflang="x-default" rel="alternate" href="https://www.mec.ca/en/product/5050-315/Quandary-Pants"/>
<link hreflang="en" rel="alternate" href="https://www.mec.ca/en/product/5050-315/Quandary-Pants"/>
<link rel="canonical" href="https://www.mec.ca/en/product/5050-315/Quandary-Pants"/>
<script>
// Source: https://github.com/GoogleChromeLabs/tti-polyfill
!function(){if('PerformanceLongTaskTiming' in window){var g=window.__tti={e:[]};
g.o=new PerformanceObserver(function(l){g.e=g.e.concat(l.getEntries())});
g.o.observe({entryTypes:['longtask']})}}();
</script>
<script>
    var MECPerformanceMetrics = {};
    if (window.PerformanceObserver && window.PerformanceEntry && window.PerformanceLongTaskTiming) {

        var MECPerformanceObserver = new PerformanceObserver(function(list) {
            var entries = list.getEntries();

            for (var i = 0; i < entries.length; i++) {
                var entry = entries[i];

                switch (entry.entryType) {
                    case 'paint':
                        if (typeof(newrelic) !== 'undefined') {
                            newrelic.setCustomAttribute(entry.name, entry.startTime);
                            newrelic.setCustomAttribute(entry.name + '--duration', entry.duration);
                        }

                        MECPerformanceMetrics[entry.name] = entry.startTime;

                        break;
                    case 'longtask':
                        if (entry.attribution[0].containerType !== 'iframe') {
                            var attribution = entry.attribution[0];

                            if (typeof(newrelic) !== 'undefined') {
                                newrelic.addPageAction('longTask', {
                                    longTaskContainerType: attribution.containerType,
                                    longTaskContainerId: attribution.containerId,
                                    longTaskContainerName: attribution.containerName,
                                    longTaskContainerSrc: attribution.containerSrc,
                                    longTaskStartTime: Math.round(entry.startTime),
                                    longTaskduration: Math.round(entry.duration),
                                });
                            }
                        }
                        break;
                    default:
                        break;
                }
            }
        });

        MECPerformanceObserver.observe({entryTypes: ['paint', 'longtask']});
    }
</script>
<script>
    function performanceMarker(marker) {
        if (window.performance && typeof(window.performance.mark) !== 'undefined') {
            performance.mark(marker);
        }
    }
    function clearPerformanceMarker(marker) {
        if (window.performance && typeof(window.performance.clearMarks) !== 'undefined') {
            performance.clearMarks(marker);
        }
    }
    function performanceClearAndMark(marker) {
        if (window.performance && typeof(window.performance.mark) !== 'undefined' && typeof(window.performance.clearMarks) !== 'undefined') {
            performance.clearMarks(marker);
            performance.mark(marker);
        }
    }
</script>













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-57x57.png?v=GvJMgPgyYM" sizes="57x57" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-60x60.png?v=GvJMgPgyYM" sizes="60x60" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-72x72.png?v=GvJMgPgyYM" sizes="72x72" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-76x76.png?v=GvJMgPgyYM" sizes="76x76" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-114x114.png?v=GvJMgPgyYM" sizes="114x114" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-120x120.png?v=GvJMgPgyYM" sizes="120x120" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-144x144.png?v=GvJMgPgyYM" sizes="144x144" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-152x152.png?v=GvJMgPgyYM" sizes="152x152" >













<link rel="apple-touch-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/apple-touch-icon-180x180.png?v=GvJMgPgyYM" sizes="180x180" >













<link rel="icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/favicon-16x16.png?v=GvJMgPgyYM" type="image/png" sizes="16x16" >













<link rel="icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/favicon-32x32.png?v=GvJMgPgyYM" type="image/png" sizes="32x32" >













<link rel="icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/favicon-194x194.png?v=GvJMgPgyYM" type="image/png" sizes="194x194" >













<link rel="icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/android-chrome-192x192.png?v=GvJMgPgyYM" type="image/png" sizes="192x192" >













<link rel="manifest" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/manifest.json?v=GvJMgPgyYM" >













<link rel="shortcut icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/favicon.ico?v=GvJMgPgyYM" >













<link rel="mask-icon" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/safari-pinned-tab.svg?v=GvJMgPgyYM" color="#525252" >
<meta name="apple-mobile-web-app-title" content="MEC" />
<meta name="application-name" content="MEC" />
<meta name="msapplication-TileColor" content="#0ca948" />









<meta name="msapplication-TileImage" content="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/mstile-144x144.png?v=GvJMgPgyYM">









<meta name="msapplication-config" content="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/favicons/browserconfig.xml?v=GvJMgPgyYM">
<meta name="theme-color" content="#0ca948" />
<link rel="stylesheet" type="text/css" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/css/mec_bundled.css" />
<link rel="stylesheet" type="text/css" href="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/css/core.css" />

<script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"VwQHUldXGwEFUVZQAwAH",licenseKey:"5dfbfbeddb",applicationID:"25572410"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{s.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(29),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,s){try{l?l-=1:o(s||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:c.now();i("err",[t,n])}var i=t("handle"),a=t(30),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,p="nr@seenError";if(!c.disabled){var l=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(13),t(12),"addEventListener"in window&&t(6),c.xhrWrappable&&t(14),d=!0)}s.on("fn-start",function(t,e,n){d&&(l+=1)}),s.on("fn-err",function(t,e,n){d&&!n[p]&&(f(n,p,function(){return!0}),this.thrown=!0,o(n))}),s.on("fn-end",function(){d&&!this.thrown&&l>0&&(l-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})}},{}],3:[function(t,e,n){var r=t("loader");r.disabled||(r.features.ins=!0)},{}],4:[function(t,e,n){function r(){L++,C=g.hash,this[u]=y.now()}function o(){L--,g.hash!==C&&i(0,!0);var t=y.now();this[h]=~~this[h]+t-this[u],this[d]=t}function i(t,e){E.emit("newURL",[""+g,e])}function a(t,e){t.on(e,function(){this[e]=y.now()})}var s="-start",c="-end",f="-body",u="fn"+s,d="fn"+c,p="cb"+s,l="cb"+c,h="jsTime",m="fetch",v="addEventListener",w=window,g=w.location,y=t("loader");if(w[v]&&y.xhrWrappable&&!y.disabled){var x=t(10),b=t(11),E=t(8),R=t(6),O=t(13),S=t(7),N=t(14),M=t(9),P=t("ee"),T=P.get("tracer");t(16),y.features.spa=!0;var C,L=0;P.on(u,r),b.on(p,r),M.on(p,r),P.on(d,o),b.on(l,o),M.on(l,o),P.buffer([u,d,"xhr-done","xhr-resolved"]),R.buffer([u]),O.buffer(["setTimeout"+c,"clearTimeout"+s,u]),N.buffer([u,"new-xhr","send-xhr"+s]),S.buffer([m+s,m+"-done",m+f+s,m+f+c]),E.buffer(["newURL"]),x.buffer([u]),b.buffer(["propagate",p,l,"executor-err","resolve"+s]),T.buffer([u,"no-"+u]),M.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"]),a(N,"send-xhr"+s),a(P,"xhr-resolved"),a(P,"xhr-done"),a(S,m+s),a(S,m+"-done"),a(M,"new-jsonp"),a(M,"jsonp-end"),a(M,"cb-start"),E.on("pushState-end",i),E.on("replaceState-end",i),w[v]("hashchange",i,!0),w[v]("load",i,!0),w[v]("popstate",function(){i(0,L>1)},!0)}},{}],5:[function(t,e,n){function r(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var o=t("ee"),i=t("handle"),a=t(13),s=t(12),c="learResourceTimings",f="addEventListener",u="resourcetimingbufferfull",d="bstResource",p="resource",l="-start",h="-end",m="fn"+l,v="fn"+h,w="bstTimer",g="pushState",y=t("loader");if(!y.disabled){y.features.stn=!0,t(8),"addEventListener"in window&&t(6);var x=NREUM.o.EV;o.on(m,function(t,e){var n=t[0];n instanceof x&&(this.bstStart=y.now())}),o.on(v,function(t,e){var n=t[0];n instanceof x&&i("bst",[n,e,this.bstStart,y.now()])}),a.on(m,function(t,e,n){this.bstStart=y.now(),this.bstType=n}),a.on(v,function(t,e){i(w,[e,this.bstStart,y.now(),this.bstType])}),s.on(m,function(){this.bstStart=y.now()}),s.on(v,function(t,e){i(w,[e,this.bstStart,y.now(),"requestAnimationFrame"])}),o.on(g+l,function(t){this.time=y.now(),this.startPath=location.pathname+location.hash}),o.on(g+h,function(t){i("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),f in window.performance&&(window.performance["c"+c]?window.performance[f](u,function(t){i(d,[window.performance.getEntriesByType(p)]),window.performance["c"+c]()},!1):window.performance[f]("webkit"+u,function(t){i(d,[window.performance.getEntriesByType(p)]),window.performance["webkitC"+c]()},!1)),document[f]("scroll",r,{passive:!0}),document[f]("keypress",r,!1),document[f]("click",r,!1)}}},{}],6:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),s=t("wrap-function")(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1],r=c(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?s(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],7:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=i(arguments),e={};o.emit(n+"before-start",[t],e);var a;e[m]&&e[m].dt&&(a=e[m].dt);var s=r.apply(this,t);return o.emit(n+"start",[t,a],s),s.then(function(t){return o.emit(n+"end",[null,t],s),t},function(t){throw o.emit(n+"end",[t],s),t})})}var o=t("ee").get("fetch"),i=t(30),a=t(29);e.exports=o;var s=window,c="fetch-",f=c+"body-",u=["arrayBuffer","blob","json","text","formData"],d=s.Request,p=s.Response,l=s.fetch,h="prototype",m="nr@context";d&&p&&l&&(a(u,function(t,e){r(d[h],e,f),r(p[h],e,f)}),r(s,"fetch",c),o.on(c+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),o.emit(c+"done",[null,e],n)}else o.emit(c+"done",[t],n)}))},{}],8:[function(t,e,n){var r=t("ee").get("history"),o=t("wrap-function")(r);e.exports=r;var i=window.history&&window.history.constructor&&window.history.constructor.prototype,a=window.history;i&&i.pushState&&i.replaceState&&(a=i),o.inPlace(a,["pushState","replaceState"],"-")},{}],9:[function(t,e,n){function r(t){function e(){c.emit("jsonp-end",[],p),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}function n(){c.emit("jsonp-error",[],p),c.emit("jsonp-end",[],p),t.removeEventListener("load",e,!1),t.removeEventListener("error",n,!1)}var r=t&&"string"==typeof t.nodeName&&"script"===t.nodeName.toLowerCase();if(r){var o="function"==typeof t.addEventListener;if(o){var a=i(t.src);if(a){var u=s(a),d="function"==typeof u.parent[u.key];if(d){var p={};f.inPlace(u.parent,[u.key],"cb-",p),t.addEventListener("load",e,!1),t.addEventListener("error",n,!1),c.emit("new-jsonp",[t.src],p)}}}}}function o(){return"addEventListener"in window}function i(t){var e=t.match(u);return e?e[1]:null}function a(t,e){var n=t.match(p),r=n[1],o=n[3];return o?a(o,e[r]):e[r]}function s(t){var e=t.match(d);return e&&e.length>=3?{key:e[2],parent:a(e[1],window)}:{key:t,parent:window}}var c=t("ee").get("jsonp"),f=t("wrap-function")(c);if(e.exports=c,o()){var u=/[?&](?:callback|cb)=([^&#]+)/,d=/(.*)\.([^.]+)/,p=/^(\w+)(\.|$)(.*)$/,l=["appendChild","insertBefore","replaceChild"];Node&&Node.prototype&&Node.prototype.appendChild?f.inPlace(Node.prototype,l,"dom-"):(f.inPlace(HTMLElement.prototype,l,"dom-"),f.inPlace(HTMLHeadElement.prototype,l,"dom-"),f.inPlace(HTMLBodyElement.prototype,l,"dom-")),c.on("dom-start",function(t){r(t[0])})}},{}],10:[function(t,e,n){var r=t("ee").get("mutation"),o=t("wrap-function")(r),i=NREUM.o.MO;e.exports=r,i&&(window.MutationObserver=function(t){return this instanceof i?new i(o(t,"fn-")):i.apply(this,arguments)},MutationObserver.prototype=i.prototype)},{}],11:[function(t,e,n){function r(t){var e=i.context(),n=s(t,"executor-",e,null,!1),r=new f(n);return i.context(r).getCtx=function(){return e},r}var o=t("wrap-function"),i=t("ee").get("promise"),a=t("ee").getOrSetContext,s=o(i),c=t(29),f=NREUM.o.PR;e.exports=i,f&&(window.Promise=r,["all","race"].forEach(function(t){var e=f[t];f[t]=function(n){function r(t){return function(){i.emit("propagate",[null,!o],a,!1,!1),o=o||!t}}var o=!1;c(n,function(e,n){Promise.resolve(n).then(r("all"===t),r(!1))});var a=e.apply(f,arguments),s=f.resolve(a);return s}}),["resolve","reject"].forEach(function(t){var e=f[t];f[t]=function(t){var n=e.apply(f,arguments);return t!==n&&i.emit("propagate",[t,!0],n,!1,!1),n}}),f.prototype["catch"]=function(t){return this.then(null,t)},f.prototype=Object.create(f.prototype,{constructor:{value:r}}),c(Object.getOwnPropertyNames(f),function(t,e){try{r[e]=f[e]}catch(n){}}),o.wrapInPlace(f.prototype,"then",function(t){return function(){var e=this,n=o.argsToArray.apply(this,arguments),r=a(e);r.promise=e,n[0]=s(n[0],"cb-",r,null,!1),n[1]=s(n[1],"cb-",r,null,!1);var c=t.apply(this,n);return r.nextPromise=c,i.emit("propagate",[e,!0],c,!1,!1),c}}),i.on("executor-start",function(t){t[0]=s(t[0],"resolve-",this,null,!1),t[1]=s(t[1],"resolve-",this,null,!1)}),i.on("executor-err",function(t,e,n){t[1](n)}),i.on("cb-end",function(t,e,n){i.emit("propagate",[n,!0],this.nextPromise,!1,!1)}),i.on("propagate",function(t,e,n){this.getCtx&&!e||(this.getCtx=function(){if(t instanceof Promise)var e=i.context(t);return e&&e.getCtx?e.getCtx():this})}),r.toString=function(){return""+f})},{}],12:[function(t,e,n){var r=t("ee").get("raf"),o=t("wrap-function")(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],13:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t("wrap-function")(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],14:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",s)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,g,"fn-",s)}function i(t){y.push(t),h&&(b?b.then(a):v?v(a):(E=-E,R.data=E))}function a(){for(var t=0;t<y.length;t++)r([],y[t]);y.length&&(y=[])}function s(t,e){return e}function c(t,e){for(var n in t)e[n]=t[n];return e}t(6);var f=t("ee"),u=f.get("xhr"),d=t("wrap-function")(u),p=NREUM.o,l=p.XHR,h=p.MO,m=p.PR,v=p.SI,w="readystatechange",g=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],y=[];e.exports=u;var x=window.XMLHttpRequest=function(t){var e=new l(t);try{u.emit("new-xhr",[e],e),e.addEventListener(w,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(c(l,x),x.prototype=l.prototype,d.inPlace(x.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var b=m&&m.resolve();if(!v&&!m){var E=1,R=document.createTextNode(E);new h(a).observe(R,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===w||a()})},{}],15:[function(t,e,n){function r(t){if(!s(t))return null;var e=window.NREUM;if(!e.loader_config)return null;var n=(e.loader_config.accountID||"").toString()||null,r=(e.loader_config.agentID||"").toString()||null,f=(e.loader_config.trustKey||"").toString()||null;if(!n||!r)return null;var h=l.generateSpanId(),m=l.generateTraceId(),v=Date.now(),w={spanId:h,traceId:m,timestamp:v};return(t.sameOrigin||c(t)&&p())&&(w.traceContextParentHeader=o(h,m),w.traceContextStateHeader=i(h,v,n,r,f)),(t.sameOrigin&&!u()||!t.sameOrigin&&c(t)&&d())&&(w.newrelicHeader=a(h,m,v,n,r,f)),w}function o(t,e){return"00-"+e+"-"+t+"-01"}function i(t,e,n,r,o){var i=0,a="",s=1,c="",f="";return o+"@nr="+i+"-"+s+"-"+n+"-"+r+"-"+t+"-"+a+"-"+c+"-"+f+"-"+e}function a(t,e,n,r,o,i){var a="btoa"in window&&"function"==typeof window.btoa;if(!a)return null;var s={v:[0,1],d:{ty:"Browser",ac:r,ap:o,id:t,tr:e,ti:n}};return i&&r!==i&&(s.d.tk=i),btoa(JSON.stringify(s))}function s(t){return f()&&c(t)}function c(t){var e=!1,n={};if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(n=NREUM.init.distributed_tracing),t.sameOrigin)e=!0;else if(n.allowed_origins instanceof Array)for(var r=0;r<n.allowed_origins.length;r++){var o=h(n.allowed_origins[r]);if(t.hostname===o.hostname&&t.protocol===o.protocol&&t.port===o.port){e=!0;break}}return e}function f(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.enabled}function u(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.exclude_newrelic_header}function d(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&NREUM.init.distributed_tracing.cors_use_newrelic_header!==!1}function p(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.cors_use_tracecontext_headers}var l=t(26),h=t(17);e.exports={generateTracePayload:r,shouldGenerateTrace:s}},{}],16:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<p;r++)t.removeEventListener(d[r],this.listener,!1);e.aborted||(n.duration=a.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==e.status&&(e.status=0):i(this,t),n.cbTime=this.cbTime,u.emit("xhr-done",[t],t),s("xhr",[e,n,this.startTime]))}}function o(t,e){var n=c(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.parsedOrigin=n,t.sameOrigin=n.sameOrigin}function i(t,e){t.params.status=e.status;var n=v(e,t.lastSize);if(n&&(t.metrics.rxSize=n),t.sameOrigin){var r=e.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var a=t("loader");if(a.xhrWrappable&&!a.disabled){var s=t("handle"),c=t(17),f=t(15).generateTracePayload,u=t("ee"),d=["load","error","abort","timeout"],p=d.length,l=t("id"),h=t(22),m=t(21),v=t(18),w=NREUM.o.REQ,g=window.XMLHttpRequest;a.features.xhr=!0,t(14),t(7),u.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,e.loadCaptureCalled=!1,e.params=this.params||{},e.metrics=this.metrics||{},t.addEventListener("load",function(n){i(e,t)},!1),h&&(h>34||h<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),u.on("open-xhr-start",function(t){this.params={method:t[0]},o(this,t[1]),this.metrics={}}),u.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var n=f(this.parsedOrigin);if(n){var r=!1;n.newrelicHeader&&(e.setRequestHeader("newrelic",n.newrelicHeader),r=!0),n.traceContextParentHeader&&(e.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&e.setRequestHeader("tracestate",n.traceContextStateHeader),r=!0),r&&(this.dt=n)}}),u.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=m(r);i&&(n.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"!==t.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}};for(var s=0;s<p;s++)e.addEventListener(d[s],this.listener,!1)}),u.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),u.on("xhr-load-added",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),u.on("xhr-load-removed",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),u.on("addEventListener-end",function(t,e){e instanceof g&&"load"===t[0]&&u.emit("xhr-load-added",[t[1],t[2]],e)}),u.on("removeEventListener-end",function(t,e){e instanceof g&&"load"===t[0]&&u.emit("xhr-load-removed",[t[1],t[2]],e)}),u.on("fn-start",function(t,e,n){e instanceof g&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),u.on("fn-end",function(t,e){this.xhrCbStart&&u.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)}),u.on("fetch-before-start",function(t){function e(t,e){var n=!1;return e.newrelicHeader&&(t.set("newrelic",e.newrelicHeader),n=!0),e.traceContextParentHeader&&(t.set("traceparent",e.traceContextParentHeader),e.traceContextStateHeader&&t.set("tracestate",e.traceContextStateHeader),n=!0),n}var n,r=t[1]||{};"string"==typeof t[0]?n=t[0]:t[0]&&t[0].url?n=t[0].url:window.URL&&t[0]&&t[0]instanceof URL&&(n=t[0].href),n&&(this.parsedOrigin=c(n),this.sameOrigin=this.parsedOrigin.sameOrigin);var o=f(this.parsedOrigin);if(o&&(o.newrelicHeader||o.traceContextParentHeader))if("string"==typeof t[0]||window.URL&&t[0]&&t[0]instanceof URL){var i={};for(var a in r)i[a]=r[a];i.headers=new Headers(r.headers||{}),e(i.headers,o)&&(this.dt=o),t.length>1?t[1]=i:t.push(i)}else t[0]&&t[0].headers&&e(t[0].headers,o)&&(this.dt=o)}),u.on("fetch-start",function(t,e){this.params={},this.metrics={},this.startTime=a.now(),t.length>=1&&(this.target=t[0]),t.length>=2&&(this.opts=t[1]);var n,r=this.opts||{},i=this.target;"string"==typeof i?n=i:"object"==typeof i&&i instanceof w?n=i.url:window.URL&&"object"==typeof i&&i instanceof URL&&(n=i.href),o(this,n);var s=(""+(i&&i instanceof w&&i.method||r.method||"GET")).toUpperCase();this.params.method=s,this.txSize=m(r.body)||0}),u.on("fetch-done",function(t,e){this.params||(this.params={}),this.params.status=e?e.status:0;var n;"string"==typeof this.rxSize&&this.rxSize.length>0&&(n=+this.rxSize);var r={txSize:this.txSize,rxSize:n,duration:a.now()-this.startTime};s("xhr",[this.params,r,this.startTime])})}},{}],17:[function(t,e,n){var r={};e.exports=function(t){if(t in r)return r[t];var e=document.createElement("a"),n=window.location,o={};e.href=t,o.port=e.port;var i=e.href.split("://");!o.port&&i[1]&&(o.port=i[1].split("/")[0].split("@").pop().split(":")[1]),o.port&&"0"!==o.port||(o.port="https"===i[0]?"443":"80"),o.hostname=e.hostname||n.hostname,o.pathname=e.pathname,o.protocol=i[0],"/"!==o.pathname.charAt(0)&&(o.pathname="/"+o.pathname);var a=!e.protocol||":"===e.protocol||e.protocol===n.protocol,s=e.hostname===document.domain&&e.port===n.port;return o.sameOrigin=a&&(!e.hostname||s),"/"===o.pathname&&(r[t]=o),o}},{}],18:[function(t,e,n){function r(t,e){var n=t.responseType;return"json"===n&&null!==e?e:"arraybuffer"===n||"blob"===n||"json"===n?o(t.response):"text"===n||""===n||void 0===n?o(t.responseText):void 0}var o=t(21);e.exports=r},{}],19:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[f.now()].concat(s(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(29),s=t(30),c=t("ee").get("tracer"),f=t("loader"),u=NREUM;"undefined"==typeof window.newrelic&&(newrelic=u);var d=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],p="api-",l=p+"ixn-";a(d,function(t,e){u[e]=o(p+e,!0,"api")}),u.addPageAction=o(p+"addPageAction",!0),u.setCurrentRouteName=o(p+"routeName",!0),e.exports=newrelic,u.interaction=function(){return(new r).get()};var h=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(l+"tracer",[f.now(),t,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],n),t}finally{c.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){h[e]=o(l+e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),i("err",[t,f.now(),!1,e])}},{}],20:[function(t,e,n){function r(t){if(NREUM.init){for(var e=NREUM.init,n=t.split("."),r=0;r<n.length-1;r++)if(e=e[n[r]],"object"!=typeof e)return;return e=e[n[n.length-1]]}}e.exports={getConfiguration:r}},{}],21:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],22:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],23:[function(t,e,n){function r(){return s.exists&&performance.now?Math.round(performance.now()):(i=Math.max((new Date).getTime(),i))-a}function o(){return i}var i=(new Date).getTime(),a=i,s=t(31);e.exports=r,e.exports.offset=a,e.exports.getLastTimestamp=o},{}],24:[function(t,e,n){function r(t){return!(!t||!t.protocol||"file:"===t.protocol)}e.exports=r},{}],25:[function(t,e,n){function r(t,e){var n=t.getEntries();n.forEach(function(t){"first-paint"===t.name?d("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&d("timing",["fcp",Math.floor(t.startTime)])})}function o(t,e){var n=t.getEntries();n.length>0&&d("lcp",[n[n.length-1]])}function i(t){t.getEntries().forEach(function(t){t.hadRecentInput||d("cls",[t])})}function a(t){if(t instanceof h&&!v){var e=Math.round(t.timeStamp),n={type:t.type};e<=p.now()?n.fid=p.now()-e:e>p.offset&&e<=Date.now()?(e-=p.offset,n.fid=p.now()-e):e=p.now(),v=!0,d("timing",["fi",e,n])}}function s(t){"hidden"===t&&d("pageHide",[p.now()])}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var c,f,u,d=t("handle"),p=t("loader"),l=t(28),h=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){c=new PerformanceObserver(r);try{c.observe({entryTypes:["paint"]})}catch(m){}f=new PerformanceObserver(o);try{f.observe({entryTypes:["largest-contentful-paint"]})}catch(m){}u=new PerformanceObserver(i);try{u.observe({type:"layout-shift",buffered:!0})}catch(m){}}if("addEventListener"in document){var v=!1,w=["click","keydown","mousedown","pointerdown","touchstart"];w.forEach(function(t){document.addEventListener(t,a,!1)})}l(s)}},{}],26:[function(t,e,n){function r(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var o,i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",s=0;s<i.length;s++)o=i[s],"x"===o?a+=t().toString(16):"y"===o?(o=3&t()|8,a+=o.toString(16)):a+=o;return a}function o(){return a(16)}function i(){return a(32)}function a(t){function e(){return n?15&n[r++]:16*Math.random()|0}var n=null,r=0,o=window.crypto||window.msCrypto;o&&o.getRandomValues&&Uint8Array&&(n=o.getRandomValues(new Uint8Array(31)));for(var i=[],a=0;a<t;a++)i.push(e().toString(16));return i.join("")}e.exports={generateUuid:r,generateSpanId:o,generateTraceId:i}},{}],27:[function(t,e,n){function r(t,e){if(!o)return!1;if(t!==o)return!1;if(!e)return!0;if(!i)return!1;for(var n=i.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var s=navigator.userAgent,c=s.match(a);c&&s.indexOf("Chrome")===-1&&s.indexOf("Chromium")===-1&&(o="Safari",i=c[1])}e.exports={agent:o,version:i,match:r}},{}],28:[function(t,e,n){function r(t){function e(){t(a&&document[a]?document[a]:document[o]?"hidden":"visible")}"addEventListener"in document&&i&&document.addEventListener(i,e,!1)}e.exports=r;var o,i,a;"undefined"!=typeof document.hidden?(o="hidden",i="visibilitychange",a="visibilityState"):"undefined"!=typeof document.msHidden?(o="msHidden",i="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(o="webkitHidden",i="webkitvisibilitychange",a="webkitVisibilityState")},{}],29:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],30:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],31:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?f(t,c,a):a()}function n(n,r,o,i,a){if(a!==!1&&(a=!0),!l.aborted||i){t&&a&&t(n,r,o);for(var s=e(o),c=m(n),f=c.length,u=0;u<f;u++)c[u].apply(s,r);var p=d[y[n]];return p&&p.push([x,n,r,s]),s}}function i(t,e){g[t]=m(t).concat(e)}function h(t,e){var n=g[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return g[t]||[]}function v(t){return p[t]=p[t]||o(n)}function w(t,e){l.aborted||u(t,function(t,n){e=e||"feature",y[n]=e,e in d||(d[e]=[])})}var g={},y={},x={on:i,addEventListener:i,removeEventListener:h,emit:n,get:v,listeners:m,context:e,buffer:w,abort:s,aborted:!1};return x}function i(t){return f(t,c,a)}function a(){return new r}function s(){(d.api||d.feature)&&(l.aborted=!0,d=l.backlog={})}var c="nr@context",f=t("gos"),u=t(29),d={},p={},l=e.exports=o();e.exports.getOrSetContext=i,l.backlog=d},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!S++){var t=O.info=NREUM.info,e=m.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return f.abort();c(E,function(e,n){t[e]||(t[e]=n)});var n=a();s("mark",["onload",n+O.offset],null,"api"),s("timing",["load",n]);var r=m.createElement("script");0===t.agent.indexOf("http://")||0===t.agent.indexOf("https://")?r.src=t.agent:r.src=l+"://"+t.agent,e.parentNode.insertBefore(r,e)}}function o(){"complete"===m.readyState&&i()}function i(){s("mark",["domContent",a()+O.offset],null,"api")}var a=t(23),s=t("handle"),c=t(29),f=t("ee"),u=t(27),d=t(24),p=t(20),l=p.getConfiguration("ssl")===!1?"http":"https",h=window,m=h.document,v="addEventListener",w="attachEvent",g=h.XMLHttpRequest,y=g&&g.prototype,x=!d(h.location);NREUM.o={ST:setTimeout,SI:h.setImmediate,CT:clearTimeout,XHR:g,REQ:h.Request,EV:h.Event,PR:h.Promise,MO:h.MutationObserver};var b=""+location,E={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-spa-1210.min.js"},R=g&&y&&y[v]&&!/CriOS/.test(navigator.userAgent),O=e.exports={offset:a.getLastTimestamp(),now:a,origin:b,features:{},xhrWrappable:R,userAgent:u,disabled:x};if(!x){t(19),t(25),m[v]?(m[v]("DOMContentLoaded",i,!1),h[v]("load",r,!1)):(m[w]("onreadystatechange",o),h[w]("onload",r)),s("mark",["firstbyte",a.getLastTimestamp()],null,"api");var S=0}},{}],"wrap-function":[function(t,e,n){function r(t,e){function n(e,n,r,c,f){function nrWrapper(){var i,a,u,p;try{a=this,i=d(arguments),u="function"==typeof r?r(i,a):r||{}}catch(l){o([l,"",[i,a,c],u],t)}s(n+"start",[i,a,c],u,f);try{return p=e.apply(a,i)}catch(h){throw s(n+"err",[i,a,h],u,f),h}finally{s(n+"end",[i,a,p],u,f)}}return a(e)?e:(n||(n=""),nrWrapper[p]=e,i(e,nrWrapper,t),nrWrapper)}function r(t,e,r,o,i){r||(r="");var s,c,f,u="-"===r.charAt(0);for(f=0;f<e.length;f++)c=e[f],s=t[c],a(s)||(t[c]=n(s,u?c+r:r,o,c,i))}function s(n,r,i,a){if(!h||e){var s=h;h=!0;try{t.emit(n,r,i,e,a)}catch(c){o([c,n,r,i],t)}h=s}}return t||(t=u),n.inPlace=r,n.flag=p,n}function o(t,e){e||(e=u);try{e.emit("internal-error",t)}catch(n){}}function i(t,e,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(t);return r.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(i){o([i],n)}for(var a in t)l.call(t,a)&&(e[a]=t[a]);return e}function a(t){return!(t&&t instanceof Function&&t.apply&&!t[p])}function s(t,e){var n=e(t);return n[p]=t,i(t,n,u),n}function c(t,e,n){var r=t[e];t[e]=s(r,n)}function f(){for(var t=arguments.length,e=new Array(t),n=0;n<t;++n)e[n]=arguments[n];return e}var u=t("ee"),d=t(30),p="nr@original",l=Object.prototype.hasOwnProperty,h=!1;e.exports=r,e.exports.wrapFunction=s,e.exports.wrapInPlace=c,e.exports.argsToArray=f},{}]},{},["loader",2,16,5,3,4]);</script><script>performanceMarker("stylesheets_done_blocking");</script>

	<!-- moveTrackingToTop: false -->
        <script>
    window.MECSplitGaCustomDimensions = {"41":"moveTrackingToTop_CD41.off","42":"enableCheckoutCTATesting_HI-11468.on","43":"hi-12314-guest-checkout-flag.off","45":"enableRichRelevance_HI-11421.on","46":"pdpExpressDeliveryMessageAbTest.on"};
    window.MECSplitUserId = "24e7e289-5ed3-40ce-a944-f3528630cc43";
</script>


<script>
	dataLayer = [{"event":"ee prod details","vpv":"pages/product/productLayoutPage","ecommerce":{"detail":{"products":[{"name":"Patagonia Quandary Pants - Women's","id":"5050-315","price":99.0,"brand":"Patagonia","category":"camping and hiking/hiking clothing/hiking pants/(not set)/","dimension5":"844-320-300-300","variant":"5050-315","url":"https://www.mec.ca/en/product/5050-315/Quandary-Pants","localizedName":"Patagonia Quandary Pants - Women's","representativeSku":"596342","availableDeliveryOption":"dth-or-spu"}]}},"pageCategory":"productLayoutPage","locale":"en","loggedIn":false,"product":{"id":"5050-315","erpCategory":"844-320-300-300","webCategory":[{"id":"/products/camping-and-hiking/hiking-clothing/hiking-pants/c/1008","name":"Hiking pants"},{"id":"/products/clothing/bottoms/pants/trousers/c/1009","name":"Trousers"}],"idealFor":["Camping and hiking"],"name":{"en":"Quandary Pants","fr":"Pantalon Quandary"},"gender":"Women's","maxPrice":99.0,"minPrice":99.0,"availability":true,"archived":false,"badge":"none","averageRating":4.625}}];
</script><!-- Google Tag Manager -->
	<script>
				(function(w, d, s, l, i) {
					w[l] = w[l] || [];
					w[l].push({
						'gtm.start' : new Date().getTime(),
						event : 'gtm.js'
					});
					var f = d.getElementsByTagName(s)[0], j = d.createElement(s), dl = l != 'dataLayer' ? '&l='
							+ l
							: '';
					j.async = true;
					j.src = '//www.googletagmanager.com/gtm.js?id=' + i + dl;
					f.parentNode.insertBefore(j, f);
				})(window, document, 'script', 'dataLayer', 'GTM-WJ9Q4S');
			</script>
		<!-- End Google Tag Manager -->






    <script type="text/javascript">
        (function(){
            try {
                var treatmentConfigJson = JSON.parse('{"hotjarId":""}'),
                    hotjarId = treatmentConfigJson["hotjarId"];

                if (hotjarId) {
                    (function(h,o,t,j,a,r){
                        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
                        h._hjSettings={hjid:hotjarId,hjsv:6};
                        a=o.getElementsByTagName('head')[0];
                        r=o.createElement('script');r.async=1;
                        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
                        a.appendChild(r);
                    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
                }
            } catch (e) {
            }
        }())
    </script>

<script src="https://do9m2ht361ti1.cloudfront.net/_ui/static/jquery-2.1.4.js"></script>
		<script>performanceMarker("scripts_done_blocking");</script>


	<script type="application/ld+json">{"name":"Patagonia Quandary Pants - Women's","productID":"5050-315","url":"https://www.mec.ca/en/product/5050-315/Quandary-Pants","image":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg","description":"On the trail, on your bike, on the street – these light, tough pants are everything you need for summer action. The breathable stretch fabric moves with you, so you’re always comfortable and in good company.","category":"Hiking pants","brand":{"name":"Patagonia","@type":"Organization"},"aggregateRating":{"ratingValue":"4.6","reviewCount":"8","@type":"AggregateRating"},"offers":[{"sku":"549596","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"549597","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"549598","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"549599","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"549600","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"549601","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"549602","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"596342","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"826202","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595914","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595915","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595916","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595917","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595918","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595919","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"595920","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"596345","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"},{"sku":"826238","priceCurrency":"CAD","price":"99.00","image":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","itemCondition":"http://schema.org/NewCondition","availability":"http://schema.org/InStock","seller":{"name":"MEC","@type":"Organization"},"@type":"Offer"}],"additionalProperty":[{"name":"Weight","value":"275g (8)","@type":"PropertyValue"},{"name":"Ideal for","value":"Camping and hiking","@type":"PropertyValue"},{"name":"Fabric weight","value":"119gsm","@type":"PropertyValue"},{"name":"Fabric content","value":"62% recycled nylon 32% nylon 6% spandex","@type":"PropertyValue"},{"name":"Pockets","value":"2 front slash 1 back 1 back zippered 1 side zippered ","@type":"PropertyValue"},{"name":"Finished inseam","value":"32in. (8)","@type":"PropertyValue"},{"name":"Antimicrobial treatment","value":"No","@type":"PropertyValue"},{"name":"Additional feature(s)","value":"Gusseted crotch Converts to capris","@type":"PropertyValue"},{"name":"UPF rating","value":"40-50+ (Blocks ~97.5% of UVA/UVB)","@type":"PropertyValue"},{"name":"Made in","value":"Vietnam","@type":"PropertyValue"}],"@context":"http://schema.org/","@type":"Product"}</script>


	<script type="application/ld+json">{"itemListElement":[{"position":"1","item":{"name":"All","@id":"https://www.mec.ca/en/products/c/100"},"@type":"ListItem"},{"position":"2","item":{"name":"Camping and hiking","@id":"https://www.mec.ca/en/products/camping-and-hiking/c/1549"},"@type":"ListItem"},{"position":"3","item":{"name":"Hiking clothing","@id":"https://www.mec.ca/en/products/camping-and-hiking/hiking-clothing/c/604"},"@type":"ListItem"},{"position":"4","item":{"name":"Hiking pants","@id":"https://www.mec.ca/en/products/camping-and-hiking/hiking-clothing/hiking-pants/c/1008"},"@type":"ListItem"},{"position":"5","item":{"name":"Quandary Pants","@id":"https://www.mec.ca/en/product/5050-315/Quandary-Pants"},"@type":"ListItem"}],"@type":"BreadcrumbList","@context":"http://schema.org"}</script>







            <script src="//cdn.mec.ca/rrserver/js/1.2/p13n.js"></script>




</head>

<body id="page" class="page-productDetails pageType-ProductPage template-pages-product-productLayoutPage  smartedit-page-uid-productDetails smartedit-page-uuid-eyJpdGVtSWQiOiJwcm9kdWN0RGV0YWlscyIsImNhdGFsb2dJZCI6Im1lY0NvbnRlbnRDYXRhbG9nIiwiY2F0YWxvZ1ZlcnNpb24iOiJPbmxpbmUifQ== smartedit-catalog-version-uuid-mecContentCatalog/Online  language-en  f-hideCompareMobileOnly--off " data-currency-iso-code="CAD">


    <!-- Google Tag Manager (noscript) -->



			<noscript>
			    <iframe src="//www.googletagmanager.com/ns.html?id=GTM-WJ9Q4S"
			        height="0" width="0" style="display: none; visibility: hidden"></iframe>
			</noscript>


	<!-- End Google Tag Manager (noscript) -->

<div class="js-offcanvas-header">
    <span id="top"></span>
    <!-- Top-Banner -->
    <div class="top-banner js-offcanvas-offset-banner">



























<a href="#main-content" class="link--skip-to-content link--skip-to-content--inverse" data-skiplink="#main-content">Skip to content</a>
    <a href="#navigation" class="link--skip-to-content link--skip-to-content--inverse" data-skiplink="#navigation">Skip to navigation</a>
    <div class="top-banner__container container">
            <div class="top-banner__content">
                <script type="application/javascript">
    window.headerCarouselMessages = [{"message":"Extended store hours: see open hours at your local MEC","url":"en/stores"},{"message":"Have outdoor expertise to share? We’re hiring.","url":"https://www.mec.ca/en/explore/careers"},{"message":"Free store pickup available at all stores.","url":"/en/explore/in-store-pickup"},{"message":"Free shipping on orders over $50.","url":"/en/explore/shipping-info"}];
</script>

<div class="top-banner__message-list js-top-banner__message-list">
    <div
        class="js-react-component"
        data-mec-react-component="MessageCarousel"
    >
    </div>
        <a
                class="sr-only top-banner__sr-message"
                href="en/stores"
            >
                Extended store hours: see open hours at your local MEC<i class="label-icon icon-angle-right icon-large"></i>
            </a>
        <a
                class="sr-only top-banner__sr-message"
                href="https://www.mec.ca/en/explore/careers"
            >
                Have outdoor expertise to share? We’re hiring.<i class="label-icon icon-angle-right icon-large"></i>
            </a>
        <a
                class="sr-only top-banner__sr-message"
                href="/en/explore/in-store-pickup"
            >
                Free store pickup available at all stores.<i class="label-icon icon-angle-right icon-large"></i>
            </a>
        <a
                class="sr-only top-banner__sr-message"
                href="/en/explore/shipping-info"
            >
                Free shipping on orders over $50.<i class="label-icon icon-angle-right icon-large"></i>
            </a>
        </div>
<div class="language language--header">
                    <span class="language__label sr-only" for="lang-selector">Change language</span>
	<div class="language__toggle">
		<a href="https://www.mec.ca/fr/product/5050-315/Pantalon-Quandary" id="lang-selector" class="language__link btn-xs btn-link js-offcanvas-link" data-mec-uet-category='mega-menu-v2-meta' data-mec-uet-action='fr'>Français</a>
					</div>
</div>
            </div>
        </div>
    </div><!-- Sticky Header -->
<div data-sticky="base" class="js-offcanvas-header-sticky qa-header" data-sticky-transition data-sticky-transition-height="60" data-sticky-placement="top">
    <header class="header is-at-top js-header">
        <div class="header__container container">

            <!-- MEC 50th Anniversary Logo -->
                    <a href="/en/" class="header__logo anniversary" aria-label="MEC 50th logo">
                        <?xml version="1.0" encoding="utf-8"?>
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 300 205.75" style="enable-background:new 0 0 300 205.75;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#FFFFFF;}
	.st1{fill:#16A94A;}
</style>
<path class="st0" d="M226.55,1.69c-42.92-4.13-74.12,26.44-81.66,77.54c-12.38-18.26-33.3-23.24-53.33-23.24
	c-9.35,0-18.09,1.87-25.8,4.8l2.17-12.58h66.91c4.83,0,7.52-2.53,7.52-7.09V10.23c0-4.56-2.69-7.09-7.52-7.09h-98.9
	c-4.57,0-7.52,2.02-8.06,6.33l-9.4,88.74c-1.34,11.13,16.92,17.97,27.67,9.36c8.33-6.83,17.43-14.6,27.1-14.6
	c18,0,23.09,9.46,22.58,31.36c-0.64,27.83-20.2,30.98-27.36,25.73c-16.11-11.81-6.47-34.27-34.14-34.27
	C21.7,115.79,8,121.86,8,139.58c0,25.56,26.86,45.76,70.11,45.76c1.35,0,2.68-0.02,4.01-0.07L212.76,48.44l9.87,27.95l34.35-45.83
	v140.86c18.29-13.97,31.74-37.82,34.81-69.78C297.14,46.06,267.99,5.68,226.55,1.69z"/>
<g>
	<polyline class="st1" points="233.58,205.75 120.29,205.75 120.29,92.45 233.58,92.45 	"/>
	<g>
		<polygon class="st0" points="172.61,169.51 192.65,169.51 192.65,162.51 180.42,162.51 180.42,151.52 190.63,151.52
			190.63,144.52 180.42,144.52 180.42,134.54 192.65,134.54 192.65,127.54 172.61,127.54 		"/>
		<path class="st0" d="M220.43,142.67v-5.1c0-6.3-3.91-10.96-11.34-10.96c-7.5,0-12.1,5.04-12.1,11.53v20.79
			c0,6.49,4.6,11.53,12.1,11.53c7.43,0,11.34-4.66,11.34-10.96v-5.1h-6.99v5.04c0,2.46-1.39,4.16-4.22,4.16
			c-2.84,0-4.28-1.7-4.28-4.03V137.5c0-2.33,1.45-4.03,4.28-4.03c2.84,0,4.22,1.7,4.22,4.16v5.04H220.43z"/>
		<polygon class="st0" points="156.31,127.54 151.96,148.84 150.64,156.59 149.32,148.84 144.97,127.54 134.45,127.54
			134.45,169.51 141.44,169.51 141.44,139.08 143.08,148.21 147.3,169.51 153.98,169.51 158.2,148.21 159.84,139.08 159.84,169.51
			166.84,169.51 166.84,127.54 		"/>
	</g>
</g>
</svg>
</a>
                <div class="header__content">
                <div class="header__row">
                    <!-- WCMS-driven Utilities Menu -->
                    <!-- Search Box -->
<div class="header__search js-search-box">
    <div class="header__search__inner js-search-box__panel">
        <div class="js-react-component header__search-container" data-mec-react-component="Search">
            <div class="header__search__placeholder"></div>
        </div>
    </div>
</div>
<div class="my-store__container js-react-component" data-mec-react-component="MyStore"></div>
                        <div class="js-react-component" data-mec-react-component="HeaderSetStoreModal"></div>
                    <nav role="navigation" class="nav-utility js-utility-menu" data-module="UtilityMenu">
                        <ul class="nav-utility__list js-menu js-offcanvas-checkout">
                            <li class="nav-utility__item nav-utility__item--search">
                                    <button class="js-search-trigger nav-button nav-button--utility" id="search-button" aria-labelledby="search-label" aria-controls="search-form-panel" aria-expanded="false">
                                        <label id="search-label" for="search-button" class="nav-utility__label">
                                            Toggle search</label>
                                        <div class="nav-utility__icon nav-utility__icon--search">
                                            <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.7481 12.5273L11.136 9.91519C10.7863 9.56548 10.7538 9.01625 10.9846 8.57882C12.1495 6.37061 11.8026 3.54659 9.96483 1.70879C8.86211 0.607506 7.39661 0 5.83753 0C4.27702 0 2.81152 0.607506 1.71023 1.71023C0.607506 2.81296 0 4.27846 0 5.83753C0 7.39661 0.607506 8.86211 1.71023 9.96483C2.81296 11.0676 4.27846 11.6751 5.83753 11.6751C6.80668 11.6751 7.74444 11.4375 8.57983 10.9912C9.01728 10.7574 9.56828 10.7889 9.91908 11.1396L12.5273 13.7466C12.69 13.9093 12.9074 14 13.1377 14C13.3695 14 13.5854 13.9093 13.7466 13.7481C13.9093 13.5854 14 13.368 14 13.1377C14 12.9074 13.9107 12.69 13.7481 12.5273ZM5.83753 1.72607C6.93594 1.72607 7.96812 2.15362 8.7455 2.931C9.52144 3.7055 9.94756 4.73913 9.94756 5.83753C9.94756 6.93594 9.52 7.96956 8.7455 8.7455C7.96956 9.52144 6.93594 9.95044 5.83897 9.95044C4.74057 9.95044 3.70838 9.52288 2.931 8.7455C2.15506 7.96956 1.72607 6.93738 1.72607 5.83753C1.72607 4.73913 2.15362 3.70694 2.931 2.931C3.70694 2.15362 4.73913 1.72607 5.83753 1.72607Z" fill="white"/>
</svg></div>
                                        <span class="nav-utility__label" for="search-button">Search</span>
                                    </button>
                                </li>


















<li class="nav-utility__item nav-utility__item--account fly-menu js-fly-menu" aria-controls="menu-account-popover" aria-haspopup="true">
    <button class="nav-button nav-button--utility fly-menu__trigger qa-menu__my-account  js-fly-menu__trigger" aria-pressed="false" data-mec-uet-category='mega-menu-v2-meta' data-mec-uet-action='account'>
        <div class="nav-utility__icon nav-utility__icon--account">
            <svg width="13" height="14" viewBox="0 0 13 14" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M6.5 6.9375C5.86719 6.9375 5.31348 6.80566 4.78613 6.48926C4.25879 6.19922 3.86328 5.80371 3.57324 5.27637C3.25684 4.74902 3.125 4.19531 3.125 3.5625C3.125 2.95605 3.25684 2.40234 3.57324 1.875C3.86328 1.34766 4.25879 0.952148 4.78613 0.635742C5.31348 0.345703 5.86719 0.1875 6.5 0.1875C7.10645 0.1875 7.66016 0.345703 8.1875 0.635742C8.71484 0.952148 9.11035 1.34766 9.42676 1.875C9.7168 2.40234 9.875 2.95605 9.875 3.5625C9.875 4.19531 9.7168 4.74902 9.42676 5.27637C9.11035 5.80371 8.71484 6.19922 8.1875 6.48926C7.66016 6.80566 7.10645 6.9375 6.5 6.9375ZM8.87305 7.78125C9.50586 7.78125 10.0859 7.93945 10.6396 8.25586C11.167 8.57227 11.6152 9.02051 11.9316 9.54785C12.248 10.1016 12.4062 10.6816 12.4062 11.3145V12.4219C12.4062 12.791 12.2744 13.0811 12.0371 13.3184C11.7734 13.582 11.4834 13.6875 11.1406 13.6875H1.85938C1.49023 13.6875 1.2002 13.582 0.962891 13.3184C0.699219 13.0811 0.59375 12.791 0.59375 12.4219V11.3145C0.59375 10.6816 0.751953 10.1016 1.06836 9.54785C1.38477 9.02051 1.80664 8.57227 2.36035 8.25586C2.8877 7.93945 3.49414 7.78125 4.12695 7.78125H4.5752C5.18164 8.07129 5.81445 8.20312 6.5 8.20312C7.15918 8.20312 7.79199 8.07129 8.4248 7.78125H8.87305Z" fill="white"/>
</svg>
        </div>
        <span class="nav-utility__label">
            Account
        </span>
        <div class="nav-utility__icon nav-utility__icon--angle-down">
            <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
    <mask id="path-1-inside-1" fill="white">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M9.49497 0.505013C9.76834 0.77838 9.76834 1.2216 9.49497 1.49496L5.49497 5.49496C5.22161 5.76833 4.77839 5.76833 4.50502 5.49496L0.505025 1.49496C0.231657 1.2216 0.231657 0.77838 0.505025 0.505013C0.778392 0.231646 1.22161 0.231646 1.49497 0.505013L5 4.01004L8.50502 0.505013C8.77839 0.231646 9.22161 0.231646 9.49497 0.505013Z"/>
    </mask>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M9.49497 0.505013C9.76834 0.77838 9.76834 1.2216 9.49497 1.49496L5.49497 5.49496C5.22161 5.76833 4.77839 5.76833 4.50502 5.49496L0.505025 1.49496C0.231657 1.2216 0.231657 0.77838 0.505025 0.505013C0.778392 0.231646 1.22161 0.231646 1.49497 0.505013L5 4.01004L8.50502 0.505013C8.77839 0.231646 9.22161 0.231646 9.49497 0.505013Z" fill="#191919"/>
    <path d="M9.49497 1.49496L8.50502 0.505013L8.50502 0.505013L9.49497 1.49496ZM5.49497 5.49496L6.48492 6.48491L6.48492 6.48491L5.49497 5.49496ZM4.50502 5.49496L5.49497 4.50501L5.49497 4.50501L4.50502 5.49496ZM0.505025 1.49496L-0.484925 2.48491L-0.484925 2.48491L0.505025 1.49496ZM1.49497 0.505013L2.48492 -0.484936L2.48492 -0.484936L1.49497 0.505013ZM5 4.01004L4.01005 4.99999L5 5.98994L5.98995 4.99999L5 4.01004ZM8.50502 0.505013L9.49497 1.49496L9.49497 1.49496L8.50502 0.505013ZM10.4849 2.48491C11.305 1.66481 11.305 0.335165 10.4849 -0.484936L8.50502 1.49496C8.23166 1.2216 8.23166 0.77838 8.50502 0.505013L10.4849 2.48491ZM6.48492 6.48491L10.4849 2.48491L8.50502 0.505013L4.50502 4.50501L6.48492 6.48491ZM3.51508 6.48491C4.33518 7.30501 5.66482 7.30501 6.48492 6.48491L4.50502 4.50501C4.77839 4.23164 5.22161 4.23165 5.49497 4.50501L3.51508 6.48491ZM-0.484925 2.48491L3.51508 6.48491L5.49497 4.50501L1.49497 0.505013L-0.484925 2.48491ZM-0.484925 -0.484936C-1.30503 0.335165 -1.30503 1.66481 -0.484925 2.48491L1.49497 0.505013C1.76834 0.77838 1.76834 1.2216 1.49497 1.49496L-0.484925 -0.484936ZM2.48492 -0.484936C1.66482 -1.30504 0.335176 -1.30504 -0.484925 -0.484936L1.49497 1.49496C1.22161 1.76833 0.778391 1.76833 0.505024 1.49496L2.48492 -0.484936ZM5.98995 3.02009L2.48492 -0.484936L0.505024 1.49496L4.01005 4.99999L5.98995 3.02009ZM7.51508 -0.484936L4.01005 3.02009L5.98995 4.99999L9.49497 1.49496L7.51508 -0.484936ZM10.4849 -0.484936C9.66482 -1.30504 8.33518 -1.30504 7.51508 -0.484936L9.49497 1.49496C9.22161 1.76833 8.77839 1.76833 8.50502 1.49496L10.4849 -0.484936Z" fill="white" mask="url(#path-1-inside-1)"/>
</svg>
        </div>
    </button>
    <div class="js-react-component fly-menu__body js-fly-menu__body qa-account-menu__container nav-utility__account-fly-menu" aria-expanded="false" id="menu-account-popover"
            data-mec-react-component="AccountMenu"
            data-mec-react-data='{
                "outage": false
            }'>
    </div>
</li>












    <li class="nav-utility__item nav-utility__item--wishlist">
        <a href="/en/wishlist" class="nav-button nav-button--utility qa-menu__wishlist js-offcanvas-link" title="Wishlist" data-mec-uet-category='mega-menu-v2-meta' data-mec-uet-action='wishlist'>
            <div class="nav-utility__icon nav-utility__icon--wishlist">
                <svg width="15" height="13" viewBox="0 0 15 13" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M13.1328 1.47266C13.6797 1.96484 14.0898 2.53906 14.3086 3.22266C14.5273 3.93359 14.5547 4.61719 14.3906 5.32812C14.2266 6.03906 13.8984 6.64062 13.4062 7.13281L8.12891 12.6016C7.9375 12.793 7.71875 12.875 7.5 12.875C7.25391 12.875 7.03516 12.793 6.87109 12.6016L1.59375 7.16016C1.07422 6.64062 0.746094 6.03906 0.582031 5.32812C0.417969 4.61719 0.472656 3.93359 0.691406 3.22266C0.910156 2.53906 1.29297 1.96484 1.86719 1.47266C2.35938 1.0625 2.90625 0.789062 3.53516 0.679688C4.13672 0.570312 4.76562 0.625 5.36719 0.816406C5.96875 1.03516 6.48828 1.36328 6.95312 1.82812L7.5 2.375L8.04688 1.82812C8.48438 1.36328 9.03125 1.03516 9.63281 0.816406C10.2344 0.625 10.8359 0.570312 11.4648 0.679688C12.0664 0.789062 12.6406 1.0625 13.1328 1.47266Z" fill="white"/>
</svg>
            </div>
            <span class="nav-utility__label">Wishlist</span>
        </a>
    </li>



























<li class="nav-utility__item nav-utility__item--help fly-menu js-fly-menu" aria-controls="menu-help-fly-menu" aria-haspopup="true">
    <button class="nav-button nav-button--utility qa-menu__help fly-menu__trigger js-fly-menu__trigger" data-mec-uet-category='mega-menu-v2-meta' data-mec-uet-action='help' aria-pressed="false">
        <div class="nav-utility__icon nav-tility__icon--help">
            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M7.49042 0C3.35249 0 0 3.35249 0 7.49042C0 11.6284 3.35249 14.9808 7.49042 14.9808C11.6284 14.9808 14.9808 11.6284 14.9808 7.49042C15 3.35249 11.6475 0 7.49042 0ZM7.29885 11.6858C6.80077 11.6858 6.41762 11.3027 6.41762 10.8238C6.41762 10.2874 6.78161 9.90421 7.29885 9.90421C7.81609 9.88506 8.21839 10.2874 8.21839 10.8046C8.21839 11.3027 7.83525 11.6858 7.29885 11.6858ZM9.65517 7.43295C9.38697 7.66283 9.11877 7.87356 8.83142 8.06513C8.40996 8.35249 8.16092 8.7931 8.16092 9.36782C7.60536 9.36782 7.01149 9.36782 6.43678 9.36782C6.36015 8.75479 6.39847 8.06513 6.95402 7.62452C7.27969 7.37548 7.62452 7.16475 7.89272 6.89655C8.14176 6.62835 8.3908 6.30268 8.50575 5.97701C8.63985 5.55556 8.31418 5.05747 7.95019 4.92337C7.41379 4.7318 6.76245 4.88506 6.53257 5.32567C6.39847 5.57471 6.30268 5.86207 6.30268 6.18774C5.76628 6.18774 5.1341 6.18774 4.5977 6.18774C4.42529 5.32567 4.90421 4.27203 5.70881 3.75479C6.81992 3.06513 8.71647 3.21839 9.69349 4.09962C10.6705 4.96169 10.6513 6.57088 9.65517 7.43295Z" fill="white"/>
</svg>
        </div>
        <span class="nav-utility__label">Help</span>
        <div class="nav-utility__icon nav-utility__icon--angle-down">
            <svg width="10" height="6" viewBox="0 0 10 6" fill="none" xmlns="http://www.w3.org/2000/svg">
    <mask id="path-1-inside-1" fill="white">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M9.49497 0.505013C9.76834 0.77838 9.76834 1.2216 9.49497 1.49496L5.49497 5.49496C5.22161 5.76833 4.77839 5.76833 4.50502 5.49496L0.505025 1.49496C0.231657 1.2216 0.231657 0.77838 0.505025 0.505013C0.778392 0.231646 1.22161 0.231646 1.49497 0.505013L5 4.01004L8.50502 0.505013C8.77839 0.231646 9.22161 0.231646 9.49497 0.505013Z"/>
    </mask>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M9.49497 0.505013C9.76834 0.77838 9.76834 1.2216 9.49497 1.49496L5.49497 5.49496C5.22161 5.76833 4.77839 5.76833 4.50502 5.49496L0.505025 1.49496C0.231657 1.2216 0.231657 0.77838 0.505025 0.505013C0.778392 0.231646 1.22161 0.231646 1.49497 0.505013L5 4.01004L8.50502 0.505013C8.77839 0.231646 9.22161 0.231646 9.49497 0.505013Z" fill="#191919"/>
    <path d="M9.49497 1.49496L8.50502 0.505013L8.50502 0.505013L9.49497 1.49496ZM5.49497 5.49496L6.48492 6.48491L6.48492 6.48491L5.49497 5.49496ZM4.50502 5.49496L5.49497 4.50501L5.49497 4.50501L4.50502 5.49496ZM0.505025 1.49496L-0.484925 2.48491L-0.484925 2.48491L0.505025 1.49496ZM1.49497 0.505013L2.48492 -0.484936L2.48492 -0.484936L1.49497 0.505013ZM5 4.01004L4.01005 4.99999L5 5.98994L5.98995 4.99999L5 4.01004ZM8.50502 0.505013L9.49497 1.49496L9.49497 1.49496L8.50502 0.505013ZM10.4849 2.48491C11.305 1.66481 11.305 0.335165 10.4849 -0.484936L8.50502 1.49496C8.23166 1.2216 8.23166 0.77838 8.50502 0.505013L10.4849 2.48491ZM6.48492 6.48491L10.4849 2.48491L8.50502 0.505013L4.50502 4.50501L6.48492 6.48491ZM3.51508 6.48491C4.33518 7.30501 5.66482 7.30501 6.48492 6.48491L4.50502 4.50501C4.77839 4.23164 5.22161 4.23165 5.49497 4.50501L3.51508 6.48491ZM-0.484925 2.48491L3.51508 6.48491L5.49497 4.50501L1.49497 0.505013L-0.484925 2.48491ZM-0.484925 -0.484936C-1.30503 0.335165 -1.30503 1.66481 -0.484925 2.48491L1.49497 0.505013C1.76834 0.77838 1.76834 1.2216 1.49497 1.49496L-0.484925 -0.484936ZM2.48492 -0.484936C1.66482 -1.30504 0.335176 -1.30504 -0.484925 -0.484936L1.49497 1.49496C1.22161 1.76833 0.778391 1.76833 0.505024 1.49496L2.48492 -0.484936ZM5.98995 3.02009L2.48492 -0.484936L0.505024 1.49496L4.01005 4.99999L5.98995 3.02009ZM7.51508 -0.484936L4.01005 3.02009L5.98995 4.99999L9.49497 1.49496L7.51508 -0.484936ZM10.4849 -0.484936C9.66482 -1.30504 8.33518 -1.30504 7.51508 -0.484936L9.49497 1.49496C9.22161 1.76833 8.77839 1.76833 8.50502 1.49496L10.4849 -0.484936Z" fill="white" mask="url(#path-1-inside-1)"/>
</svg>
        </div>
    </button>
    <div class="pop-panel fly-menu__body js-fly-menu__body nav-utility__help-fly-menu" id="menu-help-fly-menu" aria-expanded="false">

	        <div class="js-livechat-init hidden">
	            <a href="#" class="u-no-decoration qa-help-tab__livechat-anchor fly-menu__link js-offcanvas-link">
	                <h5 class="u-no-margin fly-menu__heading">
	                    <svg class="livechat-svg" viewBox="0 0 28 28"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g fill="#000000">
    <path d="M14,25.5 C12.4,25.5 10.8,25.2 9.4,24.7 L4.5,27.5 L4.5,21.9 C2,19.6 0.5,16.5 0.5,13 C0.5,6.1 6.5,0.5 14,0.5 C21.5,0.5 27.5,6.1 27.5,13 C27.5,19.9 21.5,25.5 14,25.5 L14,25.5 Z M9,11.5 C8.2,11.5 7.5,12.2 7.5,13 C7.5,13.8 8.2,14.5 9,14.5 C9.8,14.5 10.5,13.8 10.5,13 C10.5,12.2 9.8,11.5 9,11.5 L9,11.5 Z M14,11.5 C13.2,11.5 12.5,12.2 12.5,13 C12.5,13.8 13.2,14.5 14,14.5 C14.8,14.5 15.5,13.8 15.5,13 C15.5,12.2 14.8,11.5 14,11.5 L14,11.5 Z M19,11.5 C18.2,11.5 17.5,12.2 17.5,13 C17.5,13.8 18.2,14.5 19,14.5 C19.8,14.5 20.5,13.8 20.5,13 C20.5,12.2 19.8,11.5 19,11.5 L19,11.5 Z"></path>
</g></g></svg>
	                    Chat with us
	                </h5>
	            </a>
	            <hr class="divider divider--margin-sm" />
	        </div>

        <h5 class="u-no-margin fly-menu__heading">
        <a class="h5 fly-menu__link js-offcanvas-link" href="/explore/support/">Help Centre</a>
        </h5>
        <hr class="divider divider--margin-sm" />
        <ul class="list list--menu">
            <li class="list__item"><a class="list__link js-offcanvas-link" href="/en/explore/shipping-info/">Shipping info</a></li>
            <li class="list__item"><a class="list__link js-offcanvas-link" href="/en/explore/returns-and-guarantee/">Returns and guarantee</a></li>
            <li><hr class="divider divider--margin-sm" /></li>
            <li class="list__item"><a class="list__link js-offcanvas-link" href="/en/explore/contact-us/">Contact us</a></li>
        </ul>
    </div>
</li>



    <li class="nav-utility__item">
    <a href="/en/cart" class="nav-button nav-button--utility">
        <div class="nav-utility__icon nav-utility__icon--cart">
            <svg width="15" height="14" viewBox="0 0 15 14" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M14.5048 2.69444H3.78495L3.36164 0.40026C3.30873 0.128539 3.04582 0 2.72503 0H0.496061C0.221574 0 0 0.232672 0 0.579239C0 0.904653 0.261259 1.18614 0.535746 1.18614H2.35464L2.7333 3.25415C2.73495 3.27042 2.73826 3.28669 2.74156 3.30296L3.70723 8.53563C3.86597 9.38497 4.61833 10 5.49636 10H11.8162C12.6446 10 13.3688 9.45005 13.5772 8.66092L14.9844 3.30947C15.0521 3.04914 14.8934 2.7823 14.6288 2.71559C14.5892 2.70582 14.5478 2.70094 14.5048 2.69932V2.69444V2.69444Z" fill="white"/>
    <path d="M5.5 11C4.67141 11 4 11.6714 4 12.5C4 13.3286 4.67141 14 5.5 14C6.32859 14 7 13.3286 7 12.5C6.99847 11.6714 6.32859 11.0015 5.5 11Z" fill="white"/>
    <path d="M11.4985 11C10.6699 11.0015 9.99848 11.6729 10 12.5015C10.0015 13.3301 10.6729 14.0015 11.5015 14C12.3301 13.9985 13 13.3286 13 12.5C12.9985 11.6714 12.3271 11 11.4985 11Z" fill="white"/>
</svg></div>
        <span class="nav-utility__label">Cart</span>
            <span class="sr-only">Number of items in your cart:</span>
            <span class="badge badge--primary badge--count nav-utility__cart-badge sr-only js-header-cart-badge-count">0</span>
                </a>
</li>





<li class="nav-utility__item nav-utility__item--hamburger">
    <button class="nav-button nav-button--utility no-bounce js-icon-menu-button js-offcanvas-trigger qa-hamburger" id="menu-button" aria-labelledby="menu-label-open menu-label-close" data-offcanvas-cover="under" data-offcanvas-trigger="right">
        <div class="menu__item nav-utility__icon nav-utility__icon--hamburger">
            <svg width="18" height="7" viewBox="0 0 18 7" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M0 0.933333C0 0.417867 0.474051 0 1.05882 0H16.9412C17.5259 0 18 0.417867 18 0.933333C18 1.4488 17.5259 1.86667 16.9412 1.86667H1.05882C0.474051 1.86667 0 1.4488 0 0.933333ZM0 6.06667C0 5.5512 0.474051 5.13333 1.05882 5.13333H16.9412C17.5259 5.13333 18 5.5512 18 6.06667C18 6.58213 17.5259 7 16.9412 7H1.05882C0.474051 7 0 6.58213 0 6.06667Z" fill="white"/>
</svg>
        </div>
        <label id="menu-label-open" for="menu-button" class="nav-utility__label">
            Menu
        </label>
        <label id="menu-label-close" for="menu-button" class="menu__label menu__label--close is-hidden sr-only js-icon-menu-close-label">
            Close menu
        </label>
    </button>
</li>
</ul>
                    </nav>
                    <!-- Utilities Menu -->

                </div>
                <div class="header__row header__row--nav">
                    <nav
                                id="navigation-menu-primary"
                                class="js-react-component nav-primary"
                                aria-expanded="false"
                                data-mec-react-component="NavPrimary"
                                data-mec-react-data='{"location":"global"}'
                                >
                            </nav>
                        </div>
            </div>
        </div>
    </header>
    <nav
                id="navigation-menu-subnav"
                class="js-react-component nav-subnav"
                aria-expanded="false"
                data-mec-react-component="NavSubnav"
                data-mec-react-data='{"location":"global"}'>
            </nav>
            <nav
                id="navigation-menu-mega"
                class="js-react-component nav-meganav"
                aria-expanded="false"
                data-mec-react-component="NavMega"
                data-mec-react-data='{"location":"global"}'>
            </nav>
        </div>
</div>

<!-- Bottom header -->
<div class="breadcrumbs">
    <div class="container">
        <ul class="breadcrumbs__control">
            <li class="breadcrumbs__item">
                <a href="/en/" class="breadcrumbs__text">Home</a>
            </li>

            <li class="breadcrumbs__item">
                            <a class="breadcrumbs__text" href="/en/products/c/100">All</a>
                        </li>
                    <li class="breadcrumbs__item">
                            <a class="breadcrumbs__text" href="/en/products/camping-and-hiking/c/1549">Camping and hiking</a>
                        </li>
                    <li class="breadcrumbs__item">
                            <a class="breadcrumbs__text" href="/en/products/camping-and-hiking/hiking-clothing/c/604">Hiking clothing</a>
                        </li>
                    <li class="breadcrumbs__item">
                            <a class="breadcrumbs__text" href="/en/products/camping-and-hiking/hiking-clothing/hiking-pants/c/1008">Hiking pants</a>
                        </li>
                    <li class="breadcrumbs__item">
                            <span class="breadcrumbs__text"> Quandary Pants</span>
                        </li>
                    </ul>
    </div>
</div><div class="main-wrapper">
			<main id="main-content" class="main-wrapper__content js-guided-selling-modal" role="main">
				<div class="container">
					<div class="layout layout--rightup product-layout" data-product-id="5050-315">
        <div class="js-sticky-bottom sticky-bottom">
            <div class="btn-add-to-cart__container">
                        <div
                            class="js-react-component"
                            data-mec-react-component="AddToCartCta"
                            data-mec-react-data='{
                                "productCode": "5050-315",
                                "trackStickyInGa": true
                            }'
                        >
                        </div>
                    </div>
                </div>

        <div class="layout__main">























<div class="product__header hidden-md-min">

    <span class="product__name t-level-3 qa-product__name u-block">
        Patagonia Quandary Pants - Women's
    </span>












        <span class="sr-only"><spring:theme code="product.code" /></span>



                <span class="product__code text--subtle">5050-315</span>




</div>
<div id="primary_image">
                <div id="images" class="product__primary-image">
                    <!-- Image Gallery -->














































    <div class="carousel carousel--products js-carousel-products u-cursor--zoom-in is-initial-render" role="region" aria-label="Carousel of slides" data-carousel>


                <a href="#" role="button" class="carousel__nav carousel__nav--prev js-carousel-prev" aria-label="Previous slide">
                    <i class="carousel__icon icon-angle-left"></i>
                </a>
                <a href="#" role="button" class="carousel__nav carousel__nav--next js-carousel-next" aria-label="Next slide">
                    <i class="carousel__icon icon-angle-right"></i>
                </a>


        <div class="carousel__list owl-carousel js-carousel-slides">


                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="true" aria-hidden="true">










                    <div class="carousel__item item synced">


















<div class="srcset-image carousel__media">
    <img
        srcset="

                https://mec.imgix.net/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg?w=1200&h=1200&auto=format&q=60&fit=fill&bg=FFF 2x,

                https://mec.imgix.net/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg?w=600&h=600&auto=format&q=60&fit=fill&bg=FFF 1x,

        "


            data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg"



            src="https://mec.imgix.net/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg?w=600&h=600&auto=format&q=60&fit=fill&bg=FFF"







            class="srcset-image__content"



            alt="Quandary Pants Forge Grey"



            data-image-fit="fill"



            onload="performanceClearAndMark('pdp_image_rendered')"

    >


        <script>performanceClearAndMark("pdp_image_rendered");</script>

</div>







                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001898014/5050315-FRG00-ALT-BACK.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001963550/5050315-FRG00-ALT-BACK-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993002061854/5050315-FRG00-ALT-BACK-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001046046/5050315-FRG00-ALT-CAPRIS.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001111582/5050315-FRG00-ALT-CAPRIS-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993001209886/5050315-FRG00-ALT-CAPRIS-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001144350/5050315-FRG00-ALT-DETAIL.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001275422/5050315-FRG00-ALT-DETAIL-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993001340958/5050315-FRG00-ALT-DETAIL-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993002487838/5050315-FRG00-ALT-FLAT.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993002586142/5050315-FRG00-ALT-FLAT-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993002651678/5050315-FRG00-ALT-FLAT-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="SHA00" data-primary="true" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8941965344798/5050315-SHA00.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941966753822/5050315-SHA00-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8941967376414/5050315-SHA00-fallback.jpg"






                alt='Quandary Pants Shale'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

        </div>
    </div>



<div class="carousel__badge js-pdp-badge">
    <div
        class="js-react-component"
        data-mec-react-component="Badges"
        data-mec-react-data='{
            "productCode": "5050-315",
            "isLarge": true
        }'
    >
    </div>
</div>

<!-- Zoom button -->

    <a href="#" role="button" class="carousel__zoom-button js-zoom-control">
        <span class="sr-only">Press to open modal with high resolution version of current image</span>
        <i class="carousel__zoom-icon icon-resize-full" aria-hidden="true"></i>
    </a>






























    <div class="carousel carousel--thumbnails js-carousel-thumbnails is-initial-render" role="region" aria-label="Carousel of slides" data-carousel>

        <div class="carousel__list owl-carousel js-carousel-slides">


                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="true" aria-hidden="true">










                    <div class="carousel__item item synced">


















<div class="srcset-image carousel__media">
    <img
        srcset="

                https://mec.imgix.net/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg?w=1200&h=1200&auto=format&q=60&fit=fill&bg=FFF 2x,

                https://mec.imgix.net/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg?w=600&h=600&auto=format&q=60&fit=fill&bg=FFF 1x,

        "


            data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg"



            src="https://mec.imgix.net/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg?w=600&h=600&auto=format&q=60&fit=fill&bg=FFF"







            class="srcset-image__content"



            alt="Quandary Pants Forge Grey"



            data-image-fit="fill"



    >


</div>







                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001898014/5050315-FRG00-ALT-BACK.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001963550/5050315-FRG00-ALT-BACK-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993002061854/5050315-FRG00-ALT-BACK-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001046046/5050315-FRG00-ALT-CAPRIS.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001111582/5050315-FRG00-ALT-CAPRIS-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993001209886/5050315-FRG00-ALT-CAPRIS-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001144350/5050315-FRG00-ALT-DETAIL.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001275422/5050315-FRG00-ALT-DETAIL-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993001340958/5050315-FRG00-ALT-DETAIL-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="FRG00" data-primary="false" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993002487838/5050315-FRG00-ALT-FLAT.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993002586142/5050315-FRG00-ALT-FLAT-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993002651678/5050315-FRG00-ALT-FLAT-fallback.jpg"






                alt='Quandary Pants Forge Grey'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

                <div class="carousel__content js-carousel-content" data-colour="SHA00" data-primary="true" aria-hidden="true">









                    <div class="carousel__item item ">































<div class="carousel__media fluid-image fluid-image--1x1">



















<img

        data-high-res-src="https://cdn.mec.ca/medias/sys_master/high-res/high-res/8941965344798/5050315-SHA00.jpg"




        src="https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941966753822/5050315-SHA00-placeholder.jpg"




        data-fallback-src="https://cdn.mec.ca/medias/sys_master/fallback/fallback/8941967376414/5050315-SHA00-fallback.jpg"






                alt='Quandary Pants Shale'







        class="fluid-image__content "



        data-defer







        data-image-fit="fill"







>



</div>








                    </div>
                </div>

        </div>
    </div>




</div>
            </div>
        </div>

        <div class="layout__sidebar layout__sidebar--pdp js-layout-stick">
        	<div class="product__controls " id="ProductDetailControls">




















<div class="product__header visible-md-min">

    <h1 class="product__name t-level-3 qa-product__name">
        Patagonia Quandary Pants - Women's
    </h1>












        <span class="sr-only"><spring:theme code="product.code" /></span>



                <span class="product__code text--subtle">5050-315</span>




</div>










<div
    class="js-react-component"
    data-mec-react-component="ProductSideBarTop"
    data-mec-react-data='{
        "productCode": "5050-315"
    }'
></div>


    <div class="product__controls__component product__quantity">
        <label for="quantity-qtyInput"
    class="control-label product__controls__component__label">
    Quantity:</label>

<div class="input-group quantity-selector js-quantitySelector">
    <span class="input-group-btn">
        <button type="button" class="quantity-selector__button no-bounce js-decrease" aria-label="Decrease quantity by one">
            <i class="icon-minus quantity-selector__icon" aria-hidden="true"></i>
        </button>
    </span>
    <input type="text"
            name="quantity"
            id="quantity-qtyInput"
            class="quantity-selector__input js-quantity"
            maxlength="3"
            min="1"
            max="999"
            size="3"
            value="1"
            pattern="[0-9]*">
    <span class="input-group-btn">
        <button type="button" class="quantity-selector__button no-bounce js-increase" aria-label="Increase quantity by one">
            <i class="icon-plus quantity-selector__icon"></i>
        </button>
    </span>
</div>



    </div>






















        <div class="product__controls__component js-pdp-availability">


                    <div class="product__availability">
                        <div
                            class="js-react-component"
                            data-mec-react-component="ProductCheckAvailability"
                            data-mec-react-data='{
                                "displayStoreStockCheck": true,
                                "productCode": "5050-315"
                            }'
                        >
                        </div>
                    </div>



        </div>


    <div class="js-react-component" data-mec-react-component="InventorySetStoreModal"></div>











    <div class="js-order-preorder-message" aria-live="polite">


<div class="alert alert--inline alert--info hidden" role="alert">
    <p class="alert__message" aria-live="polite">
        <i class="icon-error" aria-hidden="true"></i>

    </p>
</div>



    </div>







                <div class="btn-add-to-cart__container">
                    <div
                        class="js-add-to-cart-main js-react-component"
                        data-mec-react-component="AddToCartCta"
                        data-mec-react-data='{
                            "productCode": "5050-315"
                        }'
                    >
                    </div>
                </div>
                <div
                    class="js-react-component"
                    data-mec-react-component="AddToCartModal"
                >
                </div>
                <div
                    class="js-react-component"
                    data-mec-react-component="AddedToCartModal"
                ></div>
































<div class="product__value-propositions">




            <!-- Free Shipping Message -->

















<div class="value-proposition value-proposition--tighten">
    <div class="value-proposition__icon shipping-icon">
        <svg width="38" height="29" viewBox="0 0 38 29" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M10.4713 11.1372H0.45752V12.3576H10.4713V11.1372Z" fill="#666"/>
<path d="M9.64622 15.4642H3.12036V16.6847H9.64622V15.4642Z" fill="#666"/>
<path d="M13.7341 6.88416H5.93311V8.10459H12.3089L10.4712 23.1197H15.3468C14.4092 23.6374 13.8091 24.599 13.8091 25.7085C13.8091 27.3727 15.1593 28.7041 16.847 28.7041C18.5348 28.7041 19.8849 27.3727 19.8849 25.7085C19.8849 24.599 19.2474 23.6374 18.3472 23.1197H30.3863C29.4487 23.6374 28.8486 24.599 28.8486 25.7085C28.8486 27.3727 30.1988 28.7041 31.8865 28.7041C33.5743 28.7041 34.9244 27.3727 34.9244 25.7085C34.9244 24.599 34.2868 23.6374 33.3867 23.1197H36.8372V21.8993H11.8964L13.7341 6.88416Z" fill="#666"/>
<path d="M35.412 20.7528L37.9998 0.855957H27.4984L26.1857 8.32652L25.1356 8.10463L26.4108 0.855957H15.9094L13.3215 20.7528H35.412Z" fill="#666"/>
</svg>

    </div>
    <div class="value-proposition__text value-proposition__text--vertical-center">
        <div class="value-proposition__text__shipping-message">
            <span class="text--bold">
                    Free shipping
            </span>

            <!--If this is multiple SKU product, get the price from LowPrice.-->








                for this item


        </div>

    </div>
</div>

    <div class="value-proposition  value-proposition--tighten">
        <div class="value-proposition__icon">
            <svg width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M22.68 17.2618H9.03876V30.0019H22.68V17.2618Z" fill="white"/>
<path d="M29.7515 11.6982H26.2655V4.41827H26.2606L23.8798 2V4.41827V2.00251H9.88654V2L9.88407 2.00251H9.8816V2.00502L7.50572 4.41827H7.50077V11.6982H4V34H29.7391H29.7515V11.6982ZM23.3358 22.5992H10.2252V19.9374H23.3358V22.5992ZM16.0277 24.2792V32.4782H10.2252V24.2792H16.0277ZM17.5334 32.4782V24.2792H23.3358V32.4782H17.5334V32.4782ZM9.90138 4.44338H23.8624V11.6982H9.90138V4.44338Z" fill="#666666"/>
</svg>

        </div>
        <div class="value-proposition__text">
            <p class="value-proposition__text-title">
                Free store pickup
            </p>
            <p class="value-proposition__text-message u-no-margin">
                Order online, get it at your local MEC. It couldn’t be easier.
            </p>
        </div>
    </div>














<div class="value-proposition">
    <div class="value-proposition__icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" aria-labelledby="mec-logo-title" role="img">
    <title id="mec-logo-title">MEC</title>
    <path d="M0 0v60h60V0H0z M24.6 40.8H21V24.7l-0.9 4.9l-2.3 11.2h-3.5l-2.2-11.3l-0.7-4.8v16.1H7.2V18.6h5.9 l2.3 11.3l0.7 4.1l0.7-4.1l2.3-11.3h5.5V40.8z M38.4 22.2h-6.6v5.4h5.4v3.6h-5.4v6h6.6v3.6H27.6V18.6h10.8V22.2z M52.8 26.4h-3.6 v-2.5c0-1.3-0.6-2.2-2.1-2.2S45 22.6 45 23.9v11.7c0 1.3 0.6 2.2 2.1 2.2s2.1-0.9 2.1-2.2V33h3.6v2.5c0 3.4-1.9 5.8-5.8 5.8 s-6.2-2.6-6.2-6.1v-11c0-3.4 2.2-6.1 6.2-6.1s5.8 2.5 5.8 5.8V26.4z" />
</svg>
<span class='logo__symbol--trademark' aria-hidden='true'></span>
    </div>


























      <div class="value-proposition__text">
           <p class="value-proposition__text-title">
               Rocksolid Guarantee
           </p>
           <p class="value-proposition__text-message u-no-margin">
               Shop with confidence. If it’s not working out, you can return it (consumables, undergarments and swimwear excluded).
               <button
                   aria-label="toggle open rock solid proposition" class="js-toggler btn-link value-proposition__text__arrow value-proposition__text__arrow--spin rock-solid_show-arrow"
                   data-mec-toggler-elements='["#value-proposition__text-full-message", {".rock-solid_show-arrow": "is-hidden"}, {".rock-solid_hide-arrow": "is-hidden"}]'>
                       <i class="icon-angle-right-1" aria-hidden="true"></i>
               </button>
           </p>
           <div id="value-proposition__text-full-message" class="value-proposition__text-full-message--rock-solid">
               <p>Really. If it's not up to snuff after you use it (a couple times) you can still bring it back.</p><p>It lasts longer than 30 days, but not forever. We'll be fair about it.</p>
               <button
                   aria-label="toggle close rock solid proposition" class="js-toggler btn-link is-hidden value-proposition__text__arrow value-proposition__text__arrow--bump rock-solid_hide-arrow"
                   data-mec-toggler-elements='["#value-proposition__text-full-message", {".rock-solid_show-arrow": "is-hidden"}, {".rock-solid_hide-arrow": "is-hidden"}]'>
                       <i class="icon-angle-up-1" aria-hidden="true"></i>
               </button>
           </div>
      </div>


</div>











<div class="value-proposition value-proposition--pricematch">
    <div class="value-proposition__icon">
        <svg width="22" height="22" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M11 22C4.9259 22 0 17.0756 0 11C0 4.92443 4.9259 0 11 0C17.0756 0 22 4.92443 22 11C22 17.0756 17.0756 22 11 22Z" fill="#0CA948"/>
    <path fill-rule="evenodd" clip-rule="evenodd" d="M3.39502 7.93384V10.9921C3.85287 10.8638 4.26435 10.4668 4.26435 9.63805C4.26435 8.82595 3.86933 8.34744 3.39502 7.93384V7.93384ZM1.73877 3.50516C1.73877 4.17387 2.16371 4.66747 2.63802 5.08258V2.38965C2.06944 2.50135 1.73877 2.94665 1.73877 3.50516V3.50516ZM4.26434 3.90354C4.24788 3.24993 4.1207 2.62802 3.39501 2.38952V5.68776L3.82145 6.02136C4.84788 6.80177 6 7.63048 6 9.543C6 11.2155 4.99002 12.2812 3.47431 12.5046V13.3333H2.5586V12.5378C0.852868 12.4261 0.0314214 11.1038 0 9.3996H1.70574C1.73865 10.1483 1.84788 10.7687 2.63791 10.9921V7.34367L2.43142 7.16857C0.631422 5.62436 0.0793017 4.98585 0.0793017 3.61674C0.0793017 2.38952 0.790025 1.03551 2.5586 0.813616V0H3.47431V0.813616C5.16359 1.03551 5.90574 2.16763 5.95362 3.90354H4.26434Z" transform="translate(8 4.66675)" fill="#FEFEFE"/>
</svg>

    </div>

    <div class="value-proposition__text">
        <h4 class="value-proposition__text-title">
            Price match guarantee
        </h4>
        <p class="value-proposition__text-message u-no-margin">
            Found a better deal in Canada? Up to 30 days after purchase – we’ll match it.
        </p>
        <div id="value-proposition__text-pricematch-message" class="value-proposition__text-full-message--pricematch">
            <p>If you see a lower price for this exact item advertised online, in print or in a store, give us a call at 1 (888) 847-0770.</p><p>If it’s identical, brand-new, in stock, and sold and shipped by a Canadian-based retailer, we’ll match that price.</p>
        </div>
    </div>

    <div class="value-proposition__arrow" >
        <button
            class="btn btn-link value-proposition__arrow--show pricematch_show-arrow js-toggler"
            data-mec-toggler-elements='["#value-proposition__text-pricematch-message", {".pricematch_show-arrow": "is-hidden"}, {".pricematch_hide-arrow": "is-hidden"}]'
            >
            <i class="icon-angle-right value-proposition__arrow-icon" aria-hidden="true"></i>
        </button>
        <button
            class="btn btn-link value-proposition__arrow--hide pricematch_hide-arrow is-hidden js-toggler"
            data-mec-toggler-elements='["#value-proposition__text-pricematch-message", {".pricematch_show-arrow": "is-hidden"}, {".pricematch_hide-arrow": "is-hidden"}]'
            >
            <i class="icon-angle-up value-proposition__arrow-icon" aria-hidden="true"></i>
        </button>
    </div>
</div>


</div>



    <div class="js-order-special-message" aria-live="polite">

    </div>

    <!-- Shipping Restrictions -->
    <div class="js-shipping-restriction-message " aria-live="polite">



                <!-- This is the placeholder for the sku level shipping restriction message -->


<div class="alert alert--inline alert--warning hidden" role="alert">
    <p class="alert__message" aria-live="polite">
        <i class="icon-error" aria-hidden="true"></i>

    </p>
</div>





    </div>




<div class="alert alert--inline alert--warning" role="alert">
    <p class="alert__message" aria-live="polite">
        <i class="icon-error" aria-hidden="true"></i>
        Ships within Canada only.
    </p>
</div>









<!-- Special Messages (JS placeholder) -->
<div class="js-special-message" aria-live="polite">


<div class="alert alert--inline alert--warning hidden" role="alert">
    <p class="alert__message" aria-live="polite">
        <i class="icon-error" aria-hidden="true"></i>

    </p>
</div>



</div>


















<ul class="list list--horizontal product__secondary-actions">


            <li class="list__item product__secondary-actions-item">
                <div
                    class="js-react-component"
                    data-mec-react-component="AddToWishlistCta"
                    data-mec-react-data='{
                        "productCode": "5050-315"
                    }'
                ></div>
            </li>


            <li class="list__item product__secondary-actions-item">
                <div class="checkbox-link-group-container product__compare">
        <div class="checkbox-link-group js-compare-toggle">
            <input class="checkbox-link-group__field js-compare-toggle-switch" name="checkboxState_5050-315" type="checkbox" id="checkboxCompare_5050-315"   />
            <label class="checkbox-link-group__label" for="checkboxCompare_5050-315">
                <i class="checkbox-link-group__label__check js-checkbox-link-group__label__check icon-ok" aria-hidden="true"></i>
                <div class="checkbox-link-group__link product_controls--secondary-action">
                    <span class="checkbox-link-group__link__text qa-checkbox-link-group__link_text">Compare</span>
                </div>
            </label>
        </div>
    </div>

            </li>

        <li class="list__item product__secondary-actions-item">
             <div class="popover js-popover">
    <button id="share-button" role="button" class="btn btn-square product_controls--secondary-action js-popover-toggle">
        <i class="icon-share" aria-hidden="true"></i>
        Share</button>
    <div class="popover__container">
        <div class="popover__content">
            <ul class="list list--centered list--icons list--social-icons">
                <li class="list__item">
                    <a href="#" class="list__social-icon js-share" data-mec-share-method="facebook" >
                        <span class="sr-only">
                            Share with Facebook</span>
                        <i class="icon-facebook icon-large list__icon" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a href="#" class="list__social-icon js-share" data-mec-share-method="twitter" >
                        <span class="sr-only">
                            Share with Twitter</span>
                        <i class="icon-twitter icon-large list__icon" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a href="#" class="list__social-icon js-share" data-mec-share-method="pinterest" >
                        <span class="sr-only">
                            Share with Pinterest</span>
                        <i class="icon-pinterest icon-large list__icon" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a href="#" class="list__social-icon js-share" data-mec-share-method="email" >
                        <span class="sr-only">
                            Share with Email</span>
                        <i class="icon-mail icon-large list__icon" aria-hidden="true"></i>
                    </a>
                </li>
            </ul>
        </div>
    </div>
</div>
        </li>

</ul>



    <!-- Setup the hidden inputs to use for product data     -->
    <form class="is-hidden" action="/cart/add" method="post" id="addToCartForm" aria-hidden="true">


        <input type="text" name="productCodePost" id="productCodePost" value="" />
        <input type="text" name="quantity" id="productQuantity" value="1" />
        <input type="text" name="entryToBeRemoved" id="entryToBeRemoved" value="" />
        <input type="text" name="CSRFToken" value="a324047d-ea4a-4a2d-aa72-2af0187da702"/>
    </form>

</div>
        </div> <div class="layout__main">
            <!-- Product Description and Technical Specs -->
            <!-- Product Descriptions, Shipping Restriction and Tech Specs  here -->
            <!-- Replaced with -->

            <div class="product__top-border">
                <div id="product0_rr" class="js-recommendation-wrapper recommended-products" data-scheme="product0_rr" data-title="You may also like these similar items">
</div>
</div>

            <!--  Accordion -->
            <div class="product__accordion accordion" data-pdp-accordion>
                <!-- Description -->
                <div class="accordion__branch js-accordion-branch is-open" aria-expanded="true" aria-selected="true">
                    <a href="#" class="accordion__container js-accordion-branch-toggle" role="button" aria-controls="pdp-description">
                        <h3 class="t-level-3 accordion__branch__heading">Description</h3>
                        <div class="accordion__branch__toggle pull-right">
                            <span class="sr-only js-branch-toggle-label">Show</span>
                            <span class="sr-only">Description</span>
                            <i class="icon-minus treecordion__icon js-accordion-branch-icon" aria-hidden="true"></i>
                        </div>
                    </a>
                    <div id="pdp-description" class="accordion__branch__control js-accordion-branch-control product__description" aria-hidden="false">
                        <p>On the trail, on your bike, on the street – these light, tough pants are everything you need for summer action. The breathable stretch fabric moves with you, so you’re always comfortable and in good company.</p><ul><li>Made of recycled nylon with spandex for stretch. DWR finish sheds spills and splashes.</li><li>Fabric provides UPF 50+ sun protection.</li><li>Curved waistband  follows the natural shape of the hips and provides a contoured fit to keep the pants in place.</li><li>Gusseted crotch and articulated knees support a wide range of motion.</li><li>Zip fly with metal button closure, interior drawstring and belt loops.</li><li>2 front slash pockets, 2 rear pockets and a zippered thigh pocket.</li><li>Roll up the hem and convert them to capris with the inner buttons and fabric tabs and outer loops.</li></ul><!-- Sustainability Content -->
                        </div>
                </div>

                <!-- Technical Specs -->
                <div class="accordion__branch js-accordion-branch is-open" aria-expanded="true" aria-selected="false">
    <a href="#" class="accordion__container js-accordion-branch-toggle" role="button" aria-controls="pdp-tech-specs">
        <h3 class="t-level-3 accordion__branch__heading">Tech specs</h2>
        <div class="accordion__branch__toggle pull-right">
            <span class="sr-only js-branch-toggle-label">Show</span>
            <span class="sr-only">Tech specs</span>
            <i class="icon-minus treecordion__icon js-accordion-branch-icon" aria-hidden="true"></i>
        </div>
    </a>
    <div id="pdp-tech-specs" class="accordion__branch__control js-accordion-branch-control product__techspecs" aria-hidden="false">
        <table class="table table--striped table--bordered table--left-column-heading">
            <tbody>
                <!-- Display rows -->
                <tr class="">
    <th>
        Weight</th>
    <td>
        275g (8)</td>
</tr><tr class="">
    <th>
        Ideal for</th>
    <td>
        Camping and hiking</td>
</tr><tr class="">
    <th>
        <div class="popover js-popover">
                    <a href="#" class="js-popover-toggle" role="button" aria-haspopup="true" aria-controls="specs-popover-">
                        <span class="popover__label">Fabric weight</span><i class="icon-help-circled popover__icon" aria-hidden="true"></i></a>
                    <div id="specs-popover-" class="popover__container">
                        <p class="popover__content">Measured in grams per square metre (gsm). The larger the number, the heavier and thicker the garment. </p>
                    </div>
                </div>
            </th>
    <td>
        119gsm</td>
</tr><tr class="">
    <th>
        Fabric content</th>
    <td>
        <ul class="list list--no-margin">
                    <li>62% recycled nylon</li>
                    <li>32% nylon</li>
                    <li>6% spandex</li>
                    </ul>
            </td>
</tr><tr class="">
    <th>
        Pockets</th>
    <td>
        <ul class="list list--no-margin">
                    <li>2 front slash</li>
                    <li>1 back</li>
                    <li>1 back zippered</li>
                    <li>1 side zippered </li>
                    </ul>
            </td>
</tr><tr class="">
    <th>
        <div class="popover js-popover">
                    <a href="#" class="js-popover-toggle" role="button" aria-haspopup="true" aria-controls="specs-popover-">
                        <span class="popover__label">Finished inseam</span><i class="icon-help-circled popover__icon" aria-hidden="true"></i></a>
                    <div id="specs-popover-" class="popover__container">
                        <p class="popover__content">The finished inseam measurement of the garment. </p>
                    </div>
                </div>
            </th>
    <td>
        32in. (8)</td>
</tr><tr class="">
    <th>
        <div class="popover js-popover">
                    <a href="#" class="js-popover-toggle" role="button" aria-haspopup="true" aria-controls="specs-popover-">
                        <span class="popover__label">Antimicrobial treatment</span><i class="icon-help-circled popover__icon" aria-hidden="true"></i></a>
                    <div id="specs-popover-" class="popover__container">
                        <p class="popover__content">A treatment that inhibits bacteria growth and reduces odour.</p>
                    </div>
                </div>
            </th>
    <td>
        No</td>
</tr><tr class="">
    <th>
        Additional feature(s)</th>
    <td>
        <ul class="list list--no-margin">
                    <li>Gusseted crotch</li>
                    <li>Converts to capris</li>
                    </ul>
            </td>
</tr><tr class="">
    <th>
        <div class="popover js-popover">
                    <a href="#" class="js-popover-toggle" role="button" aria-haspopup="true" aria-controls="specs-popover-">
                        <span class="popover__label">UPF rating</span><i class="icon-help-circled popover__icon" aria-hidden="true"></i></a>
                    <div id="specs-popover-" class="popover__container">
                        <p class="popover__content">The Ultraviolet Protection Factor rating indicates how effective a fabric is at blocking out solar ultraviolet radiation.</p>
                    </div>
                </div>
            </th>
    <td>
        40-50+ (Blocks ~97.5% of UVA/UVB)</td>
</tr><tr class="">
    <th>
        Made in</th>
    <td>
        Vietnam</td>
</tr></tbody>
        </table>
    </div>
</div>
<!-- Reviews and Ask and Answer -->









<div class="js-bazaarvoice" data-mec-bv-api="//apps.bazaarvoice.com/deployments/mec/main_site/production/en_CA/bv.js">








<div id="reviews-panel" class="accordion__branch js-accordion-branch" aria-expanded="false" aria-selected="false">
    <a id="reviews"
        href="#"
        class="accordion__container js-accordion-branch-toggle js-bv-reviews"
        role="button"
        aria-controls="pdp-review"
        data-mec-bv-product-code="5050-315"
        data-mec-bv-employee="false"
        data-mec-bv-member=""
        data-mec-bv-email=""
    >
        <div>
            <h3 class="t-level-3 accordion__branch__heading">Reviews


                        (8)



            </h3>
            <!-- Star Ratings -->
            <div class="rating rating--large rating--inline">

                    <span class="rating__count__link__description">
                         out of 5 stars with 8 reviews for Patagonia Quandary Pants - Women's
                    </span>




















            <i class="icon-star rating__icon is-active" aria-hidden="true"></i>









            <i class="icon-star rating__icon is-active" aria-hidden="true"></i>









            <i class="icon-star rating__icon is-active" aria-hidden="true"></i>









            <i class="icon-star rating__icon is-active" aria-hidden="true"></i>








            <i class="icon-star rating__icon rating__icon--half" aria-hidden="true"><i class="icon-star rating__icon is-active" aria-hidden="true"></i></i>





            </div>
        </div>
        <div class="accordion__branch__toggle pull-right">
            <span class="sr-only js-branch-toggle-label">Show</span>
            <span class="sr-only">Reviews</span>
            <i class="icon-plus treecordion__icon js-accordion-branch-icon" aria-hidden="true"></i>
        </div>
    </a>
    <div id="pdp-review" class="accordion__branch__control js-accordion-branch-control" aria-hidden="true">


                <div data-bv-show="reviews" data-bv-product-id="5050-315">
                    <div class="spinner u-pull-center u-margin--top u-margin--bottom"></div>
                </div>



    </div>
</div>









<div class="product__component ask-and-answer">
    <div class="accordion__branch js-accordion-branch" aria-expanded="false" aria-selected="false">
        <a href="#"
            class="accordion__container js-accordion-branch-toggle js-bv-ask-answer"
            role="button"
            aria-controls="pdp-ask-answer"
            data-mec-bv-product-code="5050-315"
        >
            <h3 class="t-level-3 accordion__branch__heading">Ask and answer


                        (<span class="sr-only">Number of questions:</span>5)



            </h3>
            <div class="accordion__branch__toggle pull-right">
                <span class="sr-only js-branch-toggle-label">Show</span>
                <span class="sr-only">Ask and answer</span>
                <i class="icon-plus treecordion__icon js-accordion-branch-icon" aria-hidden="true"></i>
            </div>
        </a>
        <div id="pdp-ask-answer" class="accordion__branch__control js-accordion-branch-control" aria-hidden="true">


                    <div data-bv-show="questions" data-bv-product-id="5050-315">
                        <div class="spinner u-pull-center u-margin--top u-margin--bottom"></div>
                    </div>



        </div>
    </div>
</div>


</div>
<div id="product1_rr" class="js-recommendation-wrapper recommended-products" data-scheme="product1_rr" data-title="Members who looked at this item also looked at">
</div>
<div id="product2_rr" class="js-recommendation-wrapper recommended-products" data-scheme="product2_rr" data-title="Members who looked at this item purchased">
</div>
<!-- Product Size Chart -->



































<div class="size-modal is-hidden js-size-modal">
    <div>
        <div class="size-modal__title">
            Patagonia Size & Fit
        </div>
        <div class="size-modal__chart" aria-hidden="true">
            <input class="multi-state__input js-multi-state__input" checked="checked" type="radio" name="name" id="radio1" value="">
            <input class="multi-state__input js-multi-state__input" type="radio" name="name" id="radio2" value="">



                    <ul class="multi-state__group tabs tabs--centered" role="radiogroup">
                        <li role="radio" class="multi-state__label tabs__item">
                            <label class="js-multi-state-input-toggler" for="radio1" tabindex="0">
                                <span class="tabs__link">centimetres</span>
                                <span class="tabs__link--mobile">cm</span>
                            </label>
                        </li>
                        <li role="radio" class="multi-state__label tabs__item">
                            <label class="js-multi-state-input-toggler" for="radio2" tabindex="0">
                                <span class="tabs__link">inches</span>
                                <span class="tabs__link--mobile">in</span>
                            </label>
                        </li>
                    </ul>




            <div class="multi-state__group table-component--frozen u-margin--bottom js-size-chart-table">
                <div class="table-component--frozen__container js-table-container js-size-chart-overflow">

                        <table class="table table--striped table--bordered table-component--frozen__table js-table js-overflow-item">
                            <thead>



                                        <tr>
                                            <td></td>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        0

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        2

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        4

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        6

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        8

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        10

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        12

                                                </th>

                                                <th scope="col" class="size-modal__chart__column-title">

                                                        14

                                                </th>

                                        </tr>






                            </thead>
                            <tbody>





                                        <tr class="js-table-row">
                                            <th scope="row" class="size-modal__chart__row-title">
                                                <span class="table-component--frozen__row-header js-table-title">

                                                        <div class="popover popover--fixed-width js-popover">
                                                            <span class="popover__label">Waist</span>
                                                            <span>


                                                                    <span class="multi-state__data-item">(cm)</span>


                                                                    <span class="multi-state__data-item">(in.)</span>


                                                            </span>
                                                        </div>

                                                </span>
                                                <span class="table-component--frozen__row-placeholder">

                                                        <div class="popover popover--fixed-width js-popover">
                                                            <a href="#" class="js-popover-toggle" role="button" aria-haspopup="true" aria-controls="specs-popover-1">
                                                                <span class="popover__label">
                                                                    Waist
                                                                </span><i class="icon-help-circled popover__icon" aria-hidden="true"></i>
                                                            </a>
                                                            <div id="specs-popover-1" class="popover__container">
                                                                <p class="popover__content">Measure at the narrowest circumference of your waist.</p>
                                                            </div>
                                                        </div>




                                                        <span class="multi-state__data-item">(cm)</span>


                                                        <span class="multi-state__data-item">(in.)</span>


                                                </span>
                                            </th>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>64.75</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>25½</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>67.25</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>26½</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>69.75</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>27½</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>72.5</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>28½</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>75</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>29½</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>77.5</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>30½</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.5</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>85</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>33½</span>


                                                        </span>

                                                </td>

                                        </tr>




                                        <tr class="js-table-row">
                                            <th scope="row" class="size-modal__chart__row-title">
                                                <span class="table-component--frozen__row-header js-table-title">

                                                        <div class="popover popover--fixed-width js-popover">
                                                            <span class="popover__label">Inseam</span>
                                                            <span>


                                                                    <span class="multi-state__data-item">(cm)</span>


                                                                    <span class="multi-state__data-item">(in.)</span>


                                                            </span>
                                                        </div>

                                                </span>
                                                <span class="table-component--frozen__row-placeholder">

                                                        <div class="popover popover--fixed-width js-popover">
                                                            <a href="#" class="js-popover-toggle" role="button" aria-haspopup="true" aria-controls="specs-popover-2">
                                                                <span class="popover__label">
                                                                    Inseam
                                                                </span><i class="icon-help-circled popover__icon" aria-hidden="true"></i>
                                                            </a>
                                                            <div id="specs-popover-2" class="popover__container">
                                                                <p class="popover__content">Measure inner leg from crotch to just below the ankle bone.</p>
                                                            </div>
                                                        </div>




                                                        <span class="multi-state__data-item">(cm)</span>


                                                        <span class="multi-state__data-item">(in.)</span>


                                                </span>
                                            </th>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>78.75</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>31</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>78.75</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>31</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.25</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.25</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.25</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.25</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.5</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                                <td>



                                                        <span class="multi-state__data-item">
                                                            <span>81.5</span>


                                                        </span>



                                                        <span class="multi-state__data-item">
                                                            <span>32</span>


                                                        </span>

                                                </td>

                                        </tr>


                            </tbody>
                        </table>


                </div>
            </div>




            <footer class="size-modal__footer">
                <div>
                    <button class="size-modal__close js-size-modal__close" data-modal-close>OK</button>
                </div>
                <div>
                    <a href="#size-modal__top" class="size-modal__top-button js-size-modal__top-button">Back To Top</a>
                </div>
            </footer>
        </div>
    </div>
</div>
<div id="product3_rr" class="js-recommendation-wrapper recommended-products" data-scheme="product3_rr" data-title="Recently viewed items">
</div>
<!-- Staff Info -->
                </div> <!-- end Accordion -->

            <!-- Media Assets -->
            <div class="product__component recommendations recommendations--product">
                </div>

            <div class="u-max-line-length">
                <!-- Campaigns -->
                <div class="product__component product__promotions">
                    </div>

                <!-- Non Shop Content -->
                </div><!-- end line length container -->

        </div>




<div class="compare-drawer container js-compare-drawer">
    <div class="row">
        <div class="grid__bucket--xl compare-drawer-container">
            <div class="compare-drawer-container__wrapper">
                <a href="#" role="button" class="compare-drawer__header-container js-compare-drawer-toggle-button" aria-controls="compare-drawer">
                    <h4 class="compare-drawer__heading qa-compare-drawer__heading">Compare (<span class="js-compare-drawer-count">0</span>)
                        <i class="icon-angle-up compare-drawer__remove-icon js-compare-drawer-plus-icon">
                            <span class="sr-only">Open</span>
                        </i>
                        <i class="icon-angle-down compare-drawer__remove-icon is-hidden js-compare-drawer-minus-icon">
                            <span class="sr-only">Close</span>
                        </i>
                    </h4>
                </a>
                <div id="compare-drawer" class="compare-drawer__container js-compare-drawer-container">
                    <div class="compare-drawer__product-container-box js-compare-drawer-products-container-box js-compare-overflow">
                        <div class="compare-drawer__product-container js-compare-drawer-products-container js-overflow-item">
                        </div>
                    </div>
                    <div class="compare-drawer__compare-btn">
                        <a href="/en/compare" class="btn btn-primary btn--sm-block compare-drawer__button qa-compare-drawer__button" tabindex="-1">Compare</a>
                        <a href="#" class="compare-drawer__remove-all text--subtle js-compare-drawer-remove-all qa-compare-drawer-remove-all" tabindex="-1">Remove all</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div></div> <script>
    window.Product = window.Product || {};
    Product.code = "5050-315";
    Product.price = {"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null};
    Product.badge = {"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""};
    Product.skus = [{"code":"549596","size":"2","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-2","upc":"889833779266","skuSortValue":20,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"549597","size":"4","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-4","upc":"889833779273","skuSortValue":40,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"549598","size":"6","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-6","upc":"889833779280","skuSortValue":60,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"549599","size":"8","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-8","upc":"889833779297","skuSortValue":80,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"549600","size":"10","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-10","upc":"889833779303","skuSortValue":100,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"549601","size":"12","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-12","upc":"889833779310","skuSortValue":120,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"549602","size":"14","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-14","upc":"889833779327","skuSortValue":140,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"596342","size":"0","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-0","upc":"889833779259","skuSortValue":1,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826200","size":"0-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-0","upc":"889833782976","skuSortValue":2054,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826201","size":"16","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"INFO","vendorPartNumber":"55416-FGE-16","upc":"191743715754","skuSortValue":160,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826202","size":"18","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"WARNING","vendorPartNumber":"55416-FGE-18","upc":"191743715761","skuSortValue":180,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826203","size":"20","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55416-FGE-20","upc":"192964099692","skuSortValue":2000,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826204","size":"22","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55416-FGE-22","upc":"192964099708","skuSortValue":220,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826205","size":"2-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-2","upc":"889833782983","skuSortValue":2055,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826206","size":"4-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-4","upc":"889833782990","skuSortValue":2056,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826207","size":"6-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-6","upc":"889833783003","skuSortValue":2057,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826208","size":"8-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-8","upc":"889833783010","skuSortValue":2058,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826249","size":"10-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-10","upc":"889833783027","skuSortValue":2059,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826250","size":"12-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-12","upc":"889833783034","skuSortValue":2060,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826251","size":"14-Short","colour":"FRG00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55410-FGE-14","upc":"889833783041","skuSortValue":2061,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595914","size":"2","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-2","upc":"190696761429","skuSortValue":20,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595915","size":"4","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-4","upc":"190696761443","skuSortValue":40,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595916","size":"6","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-6","upc":"190696761467","skuSortValue":60,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595917","size":"8","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-8","upc":"190696761481","skuSortValue":80,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595918","size":"10","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-10","upc":"190696761504","skuSortValue":100,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595919","size":"12","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-12","upc":"190696761528","skuSortValue":120,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"595920","size":"14","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-14","upc":"190696761535","skuSortValue":140,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"596345","size":"0","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-0","upc":"190696761405","skuSortValue":1,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826238","size":"16","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":true,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":true,"messageSeverity":"INFO","vendorPartNumber":"55416-SHLE-16","upc":"191743716034","skuSortValue":160,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826239","size":"18","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55416-SHLE-18","upc":"191743716065","skuSortValue":180,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826240","size":"20","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55416-SHLE-20","upc":"192964099999","skuSortValue":2000,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null},{"code":"826241","size":"22","colour":"SHA00","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"specialMessage":null,"specialOrder":false,"onlineAvailabilityMessage":null,"availableForSaleOnline":false,"merchantCenterPreOrder":false,"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"shippingRestrictionMessage":"Ships within Canada only.","purchasableOnline":false,"messageSeverity":"WARNING","vendorPartNumber":"55416-SHLE-22","upc":"192964100008","skuSortValue":220,"newToMec":false,"creationDate":null,"stockLevel":null,"availability":null,"preOrder":false,"backOrder":false,"preOrderMessage":"","webOnly":false,"skuStatus":null}];
    Product.colours = [{"code":"FRG00","name":"Forge Grey","swatchUrl":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993200275486/5050315-FRG00-SWATCH-placeholder.jpg","clearance":false,"price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"swatchColours":["#59565a"],"colourBuckets":["Grey"],"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"availableForSaleOnline":true,"purchasableOnline":true,"includesSpecialOrder":false,"priceGroup":"BUY"},{"code":"SHA00","name":"Shale","swatchUrl":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941967704094/5050315-SHA00-SWATCH-placeholder.jpg","clearance":false,"price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"swatchColours":["#a8a287","#aea98e"],"colourBuckets":["Beige"],"badge":{"stateName":"none","state":"NONE","discountPercentageValue":null,"formattedDiscountPercentageValue":null,"multiDiscount":false,"beginDate":"","endDate":""},"availableForSaleOnline":true,"purchasableOnline":true,"includesSpecialOrder":false,"priceGroup":"BUY"}];
    Product.sizes = [{"code":"0","name":"0","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"2","name":"2","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"4","name":"4","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"6","name":"6","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"8","name":"8","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"10","name":"10","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"12","name":"12","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"14","name":"14","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"16","name":"16","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"18","name":"18","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":{"currencyIso":"CAD","value":99.0,"priceType":"BUY","formattedValue":"$99.00","minQuantity":null,"maxQuantity":null,"originalPrice":null,"discount":null,"discounted":false},"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":true,"includesSpecialOrder":false},{"code":"22","name":"22","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"20","name":"20","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"0-Short","name":"0-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"2-Short","name":"2-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"4-Short","name":"4-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"6-Short","name":"6-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"8-Short","name":"8-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"10-Short","name":"10-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"12-Short","name":"12-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false},{"code":"14-Short","name":"14-Short","price":{"highestDiscount":null,"discounted":false,"multiPriced":false,"multiDiscounted":false,"price":null,"lowPrice":null,"highPrice":null,"discountQualifierMessage":null},"availableForSaleOnline":false,"includesSpecialOrder":false}];
    Product.mediaGallery = [{"mediaType":null,"colour":"FRG00","colourNameMap":{"fr":"Gris forge","en":"Forge Grey"},"productNameMap":{"de":null,"fr":"Pantalon Quandary","en":"Quandary Pants"},"colourBuckets":null,"discounted":false,"primaryForColour":true,"originalMedia":null,"media":{"placeholder":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8992982827038/5050315-FRG00-placeholder.jpg","type":"image","fallback":"https://cdn.mec.ca/medias/sys_master/fallback/fallback/8992982892574/5050315-FRG00-fallback.jpg","highRes":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8992982761502/5050315-FRG00.jpg"},"caption":"Forge Grey","productName":null,"colourName":null,"altTextForImage":"Quandary Pants Forge Grey"},{"mediaType":null,"colour":"FRG00","colourNameMap":{"fr":"Gris forge","en":"Forge Grey"},"productNameMap":{"de":null,"fr":"Pantalon Quandary","en":"Quandary Pants"},"colourBuckets":null,"discounted":false,"primaryForColour":false,"originalMedia":null,"media":{"placeholder":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001963550/5050315-FRG00-ALT-BACK-placeholder.jpg","type":"image","fallback":"https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993002061854/5050315-FRG00-ALT-BACK-fallback.jpg","highRes":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001898014/5050315-FRG00-ALT-BACK.jpg"},"caption":"Forge Grey","productName":null,"colourName":null,"altTextForImage":"Quandary Pants Forge Grey"},{"mediaType":null,"colour":"FRG00","colourNameMap":{"fr":"Gris forge","en":"Forge Grey"},"productNameMap":{"de":null,"fr":"Pantalon Quandary","en":"Quandary Pants"},"colourBuckets":null,"discounted":false,"primaryForColour":false,"originalMedia":null,"media":{"placeholder":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001111582/5050315-FRG00-ALT-CAPRIS-placeholder.jpg","type":"image","fallback":"https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993001209886/5050315-FRG00-ALT-CAPRIS-fallback.jpg","highRes":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001046046/5050315-FRG00-ALT-CAPRIS.jpg"},"caption":"Forge Grey","productName":null,"colourName":null,"altTextForImage":"Quandary Pants Forge Grey"},{"mediaType":null,"colour":"FRG00","colourNameMap":{"fr":"Gris forge","en":"Forge Grey"},"productNameMap":{"de":null,"fr":"Pantalon Quandary","en":"Quandary Pants"},"colourBuckets":null,"discounted":false,"primaryForColour":false,"originalMedia":null,"media":{"placeholder":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993001275422/5050315-FRG00-ALT-DETAIL-placeholder.jpg","type":"image","fallback":"https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993001340958/5050315-FRG00-ALT-DETAIL-fallback.jpg","highRes":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993001144350/5050315-FRG00-ALT-DETAIL.jpg"},"caption":"Forge Grey","productName":null,"colourName":null,"altTextForImage":"Quandary Pants Forge Grey"},{"mediaType":null,"colour":"FRG00","colourNameMap":{"fr":"Gris forge","en":"Forge Grey"},"productNameMap":{"de":null,"fr":"Pantalon Quandary","en":"Quandary Pants"},"colourBuckets":null,"discounted":false,"primaryForColour":false,"originalMedia":null,"media":{"placeholder":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8993002586142/5050315-FRG00-ALT-FLAT-placeholder.jpg","type":"image","fallback":"https://cdn.mec.ca/medias/sys_master/fallback/fallback/8993002651678/5050315-FRG00-ALT-FLAT-fallback.jpg","highRes":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8993002487838/5050315-FRG00-ALT-FLAT.jpg"},"caption":"Forge Grey","productName":null,"colourName":null,"altTextForImage":"Quandary Pants Forge Grey"},{"mediaType":null,"colour":"SHA00","colourNameMap":{"fr":"Schiste","en":"Shale"},"productNameMap":{"de":null,"fr":"Pantalon Quandary","en":"Quandary Pants"},"colourBuckets":null,"discounted":false,"primaryForColour":true,"originalMedia":null,"media":{"placeholder":"https://cdn.mec.ca/medias/sys_master/placeholder/placeholder/8941966753822/5050315-SHA00-placeholder.jpg","type":"image","fallback":"https://cdn.mec.ca/medias/sys_master/fallback/fallback/8941967376414/5050315-SHA00-fallback.jpg","highRes":"https://cdn.mec.ca/medias/sys_master/high-res/high-res/8941965344798/5050315-SHA00.jpg"},"caption":"Shale","productName":null,"colourName":null,"altTextForImage":"Quandary Pants Shale"}];
    Product.selectedColour = "FRG00";
    Product.selectedSize = null;
    Product.specialMessage = null;
    Product.freeShippingMessage = "This item ships FREE! Free store pickup available: inside or at the storefront.";
    Product.shippingRestrictionMessage = "Ships within Canada only.";
    Product.ontarioShippingRestrictionMessage = null;
    Product.specifications = [{"name":"Weight","values":["275g (8)"],"description":"","displayDesc":false},{"name":"Ideal for","values":["Camping and hiking"],"description":"","displayDesc":false},{"name":"Fabric weight","values":["119gsm"],"description":"Measured in grams per square metre (gsm). The larger the number, the heavier and thicker the garment. ","displayDesc":true},{"name":"Fabric content","values":["62% recycled nylon","32% nylon","6% spandex"],"description":"","displayDesc":false},{"name":"Pockets","values":["2 front slash","1 back","1 back zippered","1 side zippered "],"description":"","displayDesc":false},{"name":"Finished inseam","values":["32in. (8)"],"description":"The finished inseam measurement of the garment. ","displayDesc":true},{"name":"Antimicrobial treatment","values":["No"],"description":"A treatment that inhibits bacteria growth and reduces odour.","displayDesc":true},{"name":"Additional feature(s)","values":["Gusseted crotch","Converts to capris"],"description":"","displayDesc":false},{"name":"UPF rating","values":["40-50+ (Blocks ~97.5% of UVA/UVB)"],"description":"The Ultraviolet Protection Factor rating indicates how effective a fabric is at blocking out solar ultraviolet radiation.","displayDesc":true},{"name":"Made in","values":["Vietnam"],"description":"Country where product is made","displayDesc":false}];
    Product.archived = false;
    Product.stockedInStores = true;
    Product.sustainabilityAttributes = [];
    Product.availableForSaleOnline = true;
    Product.onlineAvailabilityMessage = null;
    Product.preOrderMessage = null;
    Product.messageSeverity = null;
    Product.purchasableOnline = true;
    Product.allPreOrder = false;
    Product.allBackOrder = false;
    Product.allWebOnly = false;
    Product.type = "Normal";
    Product.selectedSku = null;
    Product.storeSkuStatuses = [];
    Product.storeColourStatuses = [];
    Product.includesSpecialOrder = false;
    Product.averageRating = 4.625;
    Product.numberOfReviews = 8;
    Product.name = "Patagonia Quandary Pants - Women's";
    Product.primaryCategoryPath = "/products/camping-and-hiking/hiking-clothing/hiking-pants/c/1008";
    Product.primaryCategoryName = "Hiking pants";
    Product.inStorePickupOnly = false;
    Product.promotionalProduct = false;
    Product.isGiftCard = false;
    Product.sizeChart = {"code":"Patagonia_Women_Bottoms_Numeric","name":"Patagonia_Women_Bottoms_Numeric","table":{"rows":[{"id":"key.measurement","definition":null,"title":"key.measurement","units":[{"unit":"Unit","system":"TEXT"}],"cells":[{"values":[[{"unit":{"unit":"Unit","system":"TEXT"},"system":"TEXT","stringValue":"0"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"0"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"2"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"2"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"4"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"4"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"6"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"6"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"8"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"8"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"10"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"10"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"12"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"12"}]]},{"values":[[{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"14"},{"unit":{"unit":"key.unit_type","system":"TEXT"},"system":"TEXT","stringValue":"14"}]]}]},{"id":"key.waist","definition":"Measure at the narrowest circumference of your waist.","title":"Waist","units":[{"unit":"in.","system":"IMPERIAL"},{"unit":"cm","system":"METRIC"}],"cells":[{"values":[[{"unit":{"unit":"cm","system":"METRIC"},"system":"METRIC","stringValue":"64.75"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"in.","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"25½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"67.25"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"26½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"69.75"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"27½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"72.5"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"28½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"75"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"29½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"77.5"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"30½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.5"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"85"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"33½"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]}]},{"id":"key.inseam","definition":"Measure inner leg from crotch to just below the ankle bone.","title":"Inseam","units":[{"unit":"in.","system":"IMPERIAL"},{"unit":"cm","system":"METRIC"}],"cells":[{"values":[[{"unit":{"unit":"cm","system":"METRIC"},"system":"METRIC","stringValue":"78.75"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"in.","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"31"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"78.75"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"31"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.25"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.25"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.25"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.25"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.5"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]},{"values":[[{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":"81.5"},{"unit":{"unit":"key.unit_cm","system":"METRIC"},"system":"METRIC","stringValue":""}],[{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":"32"},{"unit":{"unit":"key.unit_in","system":"IMPERIAL"},"system":"IMPERIAL","stringValue":""}]]}]}]},"images":null,"tableContainsMetricData":true,"tableContainsImperialData":true};
    Product.promotionMessageList = null;
    try {
        window.availabilityStore = JSON.parse("null");
    } catch (err) {
        console.error('Error while evaluating the availability store as JSON. Setting to null.', err);
        window.availabilityStore = null;
    }
    window.allStores = [{"name":"barrie","displayName":"Barrie","url":"/stores/barrie","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":44.358,"longitude":-79.693},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027186199","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Barrie","line2":"61 Bryne Drive","town":"Barrie","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"L4N 8V8","phone":"792-4675","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Barrie, 61 Bryne Drive, Ontario, Barrie, L4N 8V8","fullName":null,"areaCode":"705","areaCode2":null,"areaCode3":null,"line3":"705-792-4675","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"17","ip":"70.54.242.210","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Barrie","storeNumber":"17","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Barrie for outdoor gear, know-how and inspiration.","store_name":"Barrie","manager":"Stacey Baldry","phone_number":"(705) 792-4675","hours_reference":{"ID":1051,"post_author":"218","post_date":"2021-02-15 01:00:18","post_date_gmt":"2021-02-15 09:00:18","post_content":"","post_title":"Barrie hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"barrie-hours","to_ping":"","pinged":"","post_modified":"2021-07-27 07:53:21","post_modified_gmt":"2021-07-27 14:53:21","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1051","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"address_line_1":"61 Bryne Drive","address_line_2":"","city":"Barrie","province":"Ontario","postal_code":"L4N 8V8","latitude":"44.3570998","longitude":"-79.6960377","google_maps_url":"https://www.google.com/maps/place/MEC+Barrie/@44.3570998,-79.6960377,17z/data=!3m1!4b1!4m2!3m1!1s0x882abcfd20cc57f9:0xc6374530e7d39520?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Barrie,+61+Bryne+Drive,+Barrie+Ontario,+L4N+8V8&hl=en&sll=44.358,-79.693&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Barrie,+61+Bryne+Drive,+Barrie+Ontario,+L4N+8V8&hl=en&sll=44.358,-79.693&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Barrie,+61+Bryne+Drive,+Barrie+Ontario,+L4N+8V8&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Barrie,+61+Bryne+Drive,+Barrie+Ontario,+L4N+8V8&hl=en&sll=44.358,-79.693&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Barrie, ON - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"burlington","displayName":"Burlington","url":"/stores/burlington","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":43.339,"longitude":-79.819},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027218967","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Burlington","line2":"1030 Brant Street","town":"Burlington","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"L7R 0B2","phone":"333-8559","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Burlington, 1030 Brant Street, Ontario, Burlington, L7R 0B2","fullName":null,"areaCode":"905","areaCode2":null,"areaCode3":null,"line3":"905-333-8559","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"15","ip":"216.208.111.130","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Burlington","storeNumber":"15","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Burlington for outdoor gear, know-how and inspiration.","store_name":"Burlington","manager":"Cameron Dempster","phone_number":"(905) 333-8559","hours_reference":{"ID":1053,"post_author":"218","post_date":"2021-02-15 01:00:19","post_date_gmt":"2021-02-15 09:00:19","post_content":"","post_title":"Burlington hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"burlington-hours","to_ping":"","pinged":"","post_modified":"2021-07-27 07:52:58","post_modified_gmt":"2021-07-27 14:52:58","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1053","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"1030 Brant Street","address_line_2":"","city":"Burlington","province":"Ontario","postal_code":"L7R 0B2","latitude":"43.3386941","longitude":"-79.8208436","google_maps_url":"https://www.google.com/maps/place/MEC+Burlington/@43.3386941,-79.8208436,17z/data=!3m1!4b1!4m2!3m1!1s0x882b61fd2a6947e3:0xc80bc88cee063609?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Burlington,+1030+Brant+Street,+Burlington+Ontario,+L7R+0B2&hl=en&sll=43.339,-79.819&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Burlington,+1030+Brant+Street,+Burlington+Ontario,+L7R+0B2&hl=en&sll=43.339,-79.819&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Burlington,+1030+Brant+Street,+Burlington+Ontario,+L7R+0B2&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Burlington,+1030+Brant+Street,+Burlington+Ontario,+L7R+0B2&hl=en&sll=43.339,-79.819&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Burlington, ON - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"calgary","displayName":"Calgary","url":"/stores/calgary","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":51.044,"longitude":-114.081},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027382807","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Calgary","line2":"830 10th Avenue SW","town":"Calgary","region":{"isocode":"CA-AB","isocodeShort":"AB","countryIso":"CA","name":"Alberta"},"postalCode":"T2R 0A9","phone":"269-2420","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Calgary, 830 10th Avenue SW, Alberta, Calgary, T2R 0A9","fullName":null,"areaCode":"403","areaCode2":null,"areaCode3":null,"line3":"403-269-2420","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"2","ip":"216.123.210.149","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Calgary","storeNumber":"2","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Calgary for outdoor gear, know-how and inspiration.","store_name":"Calgary","manager":"Matthew Lewis","phone_number":"(403) 269-2420","hours_reference":{"ID":1060,"post_author":"171","post_date":"2020-06-03 00:05:09","post_date_gmt":"2020-06-03 07:05:09","post_content":"","post_title":"Calgary hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"calgary-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:02:44","post_modified_gmt":"2021-08-03 14:02:44","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1060","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"9:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"830 – 10th Avenue SW","address_line_2":"","city":"Calgary","province":"Alberta","postal_code":"T2R 0A9","latitude":"51.0441907","longitude":"-114.083004","google_maps_url":"https://www.google.com/maps/place/MEC+Calgary/@51.0441907,-114.083004,17z/data=!3m1!4b1!4m2!3m1!1s0x53716fe1118d6e2d:0x2c2d94f6697dfc66?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Calgary,+830+%E2%80%93+10th+Avenue+SW,+Calgary+Alberta,+T2R+0A9&hl=en&sll=51.044,-114.081&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Calgary,+830+%E2%80%93+10th+Avenue+SW,+Calgary+Alberta,+T2R+0A9&hl=en&sll=51.044,-114.081&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Calgary,+830+%E2%80%93+10th+Avenue+SW,+Calgary+Alberta,+T2R+0A9&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Calgary,+830+%E2%80%93+10th+Avenue+SW,+Calgary+Alberta,+T2R+0A9&hl=en&sll=51.044,-114.081&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Calgary, AB - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"edmonton","displayName":"Edmonton","url":"/stores/edmonton","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":53.54620805,"longitude":-113.527045},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027251735","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Edmonton","line2":"11904 104 Avenue NW","town":"Edmonton","region":{"isocode":"CA-AB","isocodeShort":"AB","countryIso":"CA","name":"Alberta"},"postalCode":"T5K 0G6","phone":"488-6614","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Edmonton, 11904 104 Avenue NW, Alberta, Edmonton, T5K 0G6","fullName":null,"areaCode":"780","areaCode2":null,"areaCode3":null,"line3":"780-488-6614","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"5","ip":"216.123.198.213","inStockRange":"48","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Edmonton","storeNumber":"5","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Edmonton for outdoor gear, know-how and inspiration.","store_name":"Edmonton","manager":"Garry Beer","phone_number":"(780) 488-6614","hours_reference":{"ID":1071,"post_author":"171","post_date":"2020-11-10 14:20:10","post_date_gmt":"2020-11-10 22:20:10","post_content":"","post_title":"Edmonton hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"edmonton-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:04:58","post_modified_gmt":"2021-08-03 14:04:58","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1071","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"9:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"11904 104th Ave NW","address_line_2":"","city":"Edmonton","province":"Alberta","postal_code":"T5K 0G6","latitude":"53.5468197","longitude":"-113.5278247","google_maps_url":"https://www.google.ca/maps/dir/11904+104+Avenue+Northwest/11904+104+Ave+NW,+Edmonton,+AB+T5K/@53.5462077,-113.5297237,17z/data=!4m13!4m12!1m5!1m1!1s0x53a0222d41f4ae6f:0xdeda1a7a17f2885b!2m2!1d-113.527535!2d53.5462077!1m5!1m1!1s0x53a0222d41f4ae6f:0xdeda1a7a17f2885b!2m2!1d-113.527535!2d53.5462077","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=11904+104+Ave+NW,+Edmonton,+AB+T5K&hl=en&sll=53.5468197,-113.5278247&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=11904+104+Ave+NW,+Edmonton,+AB+T5K&hl=en&sll=53.5468197,-113.5278247&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=11904+104+Ave+NW,+Edmonton,+AB+T5K&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=11904+104+Ave+NW,+Edmonton,+AB+T5K&hl=en&sll=53.5468197,-113.5278247&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Edmonton, AB - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":"Store is temporarily closed until further notice","relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"south-edmonton","displayName":"South Edmonton","url":"/stores/south-edmonton","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":53.445732,"longitude":-113.487483},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027710487","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"South Edmonton","line2":"1624 99 Street NW","town":"Edmonton","region":{"isocode":"CA-AB","isocodeShort":"AB","countryIso":"CA","name":"Alberta"},"postalCode":"T6N 1M5","phone":"433-0293","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"South Edmonton, 1624 99 Street NW, Alberta, Edmonton, T6N 1M5","fullName":null,"areaCode":"780","areaCode2":null,"areaCode3":null,"line3":null,"phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"24","ip":null,"inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Edmonton South","storeNumber":"24","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC South Edmonton for outdoor gear, know-how and inspiration.","meta_title":"MEC South Edmonton, AB - Outdoor and Camping Store | MEC","store_name":"South Edmonton","manager":"Garry Beer","phone_number":"(780) 433-0293","hours_reference":{"ID":3673,"post_author":"171","post_date":"2020-06-03 00:05:08","post_date_gmt":"2020-06-03 07:05:08","post_content":"","post_title":"South Edmonton Common hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"south-edmonton-common-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:05:18","post_modified_gmt":"2021-08-03 14:05:18","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=3673","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"9:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"services":[{"service":"Bike shop"},{"service":"Ski shop"}],"address_line_1":"1624 99 Street NW","address_line_2":"South Edmonton Common","city":"Edmonton","province":"Alberta","postal_code":"T6N 1M5","latitude":"53.445732","longitude":"-113.487483","google_maps_url":"https://www.google.ca/maps/place/MEC+South+Edmonton+Common/@53.4457324,-113.4874828,15z/data=!4m13!1m7!3m6!1s0x0:0x7963f519f2d2b664!2sMEC+South+Edmonton+Common!3b1!8m2!3d53.4457324!4d-113.4874828!3m4!1s0x0:0x7963f519f2d2b664!8m2!3d53.4457324!4d-113.4874828","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+South+Edmonton+Common,1624+99+Street+NW,+South+Edmonton+Common,,+Edmonton+Alberta,+T6N+1N5&hl=en&sll=53.445732,-113.487483&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+South+Edmonton+Common,1624+99+Street+NW,+South+Edmonton+Common,,+Edmonton+Alberta,+T6N+1N5&hl=en&sll=53.445732,-113.487483&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+South+Edmonton+Common,1624+99+Street+NW,+South+Edmonton+Common,,+Edmonton+Alberta,+T6N+1N5&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+South+Edmonton+Common,1624+99+Street+NW,+South+Edmonton+Common,,+Edmonton+Alberta,+T6N+1N5&hl=en&sll=53.445732,-113.487483&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","direction_details":[{"label":"","details":""}],"twitter_url":"","open_to_public":true},"relocationMessage":null,"relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"halifax","displayName":"Halifax","url":"/stores/halifax","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":44.646,"longitude":-63.573},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027153431","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Halifax","line2":"1550 Granville Street","town":"Halifax","region":{"isocode":"CA-NS","isocodeShort":"NS","countryIso":"CA","name":"Nova Scotia"},"postalCode":"B3J 1X1","phone":"421-2667","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Halifax, 1550 Granville Street, Nova Scotia, Halifax, B3J 1X1","fullName":null,"areaCode":"902","areaCode2":null,"areaCode3":null,"line3":"902-421-2667","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"6","ip":"142.176.158.58","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":false,"storePickup":true,"storeName":"Halifax","storeNumber":"6","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Halifax for outdoor gear, know-how and inspiration.","store_name":"Halifax","manager":"Kristian Rafuse","phone_number":"(902) 421-2667","hours_reference":{"ID":1084,"post_author":"218","post_date":"2021-05-30 21:00:47","post_date_gmt":"2021-05-31 04:00:47","post_content":"","post_title":"Halifax hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"halifax-hours","to_ping":"","pinged":"","post_modified":"2021-07-02 15:24:13","post_modified_gmt":"2021-07-02 22:24:13","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1084","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"6:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"address_line_1":"1550 Granville Street","address_line_2":"","city":"Halifax","province":"Nova Scotia","postal_code":"B3J 1X1","latitude":"44.6455736","longitude":"-63.5749633","google_maps_url":"https://www.google.com/maps/place/MEC+Halifax/@44.6455736,-63.5749633,17z/data=!3m1!4b1!4m2!3m1!1s0x4b5a2233547dff5d:0x144c81cb8c9aea6?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Halifax,+1550+Granville+Street,+Halifax+Nova+Scotia,+B3J+1X1&hl=en&sll=44.646,-63.573&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Halifax,+1550+Granville+Street,+Halifax+Nova+Scotia,+B3J+1X1&hl=en&sll=44.646,-63.573&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Halifax,+1550+Granville+Street,+Halifax+Nova+Scotia,+B3J+1X1&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Halifax,+1550+Granville+Street,+Halifax+Nova+Scotia,+B3J+1X1&hl=en&sll=44.646,-63.573&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Halifax, NS - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"kelowna","displayName":"Kelowna","url":"/stores/kelowna","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":49.8800569,"longitude":-119.4490824},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027644951","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Kelowna","line2":"Unit 100 – 1876 Cooper Rd","town":"Kelowna","region":{"isocode":"CA-BC","isocodeShort":"BC","countryIso":"CA","name":"British Columbia"},"postalCode":"V1Y 9N6","phone":"448-7637","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Kelowna, Unit 100 – 1876 Cooper Rd, British Columbia, Kelowna, V1Y 9N6","fullName":null,"areaCode":"250","areaCode2":null,"areaCode3":null,"line3":null,"phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"22","ip":null,"inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Kelowna","storeNumber":"22","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Kelowna for outdoor gear, know-how and inspiration. ","store_name":"Kelowna","manager":"Liz Burnside","phone_number":"(250) 448-7637","hours_reference":{"ID":1267,"post_author":"171","post_date":"2020-05-25 00:05:15","post_date_gmt":"2020-05-25 07:05:15","post_content":"","post_title":"Kelowna hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"kelowna-hours","to_ping":"","pinged":"","post_modified":"2021-07-02 14:38:46","post_modified_gmt":"2021-07-02 21:38:46","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1267","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"British Columbia Day","date":"02/08/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"1876 Cooper Rd, Unit 100","address_line_2":"","city":"Kelowna","province":"British Columbia","postal_code":"V1Y 9N6","latitude":"49.879605","longitude":"-119.447051","google_maps_url":"https://www.google.ca/maps/place/MEC+Kelowna/@49.880859,-119.4480116,17z/data=!3m1!4b1!4m5!3m4!1s0x537d8cb7bd7fedc1:0x601576ab0ca9b44!8m2!3d49.8808556!4d-119.4458229","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Kelowna,+1876+Cooper+Rd,+Unit+100++,+Kelowna+British+Columbia,+V1Y+9N6&hl=en&sll=49.8800569,-119.4490824&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Kelowna,+1876+Cooper+Rd,+Unit+100++,+Kelowna+British+Columbia,+V1Y+9N6&hl=en&sll=49.8800569,-119.4490824&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Kelowna,+1876+Cooper+Rd,+Unit+100++,+Kelowna+British+Columbia,+V1Y+9N6&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Kelowna,+1876+Cooper+Rd,+Unit+100++,+Kelowna+British+Columbia,+V1Y+9N6&hl=en&sll=49.8800569,-119.4490824&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Kelowna, BC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"kitchener","displayName":"Kitchener","url":"/stores/kitchener","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":43.418698,"longitude":-80.452622},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"9052207742999","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Kitchener","line2":"10 Manitou Drive","town":"Kitchener","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"N2C 2N3","phone":"896-4972","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Kitchener, 10 Manitou Drive, Ontario, Kitchener, N2C 2N3","fullName":null,"areaCode":"519","areaCode2":null,"areaCode3":null,"line3":null,"phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"25","ip":null,"inStockRange":"2","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Kitchener","storeNumber":"25","wpStoreContent":{"meta_description":"","meta_title":"MEC Kitchener, Ontario - Outdoor and Camping Store | MEC","store_name":"Kitchener","manager":"Marten Mann","phone_number":"(519) 896-4972","hours_reference":{"ID":13006,"post_author":"218","post_date":"2021-02-15 01:00:17","post_date_gmt":"2021-02-15 09:00:17","post_content":"","post_title":"Kitchener hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"kitchener-hours","to_ping":"","pinged":"","post_modified":"2021-07-27 07:51:25","post_modified_gmt":"2021-07-27 14:51:25","post_content_filtered":"","post_parent":0,"guid":"https://meccms.wpengine.com/?post_type=hours&#038;p=13006","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"open_to_public":true,"services":false,"address_line_1":"10 Manitou Drive","address_line_2":"","city":"Kitchener","province":"Ontario","postal_code":"N2C 2N3","latitude":"43.4186982","longitude":"-80.454811","google_maps_url":"","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=10+Manitou+Dr,+Kitchener,+ON+N2C+2N3&hl=en&sll=43.4186982,-80.454811,17&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=10+Manitou+Dr,+Kitchener,+ON+N2C+2N3&hl=en&sll=43.4186982,-80.454811,17&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=10+Manitou+Dr,+Kitchener,+ON+N2C+2N3&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=10+Manitou+Dr,+Kitchener,+ON+N2C+2N3&hl=en&sll=43.4186982,-80.454811,17&gl=ca&dirflg=b&mra=ltm&t=m&z=11","direction_details":false,"twitter_url":""},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"JUST_RELOCATED","relocationImage":null},{"name":"langley","displayName":"Langley","url":"/stores/langley","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":49.114,"longitude":-122.672},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027415575","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Langley","line2":"Unit #1 - 6121 200th St","town":"Langley","region":{"isocode":"CA-BC","isocodeShort":"BC","countryIso":"CA","name":"British Columbia"},"postalCode":"V2Y 1A2","phone":"534-4570","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Langley, Unit #1 - 6121 200th St, British Columbia, Langley, V2Y 1A2","fullName":null,"areaCode":"604","areaCode2":null,"areaCode3":null,"line3":"604-534-4570","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"19","ip":null,"inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Langley","storeNumber":"19","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Langley for outdoor gear, know-how and inspiration.","store_name":"Langley","manager":"Andrew Brumby","phone_number":"(604) 534-4570","hours_reference":{"ID":1094,"post_author":"171","post_date":"2020-03-15 11:00:50","post_date_gmt":"2020-03-15 18:00:50","post_content":"","post_title":"Langley hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"langley-hours","to_ping":"","pinged":"","post_modified":"2021-07-02 14:42:43","post_modified_gmt":"2021-07-02 21:42:43","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1094","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"8:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"8:00pm","notice":""},{"day":"Saturday","open":"9:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"British Columbia Day","date":"02/08/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"8:00pm","notice":""}]},"address_line_1":"6121 200th St Unit 1","address_line_2":"","city":"Langley","province":"British Columbia","postal_code":"V2Y 1A2","latitude":"49.1138081","longitude":"-122.6738497","google_maps_url":"https://www.google.com/maps/place/MEC+Langley/@49.1138081,-122.6738497,17z/data=!3m1!4b1!4m2!3m1!1s0x5485d02b964a1e5b:0x35e80759b911a910?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Langley,+6121+200th+St+Unit+1,+Langley+British+Columbia,+V2Y+1A2&hl=en&sll=49.114,-122.672&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Langley,+6121+200th+St+Unit+1,+Langley+British+Columbia,+V2Y+1A2&hl=en&sll=49.114,-122.672&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Langley,+6121+200th+St+Unit+1,+Langley+British+Columbia,+V2Y+1A&hl=en2&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Langley,+6121+200th+St+Unit+1,+Langley+British+Columbia,+V2Y+1A2&hl=en&sll=49.114,-122.672&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Langley, BC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"laval","displayName":"Laval","url":"/stores/laval","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":45.56958,"longitude":-73.7576268},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027841559","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Laval","line2":"2615, boulevard Daniel-Johnson","town":"Laval","region":{"isocode":"CA-QC","isocodeShort":"QC","countryIso":"CA","name":"Quebec"},"postalCode":"H7T 1S8","phone":"688-2712","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Laval, 2615, boulevard Daniel-Johnson, Quebec, Laval, H7T 1S8","fullName":null,"areaCode":"450","areaCode2":null,"areaCode3":null,"line3":null,"phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"23","ip":null,"inStockRange":"2","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Laval","storeNumber":"23","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Laval for outdoor gear, know-how and inspiration.","meta_title":"MEC Laval, QC - Outdoor and Camping Store | MEC","store_name":"Laval","manager":"Rémi Larose","phone_number":"(450) 688-2712","hours_reference":{"ID":3657,"post_author":"171","post_date":"2020-12-25 00:10:08","post_date_gmt":"2020-12-25 08:10:08","post_content":"","post_title":"Laval hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"laval-hours","to_ping":"","pinged":"","post_modified":"2021-07-02 15:44:27","post_modified_gmt":"2021-07-02 22:44:27","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=3657","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"6:00pm","notice":""}],"exceptions":[{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"services":[{"service":"Bike shop"},{"service":"Ski shop"}],"address_line_1":"2615 Boulevard Daniel-Johnson","address_line_2":"","city":"Laval","province":"Quebec","postal_code":"H7T 1S8","latitude":"45.56958","longitude":"-73.7576268","google_maps_url":"https://www.google.ca/maps/place/MEC+Laval/@45.570326,-73.757793,15z/data=!4m2!3m1!1s0x0:0x1c57681540b6d0b7?sa=X&ved=0ahUKEwjn1JKa6rDQAhUY02MKHd1gC3wQ_BIIfDAK","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Laval,2615+Boulevard+Daniel-Johnson,,+Laval+Quebec,+H7T+1S8&hl=en&sll=45.5687789,-73.7571293&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Laval,2615+Boulevard+Daniel-Johnson,,+Laval+Quebec,+H7T+1S8&hl=en&sll=45.5687789,-73.7571293&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Laval,2615+Boulevard+Daniel-Johnson,,+Laval+Quebec,+H7T+1S8&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Laval,2615+Boulevard+Daniel-Johnson,,+Laval+Quebec,+H7T+1S8&hl=en&sll=45.5687789,-73.7571293&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","direction_details":[{"label":"","details":""}],"twitter_url":"","open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"london","displayName":"London","url":"/stores/london","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":42.936918,"longitude":-81.225298},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027284503","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"London","line2":"1051 Wellington Road","town":"London","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"N6E 1W4","phone":"668-6657","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"London, 1051 Wellington Road, Ontario, London, N6E 1W4","fullName":null,"areaCode":"519","areaCode2":null,"areaCode3":null,"line3":"519-668-6657","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"18","ip":null,"inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"London","storeNumber":"18","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC London for outdoor gear, know-how and inspiration.","store_name":"London","manager":"Marten Mann","phone_number":"(519) 668-6657","hours_reference":{"ID":1100,"post_author":"218","post_date":"2021-02-15 01:00:15","post_date_gmt":"2021-02-15 09:00:15","post_content":"","post_title":"London hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"london-hours","to_ping":"","pinged":"","post_modified":"2021-07-27 07:48:04","post_modified_gmt":"2021-07-27 14:48:04","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1100","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"address_line_1":"1051 Wellington Road","address_line_2":"","city":"London","province":"Ontario","postal_code":"N6E 1W4","latitude":"42.936858","longitude":"-81.2278629","google_maps_url":"https://www.google.ca/maps/place/MEC+London/@42.936858,-81.2278629,17z/data=!3m1!4b1!4m5!3m4!1s0x882ef39a76100ebf:0x7ef4cb36ef7aa355!8m2!3d42.936858!4d-81.2256742","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+London,+1051+Wellington+Rd,+London,+ON+N6E+1W4&hl=en&sll=42.927,-81.217&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+London,+1051+Wellington+Rd,+London,+ON+N6E+1W4&hl=en&sll=42.927,-81.217&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+London,+1051+Wellington+Rd,+London,+ON+N6E+1W4&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+London,+1051+Wellington+Rd,+London,+ON+N6E+1W4&hl=en&sll=42.927,-81.217&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC London, ON - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"longueuil","displayName":"Longueuil","url":"/stores/longueuil","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":45.484,"longitude":-73.465},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027317271","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Longueuil","line2":"4869, boulevard Taschereau","town":"Greenfield Park","region":{"isocode":"CA-QC","isocodeShort":"QC","countryIso":"CA","name":"Quebec"},"postalCode":"J4V 3K3","phone":"766-1359","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Longueuil, 4869, boulevard Taschereau, Quebec, Greenfield Park, J4V 3K3","fullName":null,"areaCode":"450","areaCode2":null,"areaCode3":null,"line3":"450-766-1359","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"16","ip":"207.134.106.218","inStockRange":"2","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Longueuil","storeNumber":"16","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Longueuil for outdoor gear, know-how and inspiration.","store_name":"Longueuil","manager":"Benoit Perrier","phone_number":"(450) 766-1359","hours_reference":{"ID":1105,"post_author":"171","post_date":"2020-12-25 00:50:03","post_date_gmt":"2020-12-25 08:50:03","post_content":"","post_title":"Longueuil hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"longueuil-hours","to_ping":"","pinged":"","post_modified":"2021-07-23 10:43:51","post_modified_gmt":"2021-07-23 17:43:51","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1105","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"address_line_1":"4869 Taschereau Boulevard","address_line_2":"","city":"Longueuil","province":"Quebec","postal_code":"J4V 3K3","latitude":"45.4841689","longitude":"-73.4671005","google_maps_url":"https://www.google.com/maps/place/MEC+Longueuil/@45.4841689,-73.4671005,17z/data=!3m1!4b1!4m2!3m1!1s0x4cc9050c50a050e7:0xee153ea908143b84?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Longueuil,+4869+Taschereau+Boulevard,+Longueuil+Quebec,+J4V+3K3&hl=en&sll=45.484,-73.465&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Longueuil,+4869+Taschereau+Boulevard,+Longueuil+Quebec,+J4V+3K3&hl=en&sll=45.484,-73.465&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Longueuil,+4869+Taschereau+Boulevard,+Longueuil+Quebec,+J4V+3K3&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Longueuil,+4869+Taschereau+Boulevard,+Longueuil+Quebec,+J4V+3K3&hl=en&sll=45.484,-73.465&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Longueuil, QC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"montreal","displayName":"Montréal (Marché Central)","url":"/stores/montreal","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":45.532,"longitude":-73.652},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027350039","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Montréal (Marché Central)","line2":"8989, boulevard de l'Acadie","town":"Montréal","region":{"isocode":"CA-QC","isocodeShort":"QC","countryIso":"CA","name":"Quebec"},"postalCode":"H4N 3K1","phone":"788-5878","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Montréal (Marché Central), 8989, boulevard de l'Acadie, Quebec, Montréal, H4N 3K1","fullName":null,"areaCode":"514","areaCode2":null,"areaCode3":null,"line3":"514-788-5878","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"11","ip":"66.158.144.242","inStockRange":"2","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Montréal","storeNumber":"11","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Montreal for outdoor gear, know-how and inspiration.","store_name":"Montréal","manager":"Jean-Francois Brien","phone_number":"(514) 788-5878","hours_reference":{"ID":1120,"post_author":"171","post_date":"2020-12-25 00:10:09","post_date_gmt":"2020-12-25 08:10:09","post_content":"","post_title":"Montreal hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"montreal-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:03:10","post_modified_gmt":"2021-08-03 14:03:10","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1120","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"8:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"8:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"8:00pm","notice":""}],"exceptions":[{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"8989 de l'Acadie Boulevard","address_line_2":"","city":"Montréal","province":"Québec","postal_code":"H4N 3K1","latitude":"45.5643362","longitude":"-73.6987865","google_maps_url":"https://www.google.com/maps/place/MEC+Montr%C3%A9al/@45.5643362,-73.6987865,11z/data=!4m5!1m2!2m1!1smec+montreal!3m1!1s0x4cc918f99ab0930f:0x3a22dc2c7f858e63?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Montr%C3%A9al,+8989+de+l%27Acadie+Boulevard,+Montreal+Quebec,+H4N+3K1&hl=en&sll=45.532,-73.652&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Montr%C3%A9al,+8989+de+l%27Acadie+Boulevard,+Montreal+Quebec,+H4N+3K1&hl=en&sll=45.532,-73.652&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Montr%C3%A9al,+8989+de+l%27Acadie+Boulevard,+Montreal+Quebec,+H4N+3K1&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Montr%C3%A9al,+8989+de+l%27Acadie+Boulevard,+Montreal+Quebec,+H4N+3K1&hl=en&sll=45.532,-73.652&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Montreal, QC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"north-vancouver","displayName":"North Vancouver","url":"/stores/north-vancouver","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":49.308,"longitude":-123.04},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027448343","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"North Vancouver","line2":"212 Brooksbank Avenue","town":"North Vancouver","region":{"isocode":"CA-BC","isocodeShort":"BC","countryIso":"CA","name":"British Columbia"},"postalCode":"V7J 2C1","phone":"990-4417","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"North Vancouver, 212 Brooksbank Avenue, British Columbia, North Vancouver, V7J 2C1","fullName":null,"areaCode":"604","areaCode2":null,"areaCode3":null,"line3":"604-990-4417","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"13","ip":"208.181.70.245","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"North Vancouver","storeNumber":"13","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC North Vancouver for outdoor gear, know-how and inspiration.","store_name":"North Vancouver","manager":"Caitlin Brown","phone_number":"(604) 990-4417","hours_reference":{"ID":1009,"post_author":"171","post_date":"2020-06-13 00:05:02","post_date_gmt":"2020-06-13 07:05:02","post_content":"","post_title":"North Vancouver Hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"north-vancouver-hours","to_ping":"","pinged":"","post_modified":"2021-07-02 14:37:25","post_modified_gmt":"2021-07-02 21:37:25","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1009","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"British Columbia Day","date":"02/08/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"address_line_1":"212 Brooksbank Avenue","address_line_2":"","city":"North Vancouver","province":"BC","postal_code":"V7J 2C1","latitude":"49.307849","longitude":"-123.040003","google_maps_url":"https://www.google.com/maps/place/MEC+North+Vancouver/@49.3075647,-123.0422289,17z/data=!3m1!4b1!4m2!3m1!1s0x548670f4cbedb3b7:0xb82f1ab02b50635a?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+Vancouver,+212+Brooksbank+Avenue,+North+Vancouver+British+Columbia,+V7J+2C1&hl=en&sll=49.308,-123.04&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+Vancouver,+212+Brooksbank+Avenue,+North+Vancouver+British+Columbia,+V7J+2C1&hl=en&sll=49.308,-123.04&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+Vancouver,+212+Brooksbank+Avenue,+North+Vancouver+British+Columbia,+V7J+2C1&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+Vancouver,+212+Brooksbank+Avenue,+North+Vancouver+British+Columbia,+V7J+2C1&hl=en&sll=49.308,-123.04&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC North Vancouver, BC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"north-york","displayName":"North York","url":"/stores/north-york","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":43.769509,"longitude":-79.375179},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027677719","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"North York","line2":"784 Sheppard Avenue East","town":"North York","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"M2K 1C3","phone":"221-0030","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"North York, 784 Sheppard Avenue East, Ontario, North York, M2K 1C3","fullName":null,"areaCode":"416","areaCode2":null,"areaCode3":null,"line3":null,"phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"21","ip":null,"inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"North York","storeNumber":"21","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC North York for outdoor gear, know-how and inspiration.","meta_title":"MEC North York, ON - Outdoor and Camping Store | MEC","store_name":"North York","manager":"Graeme Stewart","phone_number":"1 (416) 221-0030","hours_reference":{"ID":3681,"post_author":"218","post_date":"2021-03-07 20:00:05","post_date_gmt":"2021-03-08 04:00:05","post_content":"","post_title":"North York hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"north-york-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:04:13","post_modified_gmt":"2021-08-03 14:04:13","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=3681","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Closed","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"services":[{"service":"Bike shop"},{"service":"Ski shop"}],"address_line_1":"784 Sheppard Avenue East","address_line_2":"","city":"North York","province":"Ontario","postal_code":"M2K 1C3","latitude":"43.769509","longitude":"-79.375179","google_maps_url":"https://www.google.ca/maps/place/MEC+North+York/@43.769856,-79.375251,15z/data=!4m2!3m1!1s0x0:0x233774d761ba422e?sa=X&ved=0ahUKEwj_5cvJhdHQAhUi2oMKHfG1AbYQ_BIIcjAL","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+York,784+Sheppard+Avenue+East,,+Toronto+Ontario,+M2K+1C3&hl=en&sll=,&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+York,784+Sheppard+Avenue+East,,+Toronto+Ontario,+M2K+1C3&hl=en&sll=,&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+York,784+Sheppard+Avenue+East,,+Toronto+Ontario,+M2K+1C3&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+North+York,784+Sheppard+Avenue+East,,+Toronto+Ontario,+M2K+1C3&hl=en&sll=,&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","direction_details":[{"label":"","details":""}],"twitter_url":"","open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":null},{"name":"ottawa","displayName":"Ottawa","url":"/stores/ottawa","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":45.391,"longitude":-75.755},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027513879","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Ottawa","line2":"366 Richmond Road","town":"Ottawa","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"K2A 0E8","phone":"729-2700","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Ottawa, 366 Richmond Road, Ontario, Ottawa, K2A 0E8","fullName":null,"areaCode":"613","areaCode2":null,"areaCode3":null,"line3":"613-729-2700","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"4","ip":"216.208.111.162","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Ottawa","storeNumber":"4","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Ottawa for outdoor gear, know-how and inspiration. ","store_name":"Ottawa","manager":"Chris Chapman","phone_number":"(613) 729-2700","hours_reference":{"ID":1141,"post_author":"218","post_date":"2021-02-15 01:00:14","post_date_gmt":"2021-02-15 09:00:14","post_content":"","post_title":"Ottawa hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"ottawa-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:03:41","post_modified_gmt":"2021-08-03 14:03:41","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1141","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"366 Richmond Road","address_line_2":"","city":"Ottawa","province":"Ontario","postal_code":"K2A 0E8","latitude":"45.3912797","longitude":"-75.7574117","google_maps_url":"https://www.google.com/maps/place/MEC+Ottawa/@45.3912797,-75.7574117,17z/data=!3m1!4b1!4m2!3m1!1s0x4cce06a9de2c46cf:0xc4878f2b596c04af?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Ottawa,+366+Richmond+Road,+Ottawa+Ontario,+K2A+0E8&hl=en&sll=45.391,-75.755&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Ottawa,+366+Richmond+Road,+Ottawa+Ontario,+K2A+0E8&hl=en&sll=45.391,-75.755&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Ottawa,+366+Richmond+Road,+Ottawa+Ontario,+K2A+0E8&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Ottawa,+366+Richmond+Road,+Ottawa+Ontario,+K2A+0E8&hl=en&sll=45.391,-75.755&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Ottawa, ON - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"quebec","displayName":"Québec","url":"/stores/quebec","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":46.83412505,"longitude":-71.29889307},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027546647","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Québec","line2":"1475, boulevard Lebourgneuf","town":"Québec","region":{"isocode":"CA-QC","isocodeShort":"QC","countryIso":"CA","name":"Quebec"},"postalCode":"G2K 2G3","phone":"522-8884","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Québec, 1475, boulevard Lebourgneuf, Quebec, Québec, G2K 2G3","fullName":null,"areaCode":"418","areaCode2":null,"areaCode3":null,"line3":"418-522-8884","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"12","ip":"199.243.87.106","inStockRange":"2","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Québec City","storeNumber":"12","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Québec City for outdoor gear, know-how and inspiration.","store_name":"Québec City","manager":"Marie Claude Asselin","phone_number":"(418) 522-8884","hours_reference":{"ID":1146,"post_author":"218","post_date":"2021-05-09 23:00:41","post_date_gmt":"2021-05-10 06:00:41","post_content":"","post_title":"Quebec hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"quebec-hours","to_ping":"","pinged":"","post_modified":"2021-07-27 10:58:23","post_modified_gmt":"2021-07-27 17:58:23","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1146","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"1475 Boulevard Lebourgneuf","address_line_2":"","city":"Québec City","province":"Québec","postal_code":"G2K 2G3","latitude":"46.8353657","longitude":"-71.2987385","google_maps_url":"https://www.google.ca/maps/place/MEC/@46.8353657,-71.2987385,126a,35y,177.14h,45t/data=!3m1!1e3!4m13!1m7!3m6!1s0x4cb897eda9fcab47:0xec210278ae670b58!2s1475+Boulevard+Lebourgneuf,+Ville+de+Qu%C3%A9bec,+QC+G2K+2G3!3b1!8m2!3d46.8341245!4d-71.2988931!3m4!1s0x0:0xd0d1247a0d4e4ee6!8m2!3d46.8341243!4d-71.2988931?hl=en","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC,+1475+Boulevard+Lebourgneuf,+Qu%C3%A9bec+City,+QC,+G2K+2G3&hl=en&sll=46.8341245,-71.2988931&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC,+1475+Boulevard+Lebourgneuf,+Qu%C3%A9bec+City,+QC,+G2K+2G3&hl=en&sll=46.8341245,-71.2988931&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC,+1475+Boulevard+Lebourgneuf,+Qu%C3%A9bec+City,+QC,+G2K+2G3&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC,+1475+Boulevard+Lebourgneuf,+Qu%C3%A9bec+City,+QC,+G2K+2G3&hl=en&sll=46.8341245,-71.2988931&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Québec City, QC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"JUST_RELOCATED","relocationImage":null},{"name":"toronto","displayName":"Toronto","url":"/stores/toronto","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":43.646,"longitude":-79.393},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027808791","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Toronto","line2":"300 Queen Street West","town":"Toronto","region":{"isocode":"CA-ON","isocodeShort":"ON","countryIso":"CA","name":"Ontario"},"postalCode":"M5V 2A2","phone":"340-2667","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Toronto, 300 Queen Street West, Ontario, Toronto, M5V 2A2","fullName":null,"areaCode":"416","areaCode2":null,"areaCode3":null,"line3":"416-340-2667","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"3","ip":"216.208.111.130","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Toronto","storeNumber":"3","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Toronto for outdoor gear, know-how and inspiration.","store_name":"Toronto","manager":"Graeme Stewart","phone_number":"(416) 340-2667","hours_reference":{"ID":1164,"post_author":"218","post_date":"2021-03-07 20:00:04","post_date_gmt":"2021-03-08 04:00:04","post_content":"","post_title":"Toronto hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"toronto-hours","to_ping":"","pinged":"","post_modified":"2021-07-27 09:04:50","post_modified_gmt":"2021-07-27 16:04:50","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1164","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"5:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"","close":"Closed","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"","close":"Closed","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"","close":"Closed","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""},{"name":"Boxing Day","date":"26/12/2021","open":"10:00am","close":"5:00pm","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"300 Queen St West","address_line_2":"","city":"Toronto","province":"Ontario","postal_code":"M5V 2A2","latitude":"43.6461136","longitude":"-79.3955303","google_maps_url":"https://www.google.com/maps/place/MEC+Toronto/@43.6461136,-79.3955303,17z/data=!3m1!4b1!4m2!3m1!1s0x882b34da2473d0db:0xed019023e804ea04?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Toronto,+400+King+St+West,+Toronto+Ontario,+M5V+1K2&hl=en&sll=43.646,-79.393&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Toronto,+400+King+St+West,+Toronto+Ontario,+M5V+1K2&hl=en&sll=43.646,-79.393&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Toronto,+400+King+St+West,+Toronto+Ontario,+M5V+1K2&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Toronto,+400+King+St+West,+Toronto+Ontario,+M5V+1K2&hl=en&sll=43.646,-79.393&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Toronto, ON - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":null,"relocationStatus":"NA","relocationImage":null},{"name":"vancouver","displayName":"Vancouver","url":"/stores/vancouver","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":49.262974,"longitude":-123.108636},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027579415","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Vancouver","line2":"111 2nd Ave East","town":"Vancouver","region":{"isocode":"CA-BC","isocodeShort":"BC","countryIso":"CA","name":"British Columbia"},"postalCode":"V5T 1B4","phone":"872-7858","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Vancouver, 111 2nd Ave East, British Columbia, Vancouver, V5T 1B4","fullName":null,"areaCode":"604","areaCode2":null,"areaCode3":null,"line3":"604-872-7858","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"1","ip":"207.194.65.61","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Vancouver","storeNumber":"1","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Vancouver for outdoor gear, know-how and inspiration.","store_name":"Vancouver","manager":"Sylvia Mcloughlin","phone_number":"(604) 872-7858","hours_reference":{"ID":830,"post_author":"218","post_date":"2020-11-25 13:30:06","post_date_gmt":"2020-11-25 21:30:06","post_content":"","post_title":"Vancouver Store Hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"vancouver-store-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:01:55","post_modified_gmt":"2021-08-03 14:01:55","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=830","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"9:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"British Columbia Day","date":"02/08/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"111 2nd Ave East","address_line_2":"","city":"Vancouver","province":"British Columbia","postal_code":"V5T 1B4","latitude":"49.269311","longitude":"-123.102375","google_maps_url":"https://www.google.com/maps/place/MEC+Vancouver/@49.2692001,-123.102048,18.5z/data=!4m5!3m4!1s0x0:0x8bcc34f3037fa595!8m2!3d49.2692815!4d-123.1023783","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Vancouver,+111+2nd+Ave+East,+Vancouver,+BC+V5T+1B4&hl=en&sll=49.2692815,-123.1023783&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Vancouver,+111+2nd+Ave+East,+Vancouver,+BC+V5T+1B4&hl=en&sll=49.2692815,-123.1023783&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Vancouver,+111+2nd+Ave+East,+Vancouver,+BC+V5T+1B4&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Vancouver,+111+2nd+Ave+East,+Vancouver,+BC+V5T+1B4&hl=en&sll=49.2692815,-123.1023783&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Vancouver, BC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski shop"},{"service":"Fittings"},{"service":"Recycling and repair"}],"direction_details":[{"label":"Parking","details":"Rooftop pay parking is available via back lane access. We have preferred parking set aside for hybrid vehicles and car co-ops."}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":null,"relocationMessageMedium":null,"relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":null},{"name":"victoria","displayName":"Victoria","url":"/stores/victoria","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":48.428,"longitude":-123.367},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027612183","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Victoria","line2":"1450 Government Street","town":"Victoria","region":{"isocode":"CA-BC","isocodeShort":"BC","countryIso":"CA","name":"British Columbia"},"postalCode":"V8W 1Z2","phone":"386-2667","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Victoria, 1450 Government Street, British Columbia, Victoria, V8W 1Z2","fullName":null,"areaCode":"250","areaCode2":null,"areaCode3":null,"line3":"250-386-2667","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"14","ip":"209.53.183.37","inStockRange":"24","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Victoria","storeNumber":"14","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Victoria for outdoor gear, know-how and inspiration.","store_name":"Victoria","manager":"Patrick Humer","phone_number":"(250) 386-2667","hours_reference":{"ID":1188,"post_author":"171","post_date":"2020-05-25 00:05:13","post_date_gmt":"2020-05-25 07:05:13","post_content":"","post_title":"Victoria hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"victoria-hours","to_ping":"","pinged":"","post_modified":"2021-08-03 07:04:37","post_modified_gmt":"2021-08-03 14:04:37","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1188","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"9:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"7:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"British Columbia Day","date":"02/08/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"9:00pm","notice":""}]},"address_line_1":"1450 Government Street","address_line_2":"","city":"Victoria","province":"British Columbia","postal_code":"V8W 1Z2","latitude":"48.4280026","longitude":"-123.3695117","google_maps_url":"https://www.google.com/maps/place/MEC+Victoria/@48.4280026,-123.3695117,17z/data=!3m1!4b1!4m2!3m1!1s0x548f7484bf4be59b:0xba702c6d88a0d526?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=1450+Government+Street,+Victoria+British+Columbia,+V8W+1Z2&hl=en&sll=48.428,-123.367&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=1450+Government+Street,+Victoria+British+Columbia,+V8W+1Z2&hl=en&sll=48.428,-123.367&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&q=1450+Government+Street,+Victoria+British+Columbia,+V8W+1Z2&daddr=1450+Government+Street,+Victoria+British+Columbia,+V8W+1Z2&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=1450+Government+Street,+Victoria+British+Columbia,+V8W+1Z2&hl=en&sll=48.428,-123.367&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Victoria, BC - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":"- Temporarily closed","relocationMessageMedium":"Some MEC stores are opening with limited services.","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h07/hd5/9109816737822/store-reopen.png?w=800&h=800&auto=format&q=60","altText":null}},{"name":"winnipeg","displayName":"Winnipeg","url":"/stores/winnipeg","description":null,"openingHours":null,"storeContent":null,"features":{},"geoPoint":{"latitude":49.894,"longitude":-97.143},"formattedDistance":null,"distanceKm":null,"mapIcon":null,"address":{"id":"8798027776023","title":null,"titleCode":null,"firstName":null,"lastName":null,"companyName":null,"line1":"Winnipeg","line2":"303 Portage Avenue","town":"Winnipeg","region":{"isocode":"CA-MB","isocodeShort":"MB","countryIso":"CA","name":"Manitoba"},"postalCode":"R3B 2B4","phone":"943-4202","email":null,"country":{"isocode":"CA","name":"Canada","regions":null},"shippingAddress":false,"billingAddress":false,"defaultAddress":false,"visibleInAddressBook":true,"formattedAddress":"Winnipeg, 303 Portage Avenue, Manitoba, Winnipeg, R3B 2B4","fullName":null,"areaCode":"204","areaCode2":null,"areaCode3":null,"line3":"204-943-4202","phone2":null,"cellPhone":null,"extension":null,"extension2":null,"memberAddress":false,"fullPhoneNumber":null,"secondaryFullPhoneNumber":null},"storeImages":[],"storeStockCheck":true,"id":"7","ip":"209.202.64.242","inStockRange":"2","outOfStockRange":"5-10","outOfStockRangeForOverSizeItem":"10-15","pickFromStore":true,"storePickup":true,"storeName":"Winnipeg","storeNumber":"7","wpStoreContent":{"meta_description":"If you love trails, snow, water or fresh air, this is your store. Visit MEC Winnipeg for outdoor gear, know-how and inspiration.","store_name":"Winnipeg","manager":"Lynnette Futros","phone_number":"(204) 943-4202","hours_reference":{"ID":1257,"post_author":"171","post_date":"2020-11-10 16:10:01","post_date_gmt":"2020-11-11 00:10:01","post_content":"","post_title":"Winnipeg hours","post_excerpt":"","post_status":"publish","comment_status":"closed","ping_status":"closed","post_password":"","post_name":"winnipeg-hours","to_ping":"","pinged":"","post_modified":"2021-07-02 15:05:58","post_modified_gmt":"2021-07-02 22:05:58","post_content_filtered":"","post_parent":0,"guid":"http://meccms.wpengine.com/?post_type=hours&#038;p=1257","menu_order":0,"post_type":"hours","post_mime_type":"","comment_count":"0","filter":"raw","notice":"","hours":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Friday","open":"10:00am","close":"7:00pm","notice":""},{"day":"Saturday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Sunday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Monday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Tuesday","open":"10:00am","close":"6:00pm","notice":""},{"day":"Wednesday","open":"10:00am","close":"6:00pm","notice":""}],"exceptions":[{"name":"Canada Day","date":"01/07/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Labour Day","date":"06/09/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Thanksgiving Day","date":"11/10/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Remembrance Day","date":"11/11/2021","open":"10:00am","close":"5:00pm","notice":""},{"name":"Christmas Day","date":"25/12/2021","open":"","close":"Closed","notice":""}],"currentDate":[{"day":"Thursday","open":"10:00am","close":"7:00pm","notice":""}]},"address_line_1":"303 Portage Avenue","address_line_2":"","city":"Winnipeg","province":"Manitoba","postal_code":"R3B 2B4","latitude":"49.8941424","longitude":"-97.1455097","google_maps_url":"https://www.google.com/maps/place/MEC+Winnipeg/@49.8941424,-97.1455097,17z/data=!3m1!4b1!4m2!3m1!1s0x52ea7159a1cdfd27:0x51bc8e16cc3c8f8e?hl=en-US","walk_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Winnipeg,+303+Portage+Avenue,+Winnipeg+Manitoba,+R3B+2B4&hl=en&sll=49.894,-97.143&gl=ca&dirflg=w&mra=ltm&t=m&z=11","public_transport_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Winnipeg,+303+Portage+Avenue,+Winnipeg+Manitoba,+R3B+2B4&hl=en&sll=49.894,-97.143&gl=ca&dirflg=r&ttype=now&noexp=0&noal=0&sort=def&mra=ltm&t=m&z=11&start=0","drive_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Winnipeg,+303+Portage+Avenue,+Winnipeg+Manitoba,+R3B+2B4&hl=en&gl=ca&t=m&z=11","bike_directions":"https://maps.google.ca/maps?saddr=current+location&daddr=MEC+Winnipeg,+303+Portage+Avenue,+Winnipeg+Manitoba,+R3B+2B4&hl=en&sll=49.894,-97.143&gl=ca&dirflg=b&mra=ltm&t=m&z=11&lci=bike","twitter_url":"","meta_title":"MEC Winnipeg, MB - Outdoor and Camping Store | MEC","services":[{"service":"Bike shop"},{"service":"Ski services"},{"service":"Repairs and recycling"}],"direction_details":[{"label":"","details":""}],"open_to_public":true},"relocationMessage":null,"relocationMessageShort":"Open for pickup only","relocationMessageMedium":"Open for pickup only","relocationMessageText":"Some MEC stores are opening with limited services and strict safety measures in place","relocationStatus":"NA","relocationImage":null}];
    window.showInventoryLevelOnStorePc = false;
</script>

</div>
			</main>

			<footer class="footer ">
    <div class="footer__top">










<div class="footer__container">
    <div class="footer__row footer__row--top flexfooter__row">
        <div class="flexfooter__container">
            <div class="flexfooter__block">
                <a class="u-no-decoration" href="/en/explore/returns-and-guarantee/">
                    <div class="flexfooter__logo">
                        <div class="flexfooter__logo-image flexfooter__logo-image--mec"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 144 144" alt="MEC">
    <defs>
        <style>.logo-cls-2{fill:#fff}</style>
    </defs>
    <path fill="#0ca948" d="M0 0h144v144H0z"/>
    <path class="logo-cls-2" d="M66.5 97.94h25.47v-8.89H76.44V75.07h12.97v-8.88H76.44v-12.7h15.53V44.6H66.5v53.34zM112.87 43.4c-9.53 0-15.38 6.41-15.38 14.66v26.43c0 8.24 5.85 14.65 15.38 14.65s14.41-5.93 14.41-13.93v-6.49h-8.89v6.4c0 3.13-1.76 5.29-5.36 5.29s-5.45-2.16-5.45-5.12v-28c0-3 1.84-5.13 5.45-5.13s5.36 2.16 5.36 5.29v6.4h8.89v-6.51c0-8.01-4.96-13.94-14.41-13.94zM40.27 71.67l-1.69 9.85-1.68-9.85-5.52-27.07H18v53.34h8.89V59.26l2.08 11.61 5.37 27.07h8.49l5.36-27.07 2.08-11.61v38.68h8.89V44.6H45.79l-5.52 27.07z"/>
</svg> </div>
                        <div class="flexfooter__logo-text flexfooter__logo-text--rocksolid">
                            <span class="flexfooter__logo-text-rocksolid-top-en">
                                Rocksolid
                            </span>
                            <br/>
                            <span class="flexfooter__logo-text-rocksolid-bottom-en">
                                Guarantee
                            </span>
                        </div>
                    </div>
                    <div class="flexfooter__content">
                        <div class="flexfooter__text text--small">
                            <div>Inspired gear. Informed advice.</div>
                            <div>Members get it.</div>
                        </div>
                    </div>
                </a>
            </div>


                    <div class="flexfooter__block flexfooter__block--pricematch">
                        <a class="u-no-decoration" href="/en/explore/membership">
                            <div class="flexfooter__logo">
                                <div class="flexfooter__logo-image flexfooter__logo-image--membership">
                                    <img src="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/membership-logo.png" alt="membership logo" height="62px" />
                                </div>
                                <div class="flexfooter__logo-text flexfooter__logo-text--membership">
                                    <img src="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/images/membership-en.png" alt="Members get more" height="62px" />
                                </div>
                            </div>
                            <div class="flexfooter__content flexfooter__content--membership">
                                <div class="flexfooter__text text--small">
                                    Special perks, discounts and services
                                </div>
                            </div>
                        </a>
                    </div>




            <div class="flexfooter__block">



                        <a class="u-no-decoration" href="/en/explore/in-store-pickup">
                            <div class="flexfooter__logo">
                                <div class="flexfooter__logo-image flexfooter__logo-image--mec"><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 110.01 133.57" style="enable-background:new 0 0 110.01 133.57;" xml:space="preserve">
    <style type="text/css">
        .st0{fill:#FFFFFF;}
        .st1{fill:#12A84B;}
    </style>
    <rect x="25.95" y="73.03" class="st0" width="58.62" height="53.9"/>
    <path class="st1" d="M107.13,41.95h-14.1V12.96h-0.02l-9.63-9.63v9.63h0V3.34h-56.6V3.33l-0.01,0.01h-0.01v0.01l-9.61,9.61h-0.02
        v28.99H2.97v88.81h104.11h0.05V41.95z M81.18,85.36H28.15v-10.6h53.03V85.36z M51.62,92.05v32.65H28.15V92.05H51.62z M57.71,124.7
        V92.05h23.47v32.65H57.71z M26.84,13.06h56.47v28.89H26.84V13.06z"/>
</svg>
</div>
                                <div class="flexfooter__logo-text flexfooter__logo-text--spu">
                                    <span class="flexfooter__logo-text-spu-top">
                                        Free store
                                    </span>
                                    <span class="flexfooter__logo-text-spu-bottom">
                                        pickup
                                    </span>
                                </div>
                            </div>
                            <div class="flexfooter__content">
                                <div class="flexfooter__text">
                                    <p class="text--small">
                                        Order online, get it at your local MEC and pay no shipping.
                                    </p>
                                </div>
                            </div>
                        </a>


            </div>
            <div class="flexfooter__block flexfooter__block--getemail">
                <div class="flexfooter__logo">
                    <div class="flexfooter__logo-image flexfooter__logo-image--email "><svg width="21" height="16" viewBox="0 0 21 16" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M16.4719 7.56721C15.6844 8.19065 13.9781 9.43752 11.4187 11.275L11.0906 11.5375C10.5656 11.9313 10.1719 12.2266 9.84375 12.3906C9.31875 12.7188 8.82656 12.85 8.4 12.85C7.94062 12.85 7.48125 12.7188 6.95625 12.4235C6.62812 12.2594 6.23437 11.9641 5.70937 11.5703L5.38125 11.275C2.72344 9.3719 1.05 8.12502 0.328125 7.56721C0.2625 7.5344 0.164062 7.5344 0.0984375 7.56721C0.0328125 7.60002 0 7.66565 0 7.73127V14.425C0 14.8844 0.13125 15.2453 0.459375 15.5406C0.754687 15.8688 1.11562 16 1.575 16H15.225C15.6516 16 16.0125 15.8688 16.3406 15.5406C16.6359 15.2453 16.8 14.8844 16.8 14.425V7.73127C16.8 7.66565 16.7344 7.60002 16.6687 7.5344C16.6031 7.50159 16.5375 7.50159 16.4719 7.56721ZM8.4 11.8C8.10469 11.8 7.74375 11.6688 7.35 11.4063C7.0875 11.275 6.75937 11.0453 6.33281 10.6844L6.00469 10.4547C3.31406 8.48596 1.47656 7.14065 0.525 6.38596L0.295312 6.2219C0.0984375 6.09065 0 5.86096 0 5.59846V4.97502C0 4.54846 0.13125 4.18752 0.459375 3.8594C0.754687 3.56409 1.11562 3.40002 1.575 3.40002H15.225C15.6516 3.40002 16.0125 3.56409 16.3406 3.8594C16.6359 4.18752 16.8 4.54846 16.8 4.97502V5.59846C16.8 5.86096 16.7016 6.09065 16.5047 6.2219L16.3406 6.35315C15.3891 7.10784 13.5516 8.48596 10.7953 10.4547L10.4672 10.6844C10.0078 11.0453 9.67969 11.275 9.45 11.4063C9.02344 11.6688 8.6625 11.8 8.4 11.8Z" fill="#191919"/>
    <path d="M20.4 3.2C20.4 4.96731 18.9673 6.4 17.2 6.4C15.4327 6.4 14 4.96731 14 3.2C14 1.43269 15.4327 0 17.2 0C18.9673 0 20.4 1.43269 20.4 3.2Z" fill="#087632"/>
    <path d="M17.5752 4.79999V1.39679H17.2632C17.2408 1.52479 17.1992 1.63039 17.1384 1.71359C17.0776 1.79679 17.0024 1.86239 16.9128 1.91039C16.8264 1.95839 16.7288 1.99199 16.62 2.01119C16.5112 2.02719 16.3992 2.03519 16.284 2.03519V2.36159H17.1672V4.79999H17.5752Z" fill="white"/>
</svg></div>
                    <div class="flexfooter__logo-text flexfooter__logo-text--allout">Get MEC Email</div>
                </div>
                <div class="flexfooter__content">
                    <div class="flexfooter__text--getemail">
                        <p class="text--small">
                            Inspiration. News. Gear lust.
                        </p>
                        <a href="/en/signup" class="btn btn-primary">Sign me up</a>
                    </div>
                </div>
            </div>
        </div><!-- flexfooter__container -->
    </div>
</div>


<div class="back-to-top">
    <a class="back-to-top__link" href="#top" title="Back to top">
        <i class="back-to-top__icon icon-angle-up icon-3x" aria-hidden="true"></i>
        <span class="back-to-top__label">Back to top</span>
    </a>
</div></div>
    <div class="footer__middle">
        <div class="footer__container">
            <div class="footer__row">





<div class="footer__content footer__content--promo">
    <p class="footer__title">MEC, Since 1971</p>
    <p>
        The place Canadians trust for outdoor advice. You'll find real-world experience, decades of outdoor knowledge, and exceptional products that won't ever let you down.
        <a class="footer__link" href="/en/explore/about-mec/">Read more</a>
    </p>
</div>
<div class="footer__content footer__content--links">

    <nav id="nav" role="navigation" class="treecordion treecordion--flex treecordion--flex-md clearfix" data-accordion>
        <ul role="tree" class="treecordion__control footer__control" id="treecordion-body">

        <li role="treeitem" aria-expanded="true" aria-selected="false" class="treecordion__branch footer__branch js-accordion-branch">
                <div class="treecordion__container footer__link-container">
                    <a href="/en/explore/about-mec" class="treecordion__branch__link footer__branch__link footer__link">About MEC</a>
                    <a href="#" class="treecordion__toggle footer__toggle pull-right footer__link js-accordion-branch-toggle" role="button" aria-controls="assortment-branch-About-MEC-Footer-link">
                        <span class="sr-only js-branch-toggle-label">Open</span>
                        <span class="sr-only">subcategories</span>
                        <i class="icon-plus treecordion__icon footer__icon js-accordion-branch-icon" aria-hidden="true"></i>
                    </a>
                </div>
                <ul class="treecordion__branch__control footer__branch__control js-accordion-branch-control" role="group" id="assortment-branch-About-MEC-Footer-link" aria-hidden="true">
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/media" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Media</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/careers" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Working here</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/stores" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Stores</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/contact-us" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Contact us</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/sustainability-innovation" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Sustainability</a>
                    </li>
                    </ul>
            </li>
        <li role="treeitem" aria-expanded="true" aria-selected="false" class="treecordion__branch footer__branch js-accordion-branch">
                <div class="treecordion__container footer__link-container">
                    <a href="/en/explore/support" class="treecordion__branch__link footer__branch__link footer__link">Support</a>
                    <a href="#" class="treecordion__toggle footer__toggle pull-right footer__link js-accordion-branch-toggle" role="button" aria-controls="assortment-branch-Support---Footer-link">
                        <span class="sr-only js-branch-toggle-label">Open</span>
                        <span class="sr-only">subcategories</span>
                        <i class="icon-plus treecordion__icon footer__icon js-accordion-branch-icon" aria-hidden="true"></i>
                    </a>
                </div>
                <ul class="treecordion__branch__control footer__branch__control js-accordion-branch-control" role="group" id="assortment-branch-Support---Footer-link" aria-hidden="true">
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/shipping-info" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Shipping information</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/returns-and-guarantee" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Returns and guarantee</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/price-protection" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Price matching and protection</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/corporate-and-group-sales" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Corporate and group sales</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/mec-affiliate-program" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">MEC affiliate program</a>
                    </li>
                    </ul>
            </li>
        <li role="treeitem" aria-expanded="true" aria-selected="false" class="treecordion__branch footer__branch js-accordion-branch">
                <div class="treecordion__container footer__link-container">
                    <a href="/en/my-account" class="treecordion__branch__link footer__branch__link footer__link">My account</a>
                    <a href="#" class="treecordion__toggle footer__toggle pull-right footer__link js-accordion-branch-toggle" role="button" aria-controls="assortment-branch-My-Account---Footer-link">
                        <span class="sr-only js-branch-toggle-label">Open</span>
                        <span class="sr-only">subcategories</span>
                        <i class="icon-plus treecordion__icon footer__icon js-accordion-branch-icon" aria-hidden="true"></i>
                    </a>
                </div>
                <ul class="treecordion__branch__control footer__branch__control js-accordion-branch-control" role="group" id="assortment-branch-My-Account---Footer-link" aria-hidden="true">
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/my-account/address-book" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Change address</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/my-account/orders" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Order history</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/my-account/email-preferences" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Email preferences</a>
                    </li>
                    <li role="none" class="treecordion__leaf footer__leaf">
                        <a role="treeitem" href="/en/explore/gift-cards" tabindex="-1" class="treecordion__leaf__link footer__leaf__link footer__link js-accordion-leaf-link">Gift cards</a>
                    </li>
                    </ul>
            </li>
        </ul>
    </nav>
</div>
<div class="footer__content footer__content--categories ">
    <ul class="list">
        <li class="footer__list__item">
                <a href="/en/explore/membership" class="footer__branch__link footer__link footer__link-container">Membership</a>
            </li>
        <li class="footer__list__item">
                <a href="/en/explore/outdoor-impact" class="footer__branch__link footer__link footer__link-container">Outdoor impact</a>
            </li>
        <li class="footer__list__item">
                <a href="/en/blog" class="footer__branch__link footer__link footer__link-container">Blog</a>
            </li>
        <li class="footer__list__item">
                <a href="/en/gearswap" class="footer__branch__link footer__link footer__link-container">Gear Swap</a>
            </li>
        <li class="footer__list__item">
                <a href="/en/explore/learn" class="footer__branch__link footer__link footer__link-container">Learn</a>
            </li>
        </ul>
</div>
</div>
        </div>
    </div>
    <div class="footer__bottom">













<div class="footer__container">





    <div class="footer__row footer__row--connect ">

            <div class="footer__block footer__block--chat js-livechat-init qa-footer__livechat-block hidden">
                <span class="footer__connect-label footer__content--chat">
                    <span class="u-nowrap">
                        <svg viewBox="0 0 28 28" class="livechat-svg"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g fill="#ffffff">
    <path d="M14,25.5 C12.4,25.5 10.8,25.2 9.4,24.7 L4.5,27.5 L4.5,21.9 C2,19.6 0.5,16.5 0.5,13 C0.5,6.1 6.5,0.5 14,0.5 C21.5,0.5 27.5,6.1 27.5,13 C27.5,19.9 21.5,25.5 14,25.5 L14,25.5 Z M9,11.5 C8.2,11.5 7.5,12.2 7.5,13 C7.5,13.8 8.2,14.5 9,14.5 C9.8,14.5 10.5,13.8 10.5,13 C10.5,12.2 9.8,11.5 9,11.5 L9,11.5 Z M14,11.5 C13.2,11.5 12.5,12.2 12.5,13 C12.5,13.8 13.2,14.5 14,14.5 C14.8,14.5 15.5,13.8 15.5,13 C15.5,12.2 14.8,11.5 14,11.5 L14,11.5 Z M19,11.5 C18.2,11.5 17.5,12.2 17.5,13 C17.5,13.8 18.2,14.5 19,14.5 C19.8,14.5 20.5,13.8 20.5,13 C20.5,12.2 19.8,11.5 19,11.5 L19,11.5 Z"></path>
</g></g></svg>
                        <span class="footer__chat"> Chat with us</span>
                    </span>
                </span>
            </div>

        <div class="footer__block footer__block--contact">
            <span class="footer__connect-label footer__content--contact">


                    <a href="/en/explore/support"  class="footer__link" >Help Centre</a>


            </span>
        </div>
        <div class="footer__block footer__block--connect">
            <span class="footer__content footer__content--connect footer__connect-label">
                Connect with us
            </span>
            <ul class="list list--icons list--icons-social">
                <li class="list__item">
                    <a class="link--social-icon footer__link" href="http://www.facebook.com/mec" target="_blank">
                        <span class="sr-only">
                        Opens facebook in a new tab
                    </span>
                        <i class="footer__connect-icon icon-facebook" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a class="link--social-icon footer__link" href="http://twitter.com/mec" target="_blank">
                        <span class="sr-only">
                        Opens twitter in a new tab
                    </span>
                        <i class="footer__connect-icon icon-twitter" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a class="link--social-icon footer__link" href="http://www.youtube.com/mecvideos" target="_blank">
                        <span class="sr-only">
                        Opens youtube in a new tab
                    </span>
                        <i class="footer__connect-icon icon-youtube" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a class="link--social-icon footer__link" href="http://www.pinterest.com/mec" target="_blank">
                        <span class="sr-only">
                        Opens pinterest in a new tab
                    </span>
                        <i class="footer__connect-icon icon-pinterest" aria-hidden="true"></i>
                    </a>
                </li>
                <li class="list__item">
                    <a class="link--social-icon footer__link" href="https://www.instagram.com/mec/" target="_blank">
                        <span class="sr-only">
                        Opens instagram in a new tab
                    </span>
                        <i class="footer__connect-icon icon-instagram" aria-hidden="true"></i>
                    </a>
                </li>
            </ul>
        </div>


<div class="feedback-tab">
    <div
        class="js-react-component"
        data-mec-react-component="FeedbackTab"
    >
    </div>
</div>
    </div>


    <div class="footer__row js-session-check">
        <div class="footer__block footer__block--bottom">
            <p class="text--terms">
                <a class="footer__link" href="/en/explore/privacy-policy">Privacy policy</a>
                <a class="footer__link" href="/en/explore/terms-of-use">Terms of use</a>
                <a class="footer__link" href="/en/explore/accessible-member-service">Accessibility</a>
                <a class="footer__link" href="/en/explore/website-cookie-policy">Cookie policy</a>
            </p>
            <p class="text--copyright u-cursor--pointer js-session-check-toggle">


                &copy; 2021. All rights reserved. The MEC logo is a registered trademark of MEC Mountain Equipment Company Ltd.
            </p>
            <div id="session-id-display" class="h6 u-no-margin js-session-check-wrapper">
                <span class="js-session-check-display"></span>
                <span class="js-session-feature-display"></span>
            </div>
        </div>
    </div>
</div>
</div>



<div id="js-react-modal-portal" class="js-react-component" data-mec-react-component="ModalWrapper"></div>





</footer>
</div>


	<div id="nav-vertical-container"
		class="js-react-component nav-vertical-container offcanvas offcanvas--right offcanvas--offset offcanvas--menu"
		aria-expanded="false"
		aria-hidden="true"
		data-mec-react-component="NavVertical"
		data-mec-react-data='{"location":"global"}'
		>
	</div>

	<div class="backdrop" id="backdrop"></div>

	<form name="accessiblityForm">
		<input type="hidden" id="accesibility_refreshScreenReaderBufferField" name="accesibility_refreshScreenReaderBufferField" value=""/>
	</form>
	<div id="ariaStatusMsg" class="skip" role="status" aria-relevant="text" aria-live="polite"></div>

	<script type="text/javascript">
    /*<![CDATA[*/


    var ACC = {config: {}};
    ACC.config.siteUrlPrefix = "/en/";
    ACC.config.encodedContextPath = "/en";
    ACC.config.commonResourcePath = "https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive";
    ACC.config.CSRFToken = "a324047d-ea4a-4a2d-aa72-2af0187da702";

    ACC.autocompleteUrl = '/en/search/autocompleteSecure';



    var MEC = MEC || {};
    MEC.data = {
        promotions: {},
        pageCategory: "productLayoutPage",
        plpProductsData: null,
        content: {"heroes":[{"id":"New-for-fall-homepage-hero-banner","fallback":false,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h7d/h2c/8995068444702/lifestyle-apparel-v2.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h7d/h2c/8995068444702/lifestyle-apparel-v2.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h7d/h2c/8995068444702/lifestyle-apparel-v2.jpg?w=800&h=800&auto=format&q=60","altText":"lifestyle apparel v2.jpg"}],"logo":null,"headline":"New for fall","paragraph":"Just landed: brand-new gear that’ll transition into the chilly season without a hitch. ","ctas":[{"text":"Shop what’s new","url":"/en/products/c/100?f=featureCollection%3Anew"}]},{"id":"New-for-fall-homepage-hero-banner-test","fallback":false,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h7d/h2c/8995068444702/lifestyle-apparel-v2.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h7d/h2c/8995068444702/lifestyle-apparel-v2.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h7d/h2c/8995068444702/lifestyle-apparel-v2.jpg?w=800&h=800&auto=format&q=60","altText":"lifestyle apparel v2.jpg"}],"logo":null,"headline":"New for fall","paragraph":"Just landed: brand-new gear that’ll transition into the chilly season without a hitch. ","ctas":[{"text":"Shop what’s new","url":"/en/products/c/100?f=featureCollection%3Anew"}]},{"id":"VRE","fallback":false,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h40/h78/9089801224222/19-165-VRE-Ph2-web-D11-homepg-hero-5x2-Mar4.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h40/h78/9089801224222/19-165-VRE-Ph2-web-D11-homepg-hero-5x2-Mar4.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h40/h78/9089801224222/19-165-VRE-Ph2-web-D11-homepg-hero-5x2-Mar4.jpg?w=800&h=800&auto=format&q=60","altText":"19_165_VRE_Ph2_web_D11_homepg_hero_5x2_Mar4.jpg"}],"logo":null,"headline":"Vancouver, your new store is here","paragraph":"Bigger and better than ever. Check out the flagship store in Olympic Village.","ctas":[{"text":"Vancouver Store Now Open","url":"https://www.mec.ca/en/p/vancouverrelocation"}]},{"id":"back-to-school-homepage-hero","fallback":false,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h3d/h81/8991154536478/18-CM-43-BTS-web-5x2-Youth-Kids.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h3d/h81/8991154536478/18-CM-43-BTS-web-5x2-Youth-Kids.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h3d/h81/8991154536478/18-CM-43-BTS-web-5x2-Youth-Kids.jpg?w=800&h=800&auto=format&q=60","altText":"18_CM_43_BTS_web_5x2_Youth-Kids.jpg"}],"logo":null,"headline":"Back to school","paragraph":"Springy shoes, comfy clothes and durable backpacks so you’ll be ready when the first bell rings.","ctas":[{"text":"Shop the collection","url":"/en/products/c/100?f=CFSeasonalCollections%3ABack+to+school+collection"}]},{"id":"quebec-homepage-hero-banner","fallback":false,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h94/hf2/8991154602014/hero-5x2.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h94/hf2/8991154602014/hero-5x2.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h94/hf2/8991154602014/hero-5x2.jpg?w=800&h=800&auto=format&q=60","altText":"hero 5x2.jpg"}],"logo":null,"headline":"Quebec members, we thank you!","paragraph":"In 2003, MEC opened its first store in Québec. Today, MEC has more than 850 000 Québécois members. Thank you for taking part in this great movement of outdoor enthusiasts. ","ctas":[{"text":"Thank you","url":"/en/p/Quebecanniversary"}]},{"id":"comp_00008IC4","fallback":true,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/hf6/hb4/9029438013470/19-CM-146-April-Free-Ship-web-5x2-Apr5-EN.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/hf6/hb4/9029438013470/19-CM-146-April-Free-Ship-web-5x2-Apr5-EN.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/hf6/hb4/9029438013470/19-CM-146-April-Free-Ship-web-5x2-Apr5-EN.jpg?w=800&h=800&auto=format&q=60","altText":"19_CM_146_April-Free-Ship_web_5x2_Apr5_EN.jpg"}],"logo":null,"headline":"All orders ship free","paragraph":"A spring surprise for MEC members: free shipping on everything until April 16. *Some (just a few) conditions apply.","ctas":[{"text":"Start shopping","url":"/en/products/c/100"}]},{"id":"trail-hike-hero-vre-relocation-default","fallback":true,"images":[{"highRes":"https://cdn.mec.ca/medias/sys_master/images/images/h44/h06/9088569049118/20-001-TrailHike-Web-D2-homepage-hero-5x2-Feb20.jpg","placeholder":"https://mec.imgix.net/medias/sys_master/images/images/h44/h06/9088569049118/20-001-TrailHike-Web-D2-homepage-hero-5x2-Feb20.jpg?w=100&h=100&auto=format&q=40","fallback":"https://mec.imgix.net/medias/sys_master/images/images/h44/h06/9088569049118/20-001-TrailHike-Web-D2-homepage-hero-5x2-Feb20.jpg?w=800&h=800&auto=format&q=60","altText":"20_001_TrailHike_Web_D2_homepage_hero_5x2_Feb20.jpg"}],"logo":null,"headline":"The trail is the answer","paragraph":"Feet on the ground, eyes on the horizon. Today’s to-do list? Focus and put one foot in front of the other. ","ctas":[{"text":"Shop the hike collection","url":"/en/p/hike"}]}]},
        member: {}
    };



    MEC.Config = ACC.config;
    MEC.Config.responsiveImageHosts = {"cdn.mec.ca":"mec.imgix.net","cdnstage.mec.ca":"mecuat.imgix.net","hy-int.mec.ca":"mec-hy-int.imgix.net","hy-test.mec.ca":"mec-hy-test.imgix.net","img.youtube.com":"mecyoutube.imgix.net","meccms.staging.wpengine.com":"meccms-staging.imgix.net","meccms.wpengine.com":"meccms.imgix.net","stage.mec.ca":"mec-stage.imgix.net","stage-upg.mec.ca":"mec-stage-upg.imgix.net","test-upg.mec.ca":"mec-test-upg.imgix.net","aws-test.mec.ca":"mec-aws-test.imgix.net","www.mec.ca":"mec.imgix.net"};
    MEC.Config.responsiveImageUrlBuilder = "ImgixFolderUrlBuilder";
    MEC.Config.canadaPostAddressCompleteAPIKey = "ZJ44-FH13-UJ97-KW17";
    MEC.Config.Urls = {
        "cart": "/en/cart",
        "checkout": "/en/checkout",
        "stores": "/en/stores",
        "base": "https://www.mec.ca"
    };


        MEC.Config.languages = [{"locale":"en","active":true,"label":"English","url":"https://www.mec.ca/en/product/5050-315/Quandary-Pants"},{"locale":"fr","active":false,"label":"Français","url":"https://www.mec.ca/fr/product/5050-315/Pantalon-Quandary"}];

    MEC.Config["storesApiCacheExpiry"] = "10";

    MEC.Config["removeDisplayDiscountedGroupModal"] = "false";

    MEC.Config["clientId"] = "mobile_android";

    MEC.Config["bundleSaveProducts"] = "6001-862,6010-622,6010-626,6010-627,6010-631,6010-632,6010-635,6010-629,6010-637,6000-376,6010-625,6010-628,6010-634,6010-636,6010-630,6010-638,6003-128,6011-283,6013-502,6013-503,6007-791,6012-991,5001-785,5038-340,6013-125,6013-126,6013-500,6013-501,4003-253,5051-479,6012-425,6012-426,6012-427,6012-428,6012-430,6012-992,5061-017,6011-285,6013-504,5006-539,6014-455,6001-311,6001-315,6001-317,6001-318,5052-214,5052-217,5052-219,5057-899,5057-901,5060-250,6000-464,6000-471,5057-673,5057-676,5057-677,6000-468,6000-469,6000-470,6008-720,6008-724,6008-725,6008-727,6008-728,6008-736,6008-737,6008-750,6008-753,6008-921,6008-922,6000-970,6013-601,6000-973,6000-974,5063-945,6000-436,6000-302,6000-303,6000-132,6004-603,6010-285,6013-564,5063-097,6003-130,6003-145,6003-148,6003-131,6003-132,6003-133,6010-928,6000-124,6003-134,6000-985,6014-528,6000-885,6000-906,6010-790,6000-259,6000-268,6000-260,6000-263,6000-269,6000-272,6014-526,6012-171,6012-172,1807-460,4000-410,6010-678,5063-546,5063-552,6011-472,4013-718,4013-746,5008-962,5063-559,5063-560,5063-555,5063-556,5063-557,5063-558,5053-164,5037-746,5046-884,5046-885,6005-367,6005-369,6005-370,6005-371,6009-312,6009-313,6009-314,6009-369,6009-370,6009-372,6009-377,6009-379,6011-773,5059-386,5059-392,6011-356,6011-357,6013-925,6013-926,6013-927,6013-928,6013-930,6013-931,5040-434,5043-074,6014-246,5039-681,5039-682,5039-684,5039-685,5057-789,6005-463,6005-464,6014-031,6014-162,4003-682,6014-163,6001-958,6003-263,5033-786,5033-787,5033-790,5049-692,5049-693,5058-550,5060-352,5063-549,5064-702,5064-703,6002-346,6002-470,6002-475,6010-606,6014-476,6014-477,6014-478,6012-475,6002-869,6002-308,6002-462,6002-883,6003-775,6003-779,6003-781,6003-782,6003-783,6007-803,6007-809,6010-782,6010-783,6010-784,6010-785,6011-004,6011-011,6011-013,6014-484,6001-784,6002-410,6002-850,6002-865,6002-412,6002-414,6010-450,6011-009,6011-019,6011-021,6014-481,6014-482,6014-487,6011-022,5035-996,5035-997,4016-661,4016-662,6006-095,6006-098,6006-099,6006-100,6010-339,6010-342,6010-344,5007-068,6011-858,5029-100,6013-774,6004-420,5043-636,5048-217,5050-030,5061-470,6004-929,6004-930,6004-931,6004-932,6009-020,6009-021,6009-022,6009-133,5016-843,5047-909,6004-414,6004-402,6004-408,6004-409,6004-410,6004-435,6004-438,6004-439,6004-441,6004-443,6004-445,6009-353,6009-354,6009-355,6009-356,6009-357,6013-291,6013-292,0101-030,6007-158,5044-322,5006-727,0101-022,5027-146,0106-088,6007-157,6007-159,6008-927,5029-080,5035-129,5048-916,5048-933,5048-934,5048-937,5048-939,5048-948,6005-096,5049-291,5049-296,5049-297,5049-298,5049-299,5049-301,5049-303,5049-304,5049-305,5049-306,5049-307,5049-308,5049-309,5034-827,5046-569,5056-956,5056-963,5062-368,5063-244,5063-255,5063-265,5063-270,5063-271,5064-479,6008-397,6008-398,6008-400,6008-401,6008-402,6008-404,5054-348,5060-234,5060-239,5060-240,5060-241,5060-242,5061-031,6002-478,6002-483,6002-864,6002-867,6011-087,6011-089,5057-071,6001-661,6001-948,6001-953,6001-956,6001-963,6001-969,5057-073,5057-074,6001-951,6001-659,6001-660,6014-496,6014-497,6014-498,6014-499,6012-501,6012-502,6012-526,6012-528,6012-533,6012-534,5059-999,6000-051,6000-053,6003-439,6003-440,6003-441,6012-776,5032-852,5036-297,5036-298,5036-299,5040-931,5055-886,5055-888,5058-314,5060-884,5060-887,5060-890,5060-891,6001-511,6006-389,6006-399,6006-402,6008-164,6008-175,6008-177,6008-179,6008-178,6008-759,6008-760,6009-216,6009-218,6009-219,6009-220,6009-246,6009-247,6009-248,6013-646,6013-648,6013-717,6013-718,5039-455,5039-464,5039-465,5039-466,4001-913,4017-938,5007-785,5036-149,5053-131,6009-132,6013-831,6013-832,6013-833,6013-834,6013-835,6013-836,6013-837,6013-838,6013-839,6013-840,5049-935,5064-472,6001-944,6001-946,6011-463,6012-822,5053-593,5053-596,5053-597,5053-598,5053-600,5053-604,5059-193,5059-194,5059-195,5059-196,6000-425,6000-426,6004-905,6004-909,6004-910,6004-911,6004-912,6009-162,6009-163,6011-928,6011-929,6011-931,6011-932,6011-933,6011-934,6011-930,6012-180,6012-181,6012-182,6012-183,6012-184,6012-185,6012-186,6012-187,6012-188,6012-189,6012-190,6012-191,6012-192,6012-193,6012-194,6012-195,6012-196,6012-197,6012-198,6012-199,6012-200,6012-201,6012-202,5059-326,5059-327,5059-328,5061-619,5061-620,5061-621,6000-174,6002-571,6008-835,6008-837,6008-838,6008-839,6008-841,6010-327,6013-238,6013-239,6013-240,6013-241,6013-242,6013-243,6012-783,6012-770,6012-762,6012-857,6012-773,6012-774,6012-772,6012-778,6012-781,6012-765,6012-766,6012-767,6012-768,6012-785,6012-763,6012-764,6012-769,6014-000,5061-787,4009-671,5020-289,5035-754,5049-787,5058-451,5058-452,5006-651,5051-337,5061-089,5061-091,6009-074,6013-747,6000-773,6000-806,6000-808,6013-765,6014-074,0199-554,6005-157,6005-158,5058-432,6003-175,6003-176,6003-085,6013-024,6012-334,6012-423,4003-774,4003-778,4003-779,4004-968,5008-369,5008-370,6013-978,6013-980,5013-171,6012-318,5024-535,5024-536,5024-537,4016-488,4017-293,5023-260,5029-882,5031-024,5041-774,5041-878,5049-282,5049-817,5049-818,5049-822,5049-918,5050-110,6005-860,5019-747,5030-484,5031-696,5038-471,5038-476,5044-386,5044-391,5044-392,5044-395,5050-092,6002-431,6002-432,6002-435,6002-436,6002-437,6002-438,6006-611,6006-612,5023-201,5030-546,5009-519,5017-290,5017-869,5020-822,5023-159,5029-965,5036-168,5044-447,5055-496,5055-547,5058-512,5061-754,6002-440,6010-368,6014-285,5028-209,5031-779,5032-165,5036-361,5044-500,5053-207,5053-230,5044-394,5023-169,5045-133,5024-830,6010-896,5039-088,5000-259,5000-261,5010-442,5017-372,5017-948,5017-949,5023-606,5023-740,5038-477,5038-483,5041-093,5041-094,5041-095,5041-096,5041-097,5045-520,5049-279,5056-517,5061-575,6002-429,6002-430,6008-989,5050-102,5050-103,5050-104,6011-101,6011-102,6011-106,5030-236,5039-180,5039-181,5039-182,5039-185,5055-550,5056-378,5056-381,6011-105,6011-505,5033-228,5033-229,5036-488,5052-660,5056-507,5056-509,5056-510,5056-511,6006-339,6006-341,6006-343,6011-504,6012-251,6012-252,6012-254,5051-610,5052-661,6011-506,6011-507,5035-554,4006-361,4010-597,4010-601,4010-603,4010-608,4010-609,4010-623,4010-624,4010-630,4010-638,4010-639,4010-642,4010-644,4010-645,4010-646,4010-647,4010-650,4010-652,4010-656,4010-657,4010-658,4014-785,5034-347,5044-375,5044-377,5044-378,5052-398,6012-253,4017-119,4017-132,4005-151,4005-159,4005-177,4005-185,4005-202,4008-170,4010-619,4010-622,4011-053,4014-803,4015-918,4015-920,4015-922,4015-923,4015-924,4015-925,4015-931,4015-933,4015-934,4015-949,4019-070,5000-236,5000-290,5005-903,5009-439,5022-225,5022-310,5022-449,5029-473,5036-489,5036-490,5036-491,5050-021,5050-024,5050-026,5051-782,6010-955,6010-956,6014-231,5000-407,5003-091,4007-592,4007-593,4008-275,4008-276,4010-567,4012-806,4015-850,4019-075,5006-795,5006-797,5009-422,5012-995,5031-233,6010-954,4019-071,4012-549,5024-649,5024-747,6014-241,5058-041,5058-042,5058-043,6012-809,6002-322,0808-022,0808-097,4003-969,4003-970,5041-524,6003-531,6003-533,6004-392,6004-394,6004-395,6010-856,6010-857,6010-858,6010-859,6010-861,6004-388,6004-389,6004-390,6004-391,6004-397,6004-399,6004-400,6004-405,5054-738,6013-638,6012-608,6004-609,5060-338,5060-340,6010-334,6010-341,6010-343,6010-870,6010-871,6010-872,6010-873,6010-874,4018-728,4018-729,5006-243,5038-996,5061-406,5061-408,5061-409,5061-410,6004-964,4018-723,4018-724,5006-225,5006-233,5006-234,5008-972,5008-975,5008-976,5008-978,5008-979,5008-980,5011-681,5017-014,5017-015,5044-136,6009-212,5006-235,5006-236,5006-237,5011-679,5014-345,4014-436,5025-064,6012-918,6001-489,6001-488,6001-490,6004-965,5007-619,5036-518,5036-523,5058-553,6008-930,5021-722,5021-723,5025-211,5027-003,5027-512,5027-513,5027-802,5028-970,5029-575,5030-485,5031-113,5033-788,5034-448,5035-689,5037-426,5038-641,5038-851,5041-394,5041-397,5041-398,5041-399,5041-401,5041-402,5041-403,5041-404,5041-405,5041-406,5041-407,5041-408,5041-409,5041-410,5041-411,5044-448,5044-449,5044-577,5044-586,5044-592,5044-825,5045-136,5045-530,5046-134,5048-210,5049-729,5050-190,5050-454,5050-670,5051-057,5054-703,5055-119,5055-656,5055-934,5057-451,5057-876,5060-254,5060-819,5061-272,5061-277,5061-347,5062-097,5062-100,6001-062,6004-928,6005-071,6006-878,4007-257,4007-259,5007-609,5024-672,5028-626,5036-965,5041-663,5041-664,5032-281,5032-282,5036-969,5036-971,5021-713,5009-270,5023-884,5025-880,5032-276,5032-277,1999-010,4013-389,5012-207,5032-275,5034-523,5047-358,5053-157,4004-175,4004-181,4004-182,4004-183,5007-617,5028-763,4004-177,5000-722,5000-918,5000-920,5002-730,5012-152,5027-908,5028-627,5030-461,5038-605,5044-400,5044-412,5049-858,5057-610,6005-073,6005-375,1903-087,1903-095,1903-152,5007-758,5007-760,5007-761,5007-762,5010-513,5010-514,5031-808,6009-360,4004-627,5027-798,5036-970,5047-308,6007-936,5007-612,5009-043,5018-708,5055-423,5052-733,4004-626,5001-129,5047-150,6005-070,4018-962,5024-437,5056-370,5056-371,5056-373,5056-375,5061-554,5061-557,5061-559,6003-152,6003-697,5016-629,5016-630,5016-631,5007-693,5010-302,5055-029,4007-727,4007-741,4009-447,4009-501,4013-965,4013-970,5023-526,5025-273,5025-274,5032-613,5032-651,5042-273,5042-275,5042-276,5042-277,5042-278";

    MEC.Config["requestUsersEndpoint"] = "false";

    MEC.Config["bikeCategories"] = "1528,1527,1529,1559,296,1780,1531";

    MEC.Config["searchDebounceRate"] = "80";

    MEC.Config["searchApiHost"] = "https://cdn.mec.ca";

    MEC.Config["copyPasteNewrelicEnabled"] = "false";

    MEC.Config["injectAppCache"] = "true";

    MEC.Config["googleRecaptchaSiteKey"] = "6LfWoCgTAAAAAFSPFD4Dy-6QMkGBJKc8bLpphywp";

    MEC.Config["resonanceCustomerIdFromBackend"] = "true";

    MEC.Config["googleInvisibleRecaptchaSiteKey"] = "6Lc2llMUAAAAAFHzwdsHP1PxIAaIpOacVbJwjTmz";

    MEC.Config["newRelicApplicationId"] = "25572410";

    MEC.Config["linkableMessageCycleSpeed"] = "5000";

    MEC.Config["newRelicLicenseId"] = "5dfbfbeddb";

    MEC.Config["adventuresApiDomain"] = "https://meccms.wpengine.com";

    MEC.Config["richRelevanceCdnUrl"] = "cdn.mec.ca";

    MEC.Config["clientSecret"] = "secret";


    MEC.features = {};

            MEC.features["enableBikeFreeShippingMessage"] = true;

            MEC.features["enableClientSideThrottle"] = true;

            MEC.features["enableCachingAbTestFeatureToggleSupplier"] = true;

            MEC.features["enableStoreInfoInNav"] = true;

            MEC.features["HI-12359_Refactored_Spu"] = true;

            MEC.features["ER-289-useEmailOnlyForFetchingSubscriptions"] = true;

            MEC.features["enableSplitFeatureToggleSupplier"] = true;

            MEC.features["treatmentConfig"] = true;

            MEC.features["Klaviyo_Hybris_Check_Subscription_Disabled"] = true;

            MEC.features["tc323-spuStoreSelection"] = true;

            MEC.features["enableRemovingAllParamsFromCanonicalURL"] = false;

            MEC.features["showStockInformationAtPdpWhenStoresBeingRelocated"] = false;

            MEC.features["enableUpdatedStockStatusLogic"] = false;

            MEC.features["enableSplitBuildVersion"] = true;

            MEC.features["enablePasswordResetConfirmationPage"] = true;

            MEC.features["enableShowHiddenFacets"] = false;

            MEC.features["hi-12474-fix-search-suggestion-issue"] = true;

            MEC.features["enableOutOfStockRecContainer_HI-12051"] = true;

            MEC.features["enableRichRelevance_HI-11421"] = true;

            MEC.features["HI-12502_BV_Upgrade"] = true;

            MEC.features["ER-214-Membership-update"] = true;

            MEC.features["includeOldMegaMenuUet"] = true;

            MEC.features["hi-10374-fix-sale-end-date-issue"] = false;

            MEC.features["enableEvaluateStoresRelocationFlow"] = true;

            MEC.features["hi-10264-promo-pricing"] = false;

            MEC.features["HI-12405_DefaultProductSwatchColour"] = true;

            MEC.features["enablePlpSpuShowAvailableColours__HI-12087"] = true;

            MEC.features["enableSelectedRegionsForCheckoutAddress"] = true;

            MEC.features["hi-12525-startCachingPosData"] = true;

            MEC.features["tc-608-gaStoreNameUpdate"] = true;

            MEC.features["enablePlpNoResults__HI-11905"] = true;

            MEC.features["enableFlexibleMerchboxes"] = false;

            MEC.features["hi-11369-orderSummaryComponent"] = true;

            MEC.features["enableAvailabilityModalCtas"] = true;

            MEC.features["enableServerSideRecaptcha"] = false;

            MEC.features["enableQualtricsFeedbackTab"] = true;

            MEC.features["hi-12314-guest-checkout-flag"] = false;

            MEC.features["enableCovid19Messages"] = true;

            MEC.features["facetValuesWithTopFacetValues"] = true;

            MEC.features["enableNoStoreStockCheckForWebOnlyProduct"] = false;

            MEC.features["hi-9982-fix-wishlist-removing-bug"] = true;

            MEC.features["hi-12480-memberNumberLog"] = false;

            MEC.features["EnableSpuFooterMessage_HI-11999"] = true;

            MEC.features["HI-11995_NewSpuCalculateFlag"] = true;

            MEC.features["hi-12013-stockStatusPromotionCondition"] = true;

            MEC.features["useMecCdnForFrontendLibs_HI-10327"] = true;

            MEC.features["enableBackendFindInStoreMessageLogicUpdatePDP_HI-12130"] = true;

            MEC.features["hi-12489-phoneNumberLenghtIssueFix"] = true;

            MEC.features["hi-12405_enablePlpSpuShowAvailableColoursBackend"] = true;

            MEC.features["hi-11487-addPromotionPriceToCartModal"] = true;

            MEC.features["enableCartCouponDetailsModal_HI-11595"] = true;

            MEC.features["hi-11197-promotionFeatureForMessagesFromHybris"] = true;

            MEC.features["enableNewCoText_HI-11939"] = true;

            MEC.features["Limited_time_offer_message_HI-12515"] = false;

            MEC.features["enableMonerisIframeLogging_HI-12270"] = true;

            MEC.features["enableRichRelevanceCDNProxy_HI-11899"] = true;

            MEC.features["hi-11629-specialOfferMessageForCoupon"] = true;

            MEC.features["enableCustomTextEditorForWCMS"] = true;

            MEC.features["hotjarAnalytics"] = false;

            MEC.features["tc-688-pipeCharRegex"] = false;

            MEC.features["enableNumericalI18n"] = true;

            MEC.features["Klaviyo_Hybris_Integration"] = true;

            MEC.features["enablePhoneNumberInFooter"] = false;

            MEC.features["enableFallbackToYvrStoreOnUserGeolocation"] = true;

            MEC.features["enableUseBaseProductFromProductUtil"] = true;

            MEC.features["useCustomQueryFacet"] = true;

            MEC.features["hi-10184-skuLevelSearchCondition-create-solr-facet"] = true;

            MEC.features["ER-295-50th_anniversary_logo"] = true;

            MEC.features["hi-11197-promotionFeatureForPromotionMessages"] = true;

            MEC.features["rememberStoreAvailability_HI-12093"] = true;

            MEC.features["hi-12379-displayShippingRestrictionOnCartPage"] = true;

            MEC.features["fixDefaultPriceInfoIssue"] = true;

            MEC.features["plpDefaultColourSelection_HI-12054"] = true;

            MEC.features["enableLiveChatInHelp"] = true;

            MEC.features["enableRemovingFrCharsFromRequstObj"] = false;

            MEC.features["hi-10050-checkHazardousForSpu"] = true;

            MEC.features["hi-11568-plpTopperBanner"] = true;

            MEC.features["enableUniqueIds_HI-12214"] = true;

            MEC.features["enableKeepingDeliveryAddressForNewMember"] = true;

            MEC.features["hiddenShippingProductTypes"] = true;

            MEC.features["hi-11419-spuBufferRangeForOverSizeProduct"] = true;

            MEC.features["pushPdpSpuData"] = true;

            MEC.features["hi-10105-usePreparedStatementToFindStocklevels"] = true;

            MEC.features["enableMyStoreBadge"] = true;

            MEC.features["enablePreciseStorePickupMessaging"] = true;

            MEC.features["enableIceChat__ER-255"] = false;

            MEC.features["enablePreOrderCtaOnPdp"] = false;

            MEC.features["enablePdpSpuMessage_HI-11911"] = true;

            MEC.features["enableSpuMessageAlgorithm"] = true;

            MEC.features["enableEmailOptInForExistingMembers"] = true;

            MEC.features["enablePrideLogo"] = false;

            MEC.features["enableMixedSpuMessage"] = true;

            MEC.features["enablePreciseStorePickupMessagingOnPDP"] = true;

            MEC.features["enableReactPLP-Price__HI-12445"] = true;

            MEC.features["enableCreditCardFieldOpenDefault_HI12499"] = true;

            MEC.features["hi-10947-redirectingAfterLogin"] = true;

            MEC.features["showMessageForRedirectedArchived"] = true;

            MEC.features["enablePromoCodeInput_HI-10917"] = true;

            MEC.features["hi-10739-fixColourLevelBadge"] = true;

            MEC.features["enableMonerisCOF"] = false;

            MEC.features["enableNewFavouriteStoreFlow"] = true;

            MEC.features["enableCanadaPostAddressComplete"] = true;

            MEC.features["skipValidationEmptyBatchSolr"] = true;

            MEC.features["hi-10797-enableNewReturnPolicy"] = true;

            MEC.features["mockABTesting"] = false;

            MEC.features["enableSpuFeature"] = true;

            MEC.features["disableAnalyticsInputClicks"] = true;

            MEC.features["front-end_bundle_version"] = false;

            MEC.features["enableWidePDP"] = false;

            MEC.features["hi-11572-promotion-id-in-datalayer"] = true;

            MEC.features["useCustomCMSLink"] = true;

            MEC.features["plpFacetAccordion"] = false;

            MEC.features["enableMultiFacetValueSplitter"] = true;

            MEC.features["enableSavingShippingInfoOnHybris"] = true;

            MEC.features["enableCheckoutFormValidationToGA_HI-11614"] = true;

            MEC.features["enableRemovingMembershipShare"] = true;

            MEC.features["enableFindInStoreMessageLogicUpdatePDP_HI-12130"] = true;

            MEC.features["checkAllStoresForInventory"] = true;

            MEC.features["fixMissingSelectedFacet"] = true;

            MEC.features["enableAbTestFramework"] = true;

            MEC.features["moveTrackingToTop_CD41"] = false;

            MEC.features["useCachedSalesRankData"] = false;

            MEC.features["enableShowMecStoresOnlyAvaiableForListing"] = true;

            MEC.features["hi-10267-onsale-filter"] = true;

            MEC.features["enableRedirectArchivedProducts"] = true;

            MEC.features["hi-12443-hitCustomizedMecAsConfigurablePopulator"] = true;

            MEC.features["enableStoresPageLocationButton"] = true;

            MEC.features["mobileMerchBoxRelocation"] = false;

            MEC.features["enableHeaderRewrite"] = true;

            MEC.features["hi-10185-skuLevelSearchCondition-solr-search-query"] = true;

            MEC.features["enableHandholdLoginExperience"] = true;

            MEC.features["enable3StoryHPComponent_HI-12351"] = false;

            MEC.features["hi-11390-addtionalMemberAddressModel"] = true;

            MEC.features["hi-12314-siteLocaleEn"] = true;

            MEC.features["tc-607-geolocationUetEvent"] = true;

            MEC.features["enableIgnorableVariantsInAvailabilityRules"] = false;

            MEC.features["pdpExpressDeliveryMessageAbTest"] = true;

            MEC.features["enableCheckoutCTATesting_HI-11468"] = true;

            MEC.features["enableMecCustomizedShippingRestrictions"] = true;

            MEC.features["cookiePolicyBanner"] = false;

            MEC.features["hi-10106-hide-clearance-text-for-certain-products"] = false;

            MEC.features["enableFilterButtonUpdates__HI-11907"] = false;

            MEC.features["ctaStyleInSuperComponent"] = true;


    MEC.Config.mediaUrl = "https://cdn.mec.ca";

    MEC.Config.monerisSubmitUrl = "https://www3.moneris.com/HPPtoken/index.php";

    MEC.isFullyAuthenticated = false;


    MEC.displayDiscountedGroupModal = false;


    MEC.locale = "en";



    MEC.data.nav = {"title":"Mec MegaMenu Root Node V2","uetTitle":"Mec MegaMenu Root Node V2","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Deals","uetTitle":"Deals","url":"#/clearance","image":"","skipSubNav":false,"features":{"horizontal":["noSubnav"],"vertical":["slide"]},"subnav":[{"title":"Women's deals","uetTitle":"Women's deals","url":"/en/gender/women%27s+unisex/products/c/100?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Jackets","uetTitle":"Jackets","url":"/en/gender/women%27s/products/clothing/jackets/c/1018?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"women's deals|jackets","label":"/en/gender/women%27s/products/clothing/jackets/c/1018?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Shirts","uetTitle":"Shirts","url":"/en/gender/women%27s/products/clothing/shirts-and-tops/c/1044?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"women's deals|shirts","label":"/en/gender/women%27s/products/clothing/shirts-and-tops/c/1044?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Pants","uetTitle":"Pants","url":"/en/gender/women%27s/products/clothing/bottoms/c/1002?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"women's deals|pants","label":"/en/gender/women%27s/products/clothing/bottoms/c/1002?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Fleece, hoodies and sweaters","uetTitle":"Fleece, hoodies and sweaters","url":"/en/gender/women%27s/products/clothing/fleece-hoodies-and-sweaters/c/271?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"women's deals|fleece, hoodies and sweaters","label":"/en/gender/women%27s/products/clothing/fleece-hoodies-and-sweaters/c/271?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Base layers","uetTitle":"Base layers","url":"/gender/women%27s/products/clothing/base-layers-and-underwear/c/1053?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"women's deals|base layers","label":"/gender/women%27s/products/clothing/base-layers-and-underwear/c/1053?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Skirts and dresses","uetTitle":"Skirts and dresses","url":"/en/products/clothing/skirts-and-dresses/c/1031?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"women's deals|skirts and dresses","label":"/en/products/clothing/skirts-and-dresses/c/1031?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"women's deals"}},{"title":"Men's deals","uetTitle":"Men's deals","url":"/en/gender/men%27s+unisex/products/c/100?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Jackets","uetTitle":"Jackets","url":"/en/gender/men%27s/products/clothing/jackets/c/1018?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"men's deals|jackets","label":"/en/gender/men%27s/products/clothing/jackets/c/1018?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Shirts","uetTitle":"Shirts","url":"/en/gender/men%27s/products/clothing/shirts-and-tops/c/1044?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"men's deals|shirts","label":"/en/gender/men%27s/products/clothing/shirts-and-tops/c/1044?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Pants","uetTitle":"Pants","url":"/en/gender/men%27s/products/clothing/bottoms/c/1002?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"men's deals|pants","label":"/en/gender/men%27s/products/clothing/bottoms/c/1002?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Fleece, hoodies and sweaters","uetTitle":"Fleece, hoodies and sweaters","url":"/en/gender/men%27s/products/clothing/fleece-hoodies-and-sweaters/c/271?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"men's deals|fleece, hoodies and sweaters","label":"/en/gender/men%27s/products/clothing/fleece-hoodies-and-sweaters/c/271?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Base layers","uetTitle":"Base layers","url":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/c/1053?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"men's deals|base layers","label":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/c/1053?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"men's deals"}},{"title":"Kids deals","uetTitle":"Kids deals","url":"/en/products/kids/c/1900?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Baby (0-2 yrs)","uetTitle":"Baby (0-2 yrs)","url":"/products/kids/baby/c/1901?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"kids deals|baby (0-2 yrs)","label":"/products/kids/baby/c/1901?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Toddler and child (2-7 yrs)","uetTitle":"Toddler and child (2-7 yrs)","url":"/products/kids/toddler-and-child/c/1942?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"kids deals|toddler and child (2-7 yrs)","label":"/products/kids/toddler-and-child/c/1942?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Youth (8-16 yrs)","uetTitle":"Youth (8-16 yrs)","url":"/en/products/kids/youth/c/2001?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"kids deals|youth (8-16 yrs)","label":"/en/products/kids/youth/c/2001?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Kids backpacks","uetTitle":"Kids backpacks","url":"/en/products/packs-and-bags/kids-backpacks/c/2144?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale&b=100-1900","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"kids deals|kids backpacks","label":"/en/products/packs-and-bags/kids-backpacks/c/2144?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale&b=100-1900"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"kids deals"}},{"title":"Footwear deals","uetTitle":"Footwear deals","url":"/en/products/footwear/c/1184?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shoes","uetTitle":"Shoes","url":"/en/products/footwear/shoes/c/1195?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"footwear deals|shoes","label":"/en/products/footwear/shoes/c/1195?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Boots","uetTitle":"Boots","url":"/en/products/footwear/boots/c/1189?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"footwear deals|boots","label":"/en/products/footwear/boots/c/1189?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Sandals","uetTitle":"Sandals","url":"/en/products/footwear/sandals/c/1192?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"footwear deals|sandals","label":"/en/products/footwear/sandals/c/1192?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Kids","uetTitle":"Kids","url":"/en/products/kids/c/1900?f=categorySelect%3A1983%3AcategorySelect%3A2049%3AcategorySelect%3A1936%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"footwear deals|kids","label":"/en/products/kids/c/1900?f=categoryselect%3a1983%3acategoryselect%3a2049%3acategoryselect%3a1936%3afeaturecollection%3aonclearance"}},{"title":"Socks","uetTitle":"Socks","url":"/en/products/footwear/socks/c/1203?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"footwear deals|socks","label":"/en/products/footwear/socks/c/1203?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"footwear deals"}},{"title":"Accessories","uetTitle":"Accessories","url":"/en/products/clothing/clothing-accessories/c/982?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hats","uetTitle":"Hats","url":"/en/products/clothing/clothing-accessories/headwear/c/993?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"accessories|hats","label":"/en/products/clothing/clothing-accessories/headwear/c/993?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Sunglasses","uetTitle":"Sunglasses","url":"/en/products/clothing/clothing-accessories/sunglasses/c/1171?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"accessories|sunglasses","label":"/en/products/clothing/clothing-accessories/sunglasses/c/1171?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Face masks","uetTitle":"Face masks","url":"/en/products/clothing/clothing-accessories/personal-protective-face-masks/c/8987?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"accessories|face masks","label":"/en/products/clothing/clothing-accessories/personal-protective-face-masks/c/8987?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Packs and bags","uetTitle":"Packs and bags","url":"/en/products/packs-and-bags/c/1326?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"accessories|packs and bags","label":"/en/products/packs-and-bags/c/1326?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"accessories"}},{"title":"Limited time offers","uetTitle":"Limited time offers","url":"/en/products/c/100?f=featureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Up to 25% off Fjallraven","uetTitle":"Up to 25% off Fjallraven","url":"/en/brand/fjallraven/products/clothing/c/981?f=featureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"limited time offers|up to 25% off fjallraven","label":"/en/brand/fjallraven/products/clothing/c/981?f=featurecollection%3aonsale"}},{"title":"Up to 30% off Bug Protection","uetTitle":"Up to 30% off Bug Protection","url":"en/products/camping-and-hiking/health-and-safety/bug-spray-and-bug-nets/c/1208","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"limited time offers|up to 30% off bug protection","label":"en/products/camping-and-hiking/health-and-safety/bug-spray-and-bug-nets/c/1208"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"limited time offers"}},{"title":"Activities","uetTitle":"Activities","url":"/en/products/c/100?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hike & Camp","uetTitle":"Hike & Camp","url":"/products/camping-and-hiking/c/1549?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|hike & camp","label":"/products/camping-and-hiking/c/1549?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Snowsports","uetTitle":"Snowsports","url":"/en/products/snow/c/2067?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|snowsports","label":"/en/products/snow/c/2067?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Run & Fitness","uetTitle":"Run & Fitness","url":"/products/run-and-fitness/c/1552?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|run & fitness","label":"/products/run-and-fitness/c/1552?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Packs & Travel","uetTitle":"Packs & Travel","url":"/products/travel-gear/c/1553?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|packs & travel","label":"/products/travel-gear/c/1553?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Bike","uetTitle":"Bike","url":"/products/cycling/c/1551?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|bike","label":"/products/cycling/c/1551?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Climb","uetTitle":"Climb","url":"/products/climbing/c/301?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|climb","label":"/products/climbing/c/301?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Watersports","uetTitle":"Watersports","url":"/products/watersports/c/1550?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-deals","action":"activities|watersports","label":"/products/watersports/c/1550?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"deals","label":"activities"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all deals","uetTitle":"Shop all deals","url":"/en/products/c/100?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"deals","label":""}},{"title":"Women","uetTitle":"Women","url":"#/women","image":"","skipSubNav":false,"features":{"horizontal":["noSubnav"],"vertical":["slide"]},"subnav":[{"title":"Footwear","uetTitle":"Footwear","url":"/gender/women%27s+unisex/products/footwear/c/1184","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hiking shoes","uetTitle":"Hiking shoes","url":"/en/gender/women%27s/products/camping-and-hiking/hiking-footwear/hiking-shoes/c/1492?b=100-1184-1195","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|hiking shoes","label":"/en/gender/women%27s/products/camping-and-hiking/hiking-footwear/hiking-shoes/c/1492?b=100-1184-1195"}},{"title":"Hiking boots","uetTitle":"Hiking boots","url":"/en/gender/women%27s/products/camping-and-hiking/hiking-footwear/hiking-boots/c/1497?b=100-1184-1189","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|hiking boots","label":"/en/gender/women%27s/products/camping-and-hiking/hiking-footwear/hiking-boots/c/1497?b=100-1184-1189"}},{"title":"Trail runners","uetTitle":"Trail runners","url":"/en/gender/women%27s+unisex/products/run-and-fitness/running-and-training-footwear/running-shoes/trail-running-shoes/c/1730?b=100-1184-1195-294","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|trail runners","label":"/en/gender/women%27s+unisex/products/run-and-fitness/running-and-training-footwear/running-shoes/trail-running-shoes/c/1730?b=100-1184-1195-294"}},{"title":"Road runners","uetTitle":"Road runners","url":"/en/gender/women%27s+unisex/products/run-and-fitness/running-and-training-footwear/running-shoes/road-running-shoes/c/1731?b=100-1184-1195-294","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|road runners","label":"/en/gender/women%27s+unisex/products/run-and-fitness/running-and-training-footwear/running-shoes/road-running-shoes/c/1731?b=100-1184-1195-294"}},{"title":"Sandals","uetTitle":"Sandals","url":"/gender/women%27s+unisex/products/footwear/sandals/c/1192","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|sandals","label":"/gender/women%27s+unisex/products/footwear/sandals/c/1192"}},{"title":"Casual shoes","uetTitle":"Casual shoes","url":"/en/gender/women%27s+unisex/products/footwear/shoes/sneakers-and-casual-shoes/c/1491","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|casual shoes","label":"/en/gender/women%27s+unisex/products/footwear/shoes/sneakers-and-casual-shoes/c/1491"}},{"title":"Slippers and booties","uetTitle":"Slippers and booties","url":"/en/gender/unisex+women%27s/products/footwear/slippers-booties-and-fleece-socks/c/1202","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|slippers and booties","label":"/en/gender/unisex+women%27s/products/footwear/slippers-booties-and-fleece-socks/c/1202"}},{"title":"Socks","uetTitle":"Socks","url":"/gender/women%27s+unisex/products/footwear/socks/c/1203","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"footwear|socks","label":"/gender/women%27s+unisex/products/footwear/socks/c/1203"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"footwear"}},{"title":"Jackets","uetTitle":"Jackets","url":"/en/gender/women%27s+unisex/products/clothing/jackets/c/1018","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Rain jackets","uetTitle":"Rain jackets","url":"/en/gender/women%27s+unisex/products/clothing/jackets/rain-jackets/c/1025","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"jackets|rain jackets","label":"/en/gender/women%27s+unisex/products/clothing/jackets/rain-jackets/c/1025"}},{"title":"Down and insulated","uetTitle":"Down and insulated","url":"/en/gender/women%27s+unisex/products/clothing/jackets/insulated-jackets/c/270","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"jackets|down and insulated","label":"/en/gender/women%27s+unisex/products/clothing/jackets/insulated-jackets/c/270"}},{"title":"Fleece and soft shells","uetTitle":"Fleece and soft shells","url":"/en/gender/women%27s+unisex/products/clothing/fleece-hoodies-and-sweaters/fleece-jackets/c/1023?b=100-981-1018","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"jackets|fleece and soft shells","label":"/en/gender/women%27s+unisex/products/clothing/fleece-hoodies-and-sweaters/fleece-jackets/c/1023?b=100-981-1018"}},{"title":"Wind shells","uetTitle":"Wind shells","url":"/en/gender/women%27s+unisex/products/clothing/jackets/wind-jackets/c/1029","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"jackets|wind shells","label":"/en/gender/women%27s+unisex/products/clothing/jackets/wind-jackets/c/1029"}},{"title":"Casual jackets","uetTitle":"Casual jackets","url":"/en/gender/women%27s+unisex/products/clothing/jackets/casual-jackets/c/1019","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"jackets|casual jackets","label":"/en/gender/women%27s+unisex/products/clothing/jackets/casual-jackets/c/1019"}},{"title":"Parkas and winter coats","uetTitle":"Parkas and winter coats","url":"/en/gender/women%27s+unisex/products/clothing/jackets/parkas-and-winter-coats/c/1024","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"jackets|parkas and winter coats","label":"/en/gender/women%27s+unisex/products/clothing/jackets/parkas-and-winter-coats/c/1024"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"jackets"}},{"title":"Tops","uetTitle":"Tops","url":"/en/gender/women%27s+unisex/products/clothing/shirts-and-tops/c/1044","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"T-shirts","uetTitle":"T-shirts","url":"/en/gender/women%27s/products/clothing/shirts-and-tops/short-sleeved-shirts/c/1051?merchbox=womensshortsleeve","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"tops|t-shirts","label":"/en/gender/women%27s/products/clothing/shirts-and-tops/short-sleeved-shirts/c/1051?merchbox=womensshortsleeve"}},{"title":"Tanks and sleeveless shirts","uetTitle":"Tanks and sleeveless shirts","url":"/en/gender/women%27s/products/clothing/shirts-and-tops/tanks-and-sleeveless-shirts/c/1052","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"tops|tanks and sleeveless shirts","label":"/en/gender/women%27s/products/clothing/shirts-and-tops/tanks-and-sleeveless-shirts/c/1052"}},{"title":"Long sleeves","uetTitle":"Long sleeves","url":"/en/gender/women%27s/products/clothing/shirts-and-tops/long-sleeved-shirts/c/1049","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"tops|long sleeves","label":"/en/gender/women%27s/products/clothing/shirts-and-tops/long-sleeved-shirts/c/1049"}},{"title":"Fleece and sweaters","uetTitle":"Fleece and sweaters","url":"/en/gender/women%27s/products/clothing/fleece-hoodies-and-sweaters/c/271","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"tops|fleece and sweaters","label":"/en/gender/women%27s/products/clothing/fleece-hoodies-and-sweaters/c/271"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"tops"}},{"title":"Bottoms","uetTitle":"Bottoms","url":"/en/gender/women%27s/products/clothing/bottoms/c/1002","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Pants","uetTitle":"Pants","url":"/en/gender/women%27s/products/clothing/bottoms/pants/c/1005","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"bottoms|pants","label":"/en/gender/women%27s/products/clothing/bottoms/pants/c/1005"}},{"title":"Shorts","uetTitle":"Shorts","url":"/en/gender/women%27s/products/clothing/bottoms/shorts/c/1014","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"bottoms|shorts","label":"/en/gender/women%27s/products/clothing/bottoms/shorts/c/1014"}},{"title":"Rain pants","uetTitle":"Rain pants","url":"/en/gender/women%27s/products/clothing/bottoms/pants/rain-pants/c/1012","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"bottoms|rain pants","label":"/en/gender/women%27s/products/clothing/bottoms/pants/rain-pants/c/1012"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"bottoms"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/gender/women%27s/products/clothing/swimwear/c/1036","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Swimsuits","uetTitle":"Swimsuits","url":"/en/gender/women%27s/products/clothing/swimwear/swimsuits/c/1038?b=100-1550-369-1036","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"swimwear|swimsuits","label":"/en/gender/women%27s/products/clothing/swimwear/swimsuits/c/1038?b=100-1550-369-1036"}},{"title":"Rashguards","uetTitle":"Rashguards","url":"/en/gender/women%27s/products/clothing/swimwear/rashguards-and-sunguards/c/1041","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"swimwear|rashguards","label":"/en/gender/women%27s/products/clothing/swimwear/rashguards-and-sunguards/c/1041"}},{"title":"Boardshorts","uetTitle":"Boardshorts","url":"/en/gender/women%27s/products/clothing/swimwear/boardshorts/c/1039","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"swimwear|boardshorts","label":"/en/gender/women%27s/products/clothing/swimwear/boardshorts/c/1039"}},{"title":"Wetsuits","uetTitle":"Wetsuits","url":"/en/gender/women%27s/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/wetsuits/c/1043","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"swimwear|wetsuits","label":"/en/gender/women%27s/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/wetsuits/c/1043"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"swimwear"}},{"title":"Skirts and dresses","uetTitle":"Skirts and dresses","url":"/en/products/clothing/skirts-and-dresses/c/1031","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Dresses and jumpsuits","uetTitle":"Dresses and jumpsuits","url":"/en/products/clothing/skirts-and-dresses/dresses-and-jumpsuits/c/1032","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"skirts and dresses|dresses and jumpsuits","label":"/en/products/clothing/skirts-and-dresses/dresses-and-jumpsuits/c/1032"}},{"title":"Skirts","uetTitle":"Skirts","url":"/en/products/clothing/skirts-and-dresses/skirts/c/1033","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"skirts and dresses|skirts","label":"/en/products/clothing/skirts-and-dresses/skirts/c/1033"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"skirts and dresses"}},{"title":"Underwear","uetTitle":"Underwear","url":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/c/1053","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Sport bras","uetTitle":"Sport bras","url":"/en/gender/women%27s/products/run-and-fitness/clothing/sports-bras/c/1057?b=100-981-1053","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"underwear|sport bras","label":"/en/gender/women%27s/products/run-and-fitness/clothing/sports-bras/c/1057?b=100-981-1053"}},{"title":"Briefs","uetTitle":"Briefs","url":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/panties/c/1704","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"underwear|briefs","label":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/panties/c/1704"}},{"title":"Base layer tops","uetTitle":"Base layer tops","url":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-tops/c/1055","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"underwear|base layer tops","label":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-tops/c/1055"}},{"title":"Base layer bottoms","uetTitle":"Base layer bottoms","url":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-bottoms/c/1054","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"underwear|base layer bottoms","label":"/en/gender/women%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-bottoms/c/1054"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"underwear"}},{"title":"Accessories","uetTitle":"Accessories","url":"/en/gender/unisex+women%27s/products/clothing/clothing-accessories/c/982","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hats","uetTitle":"Hats","url":"/en/gender/unisex+women%27s/products/clothing/clothing-accessories/headwear/c/993","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"accessories|hats","label":"/en/gender/unisex+women%27s/products/clothing/clothing-accessories/headwear/c/993"}},{"title":"Sunglasses","uetTitle":"Sunglasses","url":"/en/gender/women%27s+unisex/products/clothing/clothing-accessories/sunglasses/c/1171","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"accessories|sunglasses","label":"/en/gender/women%27s+unisex/products/clothing/clothing-accessories/sunglasses/c/1171"}},{"title":"Watches","uetTitle":"Watches","url":"/en/products/camping-and-hiking/electronics/watches/c/1153","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"accessories|watches","label":"/en/products/camping-and-hiking/electronics/watches/c/1153"}},{"title":"Face masks","uetTitle":"Face masks","url":"/en/products/clothing/clothing-accessories/personal-protective-face-masks/c/8987","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"accessories|face masks","label":"/en/products/clothing/clothing-accessories/personal-protective-face-masks/c/8987"}},{"title":"Neck gaiters and scarves","uetTitle":"Neck gaiters and scarves","url":"/en/gender/unisex+women%27s/products/clothing/clothing-accessories/neck-gaiters-and-scarves/c/1001","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"accessories|neck gaiters and scarves","label":"/en/gender/unisex+women%27s/products/clothing/clothing-accessories/neck-gaiters-and-scarves/c/1001"}},{"title":"Gloves and mitts","uetTitle":"Gloves and mitts","url":"/en/gender/women%27s+unisex/products/clothing/clothing-accessories/gloves-and-mittens/c/987","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"accessories|gloves and mitts","label":"/en/gender/women%27s+unisex/products/clothing/clothing-accessories/gloves-and-mittens/c/987"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"accessories"}},{"title":"By activity","uetTitle":"By activity","url":"/en/gender/women%27s+unisex/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Casual wear","uetTitle":"Casual wear","url":"/en/gender/women%27s+unisex/ideal-for/casual-wear/products/clothing/c/981","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"by activity|casual wear","label":"/en/gender/women%27s+unisex/ideal-for/casual-wear/products/clothing/c/981"}},{"title":"Climbing clothing","uetTitle":"Climbing clothing","url":"/en/gender/women%27s/products/climbing/clothes/c/286","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"by activity|climbing clothing","label":"/en/gender/women%27s/products/climbing/clothes/c/286"}},{"title":"Cycling clothing","uetTitle":"Cycling clothing","url":"/en/gender/women%27s+unisex/products/cycling/cycling-clothing/c/1582","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"by activity|cycling clothing","label":"/en/gender/women%27s+unisex/products/cycling/cycling-clothing/c/1582"}},{"title":"Hiking clothing","uetTitle":"Hiking clothing","url":"/en/gender/women%27s/products/camping-and-hiking/hiking-clothing/c/604","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"by activity|hiking clothing","label":"/en/gender/women%27s/products/camping-and-hiking/hiking-clothing/c/604"}},{"title":"Running clothing","uetTitle":"Running clothing","url":"/en/gender/women%27s+unisex/products/run-and-fitness/clothing/c/1573","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"by activity|running clothing","label":"/en/gender/women%27s+unisex/products/run-and-fitness/clothing/c/1573"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/en/gender/women%27s/products/clothing/swimwear/c/1036","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-women","action":"by activity|swimwear","label":"/en/gender/women%27s/products/clothing/swimwear/c/1036"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"by activity"}},{"title":"Shop all womens","uetTitle":"Shop all womens","url":"/en/gender/women%27s+unisex/products/clothing/c/981","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"women","label":"shop all womens"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"New arrivals","uetTitle":"New arrivals","url":"/en/gender/women%27s+unisex/products/c/100?f=featureCollection%3Anew&sort=newest","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Everyday essentials","uetTitle":"Everyday essentials","url":"/en/products/c/100?f=CFSeasonalCollections%3Aeverydayessentials","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"10% off sock bundle","uetTitle":"10% off sock bundle","url":"/products/footwear/socks/c/1203","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Deals","uetTitle":"Deals","url":"https://www.mec.ca/en/gender/women%27s/products/c/100?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"women","label":""}},{"title":"Men","uetTitle":"Men","url":"#/men","image":"","skipSubNav":false,"features":{"horizontal":["noSubnav"],"vertical":["slide"]},"subnav":[{"title":"Footwear","uetTitle":"Footwear","url":"/gender/unisex+men%27s/products/footwear/c/1184","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hiking shoes","uetTitle":"Hiking shoes","url":"/en/gender/men%27s/products/camping-and-hiking/hiking-footwear/hiking-shoes/c/1492?b=100-1184-1195","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|hiking shoes","label":"/en/gender/men%27s/products/camping-and-hiking/hiking-footwear/hiking-shoes/c/1492?b=100-1184-1195"}},{"title":"Hiking boots","uetTitle":"Hiking boots","url":"/en/gender/men%27s/products/camping-and-hiking/hiking-footwear/hiking-boots/c/1497?b=100-1184-1189","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|hiking boots","label":"/en/gender/men%27s/products/camping-and-hiking/hiking-footwear/hiking-boots/c/1497?b=100-1184-1189"}},{"title":"Trail runners","uetTitle":"Trail runners","url":"/en/gender/men%27s+unisex/products/run-and-fitness/running-and-training-footwear/running-shoes/trail-running-shoes/c/1730?b=100-1184-1195-294","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|trail runners","label":"/en/gender/men%27s+unisex/products/run-and-fitness/running-and-training-footwear/running-shoes/trail-running-shoes/c/1730?b=100-1184-1195-294"}},{"title":"Road runners","uetTitle":"Road runners","url":"/en/gender/men%27s/products/run-and-fitness/running-and-training-footwear/running-shoes/road-running-shoes/c/1731?b=100-1184-1195-294","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|road runners","label":"/en/gender/men%27s/products/run-and-fitness/running-and-training-footwear/running-shoes/road-running-shoes/c/1731?b=100-1184-1195-294"}},{"title":"Sandals","uetTitle":"Sandals","url":"/gender/unisex+men%27s/products/footwear/sandals/c/1192","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|sandals","label":"/gender/unisex+men%27s/products/footwear/sandals/c/1192"}},{"title":"Casual shoes","uetTitle":"Casual shoes","url":"/en/gender/men%27s+unisex/products/footwear/shoes/sneakers-and-casual-shoes/c/1491","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|casual shoes","label":"/en/gender/men%27s+unisex/products/footwear/shoes/sneakers-and-casual-shoes/c/1491"}},{"title":"Slippers and booties","uetTitle":"Slippers and booties","url":"/en/gender/unisex+men%27s/products/footwear/slippers-booties-and-fleece-socks/c/1202","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|slippers and booties","label":"/en/gender/unisex+men%27s/products/footwear/slippers-booties-and-fleece-socks/c/1202"}},{"title":"Socks","uetTitle":"Socks","url":"/gender/unisex+men%27s/products/footwear/socks/c/1203","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"footwear|socks","label":"/gender/unisex+men%27s/products/footwear/socks/c/1203"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"footwear"}},{"title":"Jackets","uetTitle":"Jackets","url":"/en/gender/men%27s+unisex/products/clothing/jackets/c/1018","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Rain jackets","uetTitle":"Rain jackets","url":"/en/gender/men%27s+unisex/products/clothing/jackets/rain-jackets/c/1025","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"jackets|rain jackets","label":"/en/gender/men%27s+unisex/products/clothing/jackets/rain-jackets/c/1025"}},{"title":"Down and insulated","uetTitle":"Down and insulated","url":"/en/gender/men%27s+unisex/products/clothing/jackets/insulated-jackets/c/270","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"jackets|down and insulated","label":"/en/gender/men%27s+unisex/products/clothing/jackets/insulated-jackets/c/270"}},{"title":"Fleece and soft shells","uetTitle":"Fleece and soft shells","url":"/en/gender/men%27s+unisex/products/clothing/fleece-hoodies-and-sweaters/fleece-jackets/c/1023?b=100-981-1018","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"jackets|fleece and soft shells","label":"/en/gender/men%27s+unisex/products/clothing/fleece-hoodies-and-sweaters/fleece-jackets/c/1023?b=100-981-1018"}},{"title":"Wind shells","uetTitle":"Wind shells","url":"/en/gender/men%27s+unisex/products/clothing/jackets/wind-jackets/c/1029","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"jackets|wind shells","label":"/en/gender/men%27s+unisex/products/clothing/jackets/wind-jackets/c/1029"}},{"title":"Casual jackets","uetTitle":"Casual jackets","url":"/en/gender/men%27s+unisex/products/clothing/jackets/casual-jackets/c/1019","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"jackets|casual jackets","label":"/en/gender/men%27s+unisex/products/clothing/jackets/casual-jackets/c/1019"}},{"title":"Parkas and winter coats","uetTitle":"Parkas and winter coats","url":"/en/gender/men%27s+unisex/products/clothing/jackets/parkas-and-winter-coats/c/1024","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"jackets|parkas and winter coats","label":"/en/gender/men%27s+unisex/products/clothing/jackets/parkas-and-winter-coats/c/1024"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"jackets"}},{"title":"Tops","uetTitle":"Tops","url":"/en/gender/men%27s+unisex/products/clothing/shirts-and-tops/c/1044","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"T-shirts","uetTitle":"T-shirts","url":"/en/gender/men%27s+unisex/products/clothing/shirts-and-tops/short-sleeved-shirts/c/1051","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"tops|t-shirts","label":"/en/gender/men%27s+unisex/products/clothing/shirts-and-tops/short-sleeved-shirts/c/1051"}},{"title":"Long sleeves","uetTitle":"Long sleeves","url":"/en/gender/men%27s/products/clothing/shirts-and-tops/long-sleeved-shirts/c/1049","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"tops|long sleeves","label":"/en/gender/men%27s/products/clothing/shirts-and-tops/long-sleeved-shirts/c/1049"}},{"title":"Fleece and sweaters","uetTitle":"Fleece and sweaters","url":"/en/gender/men%27s/products/clothing/fleece-hoodies-and-sweaters/c/271","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"tops|fleece and sweaters","label":"/en/gender/men%27s/products/clothing/fleece-hoodies-and-sweaters/c/271"}},{"title":"Vests","uetTitle":"Vests","url":"/en/gender/men%27s+unisex/products/clothing/jackets/vests/c/1028","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"tops|vests","label":"/en/gender/men%27s+unisex/products/clothing/jackets/vests/c/1028"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"tops"}},{"title":"Bottoms","uetTitle":"Bottoms","url":"/en/gender/men%27s+unisex/products/clothing/bottoms/c/1002","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Pants","uetTitle":"Pants","url":"/en/gender/men%27s/products/clothing/bottoms/pants/c/1005","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"bottoms|pants","label":"/en/gender/men%27s/products/clothing/bottoms/pants/c/1005"}},{"title":"Shorts","uetTitle":"Shorts","url":"/en/gender/men%27s/products/clothing/bottoms/shorts/c/1014","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"bottoms|shorts","label":"/en/gender/men%27s/products/clothing/bottoms/shorts/c/1014"}},{"title":"Rain pants","uetTitle":"Rain pants","url":"/en/gender/men%27s/products/clothing/bottoms/pants/rain-pants/c/1012","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"bottoms|rain pants","label":"/en/gender/men%27s/products/clothing/bottoms/pants/rain-pants/c/1012"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"bottoms"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/gender/men%27s/products/clothing/swimwear/c/1036","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Boardshorts","uetTitle":"Boardshorts","url":"/gender/men%27s/products/clothing/swimwear/boardshorts/c/1039","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"swimwear|boardshorts","label":"/gender/men%27s/products/clothing/swimwear/boardshorts/c/1039"}},{"title":"Pool and lapsuits","uetTitle":"Pool and lapsuits","url":"/gender/men%27s/products/clothing/swimwear/performance-swim-and-lap-suits/c/1040","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"swimwear|pool and lapsuits","label":"/gender/men%27s/products/clothing/swimwear/performance-swim-and-lap-suits/c/1040"}},{"title":"Rashguards","uetTitle":"Rashguards","url":"/gender/men%27s/products/clothing/swimwear/rashguards-and-sunguards/c/1041","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"swimwear|rashguards","label":"/gender/men%27s/products/clothing/swimwear/rashguards-and-sunguards/c/1041"}},{"title":"Wetsuits","uetTitle":"Wetsuits","url":"/gender/men%27s/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/wetsuits/c/1043","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"swimwear|wetsuits","label":"/gender/men%27s/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/wetsuits/c/1043"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"swimwear"}},{"title":"Underwear","uetTitle":"Underwear","url":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/c/1053","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Briefs and boxers","uetTitle":"Briefs and boxers","url":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/briefs-and-boxers/c/1056","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"underwear|briefs and boxers","label":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/briefs-and-boxers/c/1056"}},{"title":"Base layer tops","uetTitle":"Base layer tops","url":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-tops/c/1055","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"underwear|base layer tops","label":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-tops/c/1055"}},{"title":"Base layer bottoms","uetTitle":"Base layer bottoms","url":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-bottoms/c/1054","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"underwear|base layer bottoms","label":"/en/gender/men%27s/products/clothing/base-layers-and-underwear/base-layers-and-underwear/base-layer-bottoms/c/1054"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"underwear"}},{"title":"Accessories","uetTitle":"Accessories","url":"/en/gender/men%27s+unisex/products/clothing/clothing-accessories/c/982","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hats","uetTitle":"Hats","url":"/en/gender/men%27s+unisex/products/clothing/clothing-accessories/headwear/c/993","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"accessories|hats","label":"/en/gender/men%27s+unisex/products/clothing/clothing-accessories/headwear/c/993"}},{"title":"Sunglasses","uetTitle":"Sunglasses","url":"/gender/men%27s+unisex/products/travel-gear/sunglasses/c/1171","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"accessories|sunglasses","label":"/gender/men%27s+unisex/products/travel-gear/sunglasses/c/1171"}},{"title":"Watches","uetTitle":"Watches","url":"/en/products/camping-and-hiking/electronics/watches/c/1153","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"accessories|watches","label":"/en/products/camping-and-hiking/electronics/watches/c/1153"}},{"title":"Face masks","uetTitle":"Face masks","url":"/en/products/clothing/clothing-accessories/personal-protective-face-masks/c/8987","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"accessories|face masks","label":"/en/products/clothing/clothing-accessories/personal-protective-face-masks/c/8987"}},{"title":"Neck gaiters and scarves","uetTitle":"Neck gaiters and scarves","url":"/en/gender/unisex+men%27s/products/clothing/clothing-accessories/neck-gaiters-and-scarves/c/1001","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"accessories|neck gaiters and scarves","label":"/en/gender/unisex+men%27s/products/clothing/clothing-accessories/neck-gaiters-and-scarves/c/1001"}},{"title":"Gloves and mitts","uetTitle":"Gloves and mitts","url":"/en/gender/men%27s+unisex/products/clothing/clothing-accessories/gloves-and-mittens/c/987","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"accessories|gloves and mitts","label":"/en/gender/men%27s+unisex/products/clothing/clothing-accessories/gloves-and-mittens/c/987"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"accessories"}},{"title":"By activity","uetTitle":"By activity","url":"/en/gender/unisex+men%27s/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Casual wear","uetTitle":"Casual wear","url":"/en/gender/unisex+men%27s/ideal-for/casual-wear/products/clothing/c/981","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"by activity|casual wear","label":"/en/gender/unisex+men%27s/ideal-for/casual-wear/products/clothing/c/981"}},{"title":"Climbing clothing","uetTitle":"Climbing clothing","url":"/en/gender/men%27s/products/climbing/clothes/c/286","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"by activity|climbing clothing","label":"/en/gender/men%27s/products/climbing/clothes/c/286"}},{"title":"Cycling clothing","uetTitle":"Cycling clothing","url":"/en/gender/men%27s+unisex/products/cycling/cycling-clothing/c/1582","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"by activity|cycling clothing","label":"/en/gender/men%27s+unisex/products/cycling/cycling-clothing/c/1582"}},{"title":"Hiking clothing","uetTitle":"Hiking clothing","url":"/en/gender/men%27s+unisex/products/camping-and-hiking/hiking-clothing/c/604","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"by activity|hiking clothing","label":"/en/gender/men%27s+unisex/products/camping-and-hiking/hiking-clothing/c/604"}},{"title":"Running clothing","uetTitle":"Running clothing","url":"/en/gender/unisex+men%27s/products/run-and-fitness/clothing/c/1573","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"by activity|running clothing","label":"/en/gender/unisex+men%27s/products/run-and-fitness/clothing/c/1573"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/en/gender/men%27s/products/clothing/swimwear/c/1036?b=100-1550-369","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-men","action":"by activity|swimwear","label":"/en/gender/men%27s/products/clothing/swimwear/c/1036?b=100-1550-369"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"by activity"}},{"title":"Shop all mens","uetTitle":"Shop all mens","url":"/en/gender/unisex+men%27s/products/clothing/c/981","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"men","label":"shop all mens"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"New arrivals","uetTitle":"New arrivals","url":"/en/gender/men%27s+unisex/products/c/100?sort=newest&f=featureCollection%3Anew","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Everyday essentials","uetTitle":"Everyday essentials","url":"/en/products/c/100?f=CFSeasonalCollections%3Aeverydayessentials","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"10% off sock bundle","uetTitle":"10% off sock bundle","url":"/products/footwear/socks/c/1203","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Deals","uetTitle":"Deals","url":"https://www.mec.ca/en/gender/men%27s/products/c/100?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"men","label":""}},{"title":"Kids","uetTitle":"Kids","url":"#/kids","image":"","skipSubNav":false,"features":{"horizontal":["noSubnav"],"vertical":["slide"]},"subnav":[{"title":"Baby (0-2 yrs)","uetTitle":"Baby (0-2 yrs)","url":"/products/kids/baby/c/1901","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"One piece suits","uetTitle":"One piece suits","url":"/products/kids/baby/clothing/outerwear/one-piece-suits/c/1919","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"baby (0-2 yrs)|one piece suits","label":"/products/kids/baby/clothing/outerwear/one-piece-suits/c/1919"}},{"title":"Outerwear","uetTitle":"Outerwear","url":"/products/kids/baby/clothing/outerwear/c/1914","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"baby (0-2 yrs)|outerwear","label":"/products/kids/baby/clothing/outerwear/c/1914"}},{"title":"Clothing","uetTitle":"Clothing","url":"/products/kids/baby/clothing/c/1902","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"baby (0-2 yrs)|clothing","label":"/products/kids/baby/clothing/c/1902"}},{"title":"Footwear","uetTitle":"Footwear","url":"/en/products/kids/baby/footwear/c/1936","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"baby (0-2 yrs)|footwear","label":"/en/products/kids/baby/footwear/c/1936"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/products/kids/baby/clothing/swimwear/c/1922","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"baby (0-2 yrs)|swimwear","label":"/products/kids/baby/clothing/swimwear/c/1922"}},{"title":"Accessories","uetTitle":"Accessories","url":"/products/kids/baby/clothing/accessories/c/1926","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"baby (0-2 yrs)|accessories","label":"/products/kids/baby/clothing/accessories/c/1926"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"baby (0-2 yrs)"}},{"title":"Toddler and child (2-7 yrs)","uetTitle":"Toddler and child (2-7 yrs)","url":"/products/kids/toddler-and-child/c/1942","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"One piece suits","uetTitle":"One piece suits","url":"/products/kids/toddler-and-child/clothing/outerwear/one-piece-suits/c/1964","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"toddler and child (2-7 yrs)|one piece suits","label":"/products/kids/toddler-and-child/clothing/outerwear/one-piece-suits/c/1964"}},{"title":"Outerwear","uetTitle":"Outerwear","url":"/products/kids/toddler-and-child/clothing/outerwear/c/1960","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"toddler and child (2-7 yrs)|outerwear","label":"/products/kids/toddler-and-child/clothing/outerwear/c/1960"}},{"title":"Clothing","uetTitle":"Clothing","url":"/products/kids/toddler-and-child/clothing/c/1943","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"toddler and child (2-7 yrs)|clothing","label":"/products/kids/toddler-and-child/clothing/c/1943"}},{"title":"Footwear","uetTitle":"Footwear","url":"/products/kids/toddler-and-child/footwear/c/1983","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"toddler and child (2-7 yrs)|footwear","label":"/products/kids/toddler-and-child/footwear/c/1983"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/products/kids/toddler-and-child/clothing/swimwear/c/1967","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"toddler and child (2-7 yrs)|swimwear","label":"/products/kids/toddler-and-child/clothing/swimwear/c/1967"}},{"title":"Accessories","uetTitle":"Accessories","url":"/products/kids/toddler-and-child/clothing/accessories/c/1971","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"toddler and child (2-7 yrs)|accessories","label":"/products/kids/toddler-and-child/clothing/accessories/c/1971"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"toddler and child (2-7 yrs)"}},{"title":"Youth (8-16 yrs)","uetTitle":"Youth (8-16 yrs)","url":"/en/products/kids/youth/c/2001?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Jackets ","uetTitle":"Jackets ","url":"/products/kids/youth/clothing/jackets/c/2021","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|jackets ","label":"/products/kids/youth/clothing/jackets/c/2021"}},{"title":"Fleece, hoodies, sweaters ","uetTitle":"Fleece, hoodies, sweaters ","url":"/products/kids/youth/clothing/fleece-hoodies-and-sweaters/c/2007","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|fleece, hoodies, sweaters ","label":"/products/kids/youth/clothing/fleece-hoodies-and-sweaters/c/2007"}},{"title":"Shirts and tops","uetTitle":"Shirts and tops","url":"/products/kids/youth/clothing/shirts/c/2003","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|shirts and tops","label":"/products/kids/youth/clothing/shirts/c/2003"}},{"title":"Pants, shorts and tights","uetTitle":"Pants, shorts and tights","url":"/products/kids/youth/clothing/bottoms/c/2011","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|pants, shorts and tights","label":"/products/kids/youth/clothing/bottoms/c/2011"}},{"title":"Base layers","uetTitle":"Base layers","url":"/products/kids/youth/clothing/base-layers/c/2020","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|base layers","label":"/products/kids/youth/clothing/base-layers/c/2020"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/products/kids/youth/clothing/swimwear/c/2029","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|swimwear","label":"/products/kids/youth/clothing/swimwear/c/2029"}},{"title":"Footwear","uetTitle":"Footwear","url":"/products/kids/youth/footwear/c/2049","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|footwear","label":"/products/kids/youth/footwear/c/2049"}},{"title":"Accessories","uetTitle":"Accessories","url":"/products/kids/youth/clothing/accessories/c/2034","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"youth (8-16 yrs)|accessories","label":"/products/kids/youth/clothing/accessories/c/2034"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"youth (8-16 yrs)"}},{"title":"Child transport","uetTitle":"Child transport","url":"/products/travel-gear/kid-transport/c/1257","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Carriers","uetTitle":"Carriers","url":"/products/travel-gear/kid-transport/child-carrier-backpacks/c/1258","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"child transport|carriers","label":"/products/travel-gear/kid-transport/child-carrier-backpacks/c/1258"}},{"title":"Trailers","uetTitle":"Trailers","url":"/products/travel-gear/kid-transport/child-trailers-and-accessories/c/1264","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"child transport|trailers","label":"/products/travel-gear/kid-transport/child-trailers-and-accessories/c/1264"}},{"title":"Strollers","uetTitle":"Strollers","url":"/products/travel-gear/child-transport/strollers-and-accessories/c/1261","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"child transport|strollers","label":"/products/travel-gear/child-transport/strollers-and-accessories/c/1261"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"child transport"}},{"title":"Kids lunch gear","uetTitle":"Kids lunch gear","url":"/en/products/kids/kids-lunch-gear/c/2162","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Water bottles","uetTitle":"Water bottles","url":"/en/products/kids/kids-lunch-gear/kids-water-bottles/c/2163","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"kids lunch gear|water bottles","label":"/en/products/kids/kids-lunch-gear/kids-water-bottles/c/2163"}},{"title":"Lunch bags","uetTitle":"Lunch bags","url":"/en/products/kids/kids-lunch-gear/kids-lunch-bags/c/2165","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"kids lunch gear|lunch bags","label":"/en/products/kids/kids-lunch-gear/kids-lunch-bags/c/2165"}},{"title":"Food containers","uetTitle":"Food containers","url":"/en/products/kids/kids-lunch-gear/kids-food-containers/c/2164","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-kids","action":"kids lunch gear|food containers","label":"/en/products/kids/kids-lunch-gear/kids-food-containers/c/2164"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"kids lunch gear"}},{"title":"Kids' backpacks","uetTitle":"Kids' backpacks","url":"/en/products/packs-and-bags/kids-backpacks/c/2144?b=100-1900","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"kids' backpacks"}},{"title":"Kids' cycling","uetTitle":"Kids' cycling","url":"/en/gender/kids%27/products/cycling/c/1551","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"kids' cycling"}},{"title":"Kids' activities","uetTitle":"Kids' activities","url":"/en/products/kids/kids-activities/c/2161","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"kids","label":"kids' activities"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all kids","uetTitle":"Shop all kids","url":"/en/products/kids/c/1900","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Back to school collection","uetTitle":"Back to school collection","url":"/en/products/kids/c/1900?f=CFSeasonalCollections%3ABack+to+school+collection","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]},{"title":"Deals","uetTitle":"Deals","url":"/en/products/kids/c/1900?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"kids","label":""}},{"title":"Activities","uetTitle":"Activities","url":"#/shop","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Hike & Camp","uetTitle":"Hike & Camp","url":"#/hikeandcamp","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Tents and shelters","uetTitle":"Tents and shelters","url":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/c/1436","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Backpacking tents","uetTitle":"Backpacking tents","url":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/tents/backpacking-tents/c/1952","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|backpacking tents","label":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/tents/backpacking-tents/c/1952"}},{"title":"Car camping tents","uetTitle":"Car camping tents","url":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/tents/car-camping-tents/c/1445","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|car camping tents","label":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/tents/car-camping-tents/c/1445"}},{"title":"Tarps and light shelters","uetTitle":"Tarps and light shelters","url":"/products/camping-and-hiking/tents-and-furniture/tarps-and-light-shelters/c/1441","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|tarps and light shelters","label":"/products/camping-and-hiking/tents-and-furniture/tarps-and-light-shelters/c/1441"}},{"title":"Footprints","uetTitle":"Footprints","url":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/tent-parts-add-ons-and-repair/footprints/c/1448","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|footprints","label":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/tent-parts-add-ons-and-repair/footprints/c/1448"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|tents and shelters","label":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/c/1436"}},{"title":"Sleeping bags and pads","uetTitle":"Sleeping bags and pads","url":"/products/camping-and-hiking/sleeping-bags-and-pads/c/1405","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Sleeping bags","uetTitle":"Sleeping bags","url":"/products/camping-and-hiking/sleeping-bags-and-pads/sleeping-bags/c/1410","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|sleeping bags","label":"/products/camping-and-hiking/sleeping-bags-and-pads/sleeping-bags/c/1410"}},{"title":"Sleeping pads","uetTitle":"Sleeping pads","url":"/products/camping-and-hiking/sleeping-bags-and-pads/sleeping-pads/c/1416","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|sleeping pads","label":"/products/camping-and-hiking/sleeping-bags-and-pads/sleeping-pads/c/1416"}},{"title":"Pillows","uetTitle":"Pillows","url":"/products/camping-and-hiking/sleeping-bags-and-pads/pillows-and-pillowcases/c/1408","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|pillows","label":"/products/camping-and-hiking/sleeping-bags-and-pads/pillows-and-pillowcases/c/1408"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|sleeping bags and pads","label":"/products/camping-and-hiking/sleeping-bags-and-pads/c/1405"}},{"title":"Camp furniture","uetTitle":"Camp furniture","url":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/camp-and-beach-furniture/c/1432","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Chairs","uetTitle":"Chairs","url":"/products/camping-and-hiking/tents-and-furniture/camp-and-beach-furniture/chairs/c/1434","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|chairs","label":"/products/camping-and-hiking/tents-and-furniture/camp-and-beach-furniture/chairs/c/1434"}},{"title":"Tables","uetTitle":"Tables","url":"/products/camping-and-hiking/tents-and-furniture/camp-and-beach-furniture/tables/c/1435","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|tables","label":"/products/camping-and-hiking/tents-and-furniture/camp-and-beach-furniture/tables/c/1435"}},{"title":"Hammocks","uetTitle":"Hammocks","url":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/hammocks/lounge-hammocks/c/1484?b=100-1549-1432","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|hammocks","label":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/hammocks/lounge-hammocks/c/1484?b=100-1549-1432"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|camp furniture","label":"/en/products/camping-and-hiking/camping-tents-tarps-and-bivies/camp-and-beach-furniture/c/1432"}},{"title":"Kitchen and hydration","uetTitle":"Kitchen and hydration","url":"/products/camping-and-hiking/kitchen-and-hydration/c/1267","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Stoves, fuel and fire","uetTitle":"Stoves, fuel and fire","url":"/products/camping-and-hiking/kitchen-and-hydration/stoves-fuel-and-fire/c/1279","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|stoves, fuel and fire","label":"/products/camping-and-hiking/kitchen-and-hydration/stoves-fuel-and-fire/c/1279"}},{"title":"Camp dinnerware","uetTitle":"Camp dinnerware","url":"/en/products/camping-and-hiking/kitchen-and-hydration/camp-dinnerware/c/1271","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|camp dinnerware","label":"/en/products/camping-and-hiking/kitchen-and-hydration/camp-dinnerware/c/1271"}},{"title":"Outdoor cookware","uetTitle":"Outdoor cookware","url":"/en/products/camping-and-hiking/kitchen-and-hydration/outdoor-cookware/c/1274","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|outdoor cookware","label":"/en/products/camping-and-hiking/kitchen-and-hydration/outdoor-cookware/c/1274"}},{"title":"Coolers and food storage","uetTitle":"Coolers and food storage","url":"/products/camping-and-hiking/kitchen-and-hydration/coolers-and-food-storage/c/1268","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|coolers and food storage","label":"/products/camping-and-hiking/kitchen-and-hydration/coolers-and-food-storage/c/1268"}},{"title":"Water bottles and treatment","uetTitle":"Water bottles and treatment","url":"/en/products/camping-and-hiking/kitchen-and-hydration/water-bottles-and-water-treatment/c/1563","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|water bottles and treatment","label":"/en/products/camping-and-hiking/kitchen-and-hydration/water-bottles-and-water-treatment/c/1563"}},{"title":"Food and drinks","uetTitle":"Food and drinks","url":"/products/camping-and-hiking/kitchen-and-hydration/food-and-drink/c/1175","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|food and drinks","label":"/products/camping-and-hiking/kitchen-and-hydration/food-and-drink/c/1175"}},{"title":"Travel mugs","uetTitle":"Travel mugs","url":"/en/products/camping-and-hiking/kitchen-and-hydration/cookware-dishes-and-utensils/mugs-cups-and-dishes/mugs-and-cups/travel-mugs/c/1791","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|travel mugs","label":"/en/products/camping-and-hiking/kitchen-and-hydration/cookware-dishes-and-utensils/mugs-cups-and-dishes/mugs-and-cups/travel-mugs/c/1791"}},{"title":"Coffee makers and kettles","uetTitle":"Coffee makers and kettles","url":"/en/products/camping-and-hiking/kitchen-and-hydration/coffee-makers-and-kettles/c/1272","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|coffee makers and kettles","label":"/en/products/camping-and-hiking/kitchen-and-hydration/coffee-makers-and-kettles/c/1272"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|kitchen and hydration","label":"/products/camping-and-hiking/kitchen-and-hydration/c/1267"}},{"title":"Packs and bags","uetTitle":"Packs and bags","url":"/products/camping-and-hiking/packs-and-bags/c/1564","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Backpacking packs","uetTitle":"Backpacking packs","url":"/products/camping-and-hiking/packs-and-bags/backpacking-packs/c/1338","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|backpacking packs","label":"/products/camping-and-hiking/packs-and-bags/backpacking-packs/c/1338"}},{"title":"Daypacks","uetTitle":"Daypacks","url":"/products/packs-and-bags/daypacks-and-school-bags/daypacks/c/1333?b=100-1549-1564","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|daypacks","label":"/products/packs-and-bags/daypacks-and-school-bags/daypacks/c/1333?b=100-1549-1564"}},{"title":"Waist packs","uetTitle":"Waist packs","url":"/products/packs-and-bags/shoulder-bags-slings-and-waist-packs/waist-packs/c/1356?b=100-1549-1564","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|waist packs","label":"/products/packs-and-bags/shoulder-bags-slings-and-waist-packs/waist-packs/c/1356?b=100-1549-1564"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|packs and bags","label":"/products/camping-and-hiking/packs-and-bags/c/1564"}},{"title":"Lighting","uetTitle":"Lighting","url":"/en/products/camping-and-hiking/headlamps-and-lighting/c/1296","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Headlamps","uetTitle":"Headlamps","url":"/en/products/run-and-fitness/headlamps/c/1306?merchbox=lighting-headlamps","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|headlamps","label":"/en/products/run-and-fitness/headlamps/c/1306?merchbox=lighting-headlamps"}},{"title":"Flashlights","uetTitle":"Flashlights","url":"/en/products/camping-and-hiking/headlamps-and-lighting/flashlights/c/1304","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|flashlights","label":"/en/products/camping-and-hiking/headlamps-and-lighting/flashlights/c/1304"}},{"title":"Lanterns","uetTitle":"Lanterns","url":"/en/products/camping-and-hiking/headlamps-and-lighting/lanterns-and-candles/c/1307","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|lanterns","label":"/en/products/camping-and-hiking/headlamps-and-lighting/lanterns-and-candles/c/1307"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|lighting","label":"/en/products/camping-and-hiking/headlamps-and-lighting/c/1296"}},{"title":"Hiking footwear","uetTitle":"Hiking footwear","url":"/products/camping-and-hiking/hiking-footwear-and-clothing/hiking-footwear/c/605","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Boots","uetTitle":"Boots","url":"/products/camping-and-hiking/hiking-footwear-and-clothing/hiking-footwear/hiking-boots/c/1497","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|boots","label":"/products/camping-and-hiking/hiking-footwear-and-clothing/hiking-footwear/hiking-boots/c/1497"}},{"title":"Shoes ","uetTitle":"Shoes ","url":"/products/footwear/shoes/hiking-shoes/c/1492?b=100-1549-605","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|shoes ","label":"/products/footwear/shoes/hiking-shoes/c/1492?b=100-1549-605"}},{"title":"Hiking socks","uetTitle":"Hiking socks","url":"/products/footwear/socks/hiking-socks/c/1518?b=100-1549-1651-605","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|hiking socks","label":"/products/footwear/socks/hiking-socks/c/1518?b=100-1549-1651-605"}},{"title":"Gaiters","uetTitle":"Gaiters","url":"/products/footwear/accessories/gaiters/c/1191?b=100-1549-1651-605-606","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|gaiters","label":"/products/footwear/accessories/gaiters/c/1191?b=100-1549-1651-605-606"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|hiking footwear","label":"/products/camping-and-hiking/hiking-footwear-and-clothing/hiking-footwear/c/605"}},{"title":"Hiking clothing","uetTitle":"Hiking clothing","url":"/products/camping-and-hiking/hiking-footwear-and-clothing/hiking-clothing/c/604","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Jackets","uetTitle":"Jackets","url":"/products/camping-and-hiking/hiking-clothing/hiking-jackets/c/420","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|jackets","label":"/products/camping-and-hiking/hiking-clothing/hiking-jackets/c/420"}},{"title":"Pants","uetTitle":"Pants","url":"/en/products/camping-and-hiking/hiking-clothing/hiking-pants/c/1008","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|pants","label":"/en/products/camping-and-hiking/hiking-clothing/hiking-pants/c/1008"}},{"title":"Tops","uetTitle":"Tops","url":"/products/camping-and-hiking/hiking-clothing/hiking-and-climbing-shirts/c/1705","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|tops","label":"/products/camping-and-hiking/hiking-clothing/hiking-and-climbing-shirts/c/1705"}},{"title":"Base layers","uetTitle":"Base layers","url":"/products/clothing/base-layers-and-underwear/base-layers-and-underwear/c/273?b=100-1549-604","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|base layers","label":"/products/clothing/base-layers-and-underwear/base-layers-and-underwear/c/273?b=100-1549-604"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|hiking clothing","label":"/products/camping-and-hiking/hiking-footwear-and-clothing/hiking-clothing/c/604"}},{"title":"Tools and accessories","uetTitle":"Tools and accessories","url":"/en/products/camping-and-hiking/tools-and-accessories/c/277","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Trekking poles","uetTitle":"Trekking poles","url":"/products/camping-and-hiking/tools-lighting-and-accessories/trekking-poles-and-accessories/c/1510","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|trekking poles","label":"/products/camping-and-hiking/tools-lighting-and-accessories/trekking-poles-and-accessories/c/1510"}},{"title":"Knives and multi-tools","uetTitle":"Knives and multi-tools","url":"/products/camping-and-hiking/tools-lighting-and-accessories/knives-and-tools/c/1289","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|knives and multi-tools","label":"/products/camping-and-hiking/tools-lighting-and-accessories/knives-and-tools/c/1289"}},{"title":"Binoculars","uetTitle":"Binoculars","url":"/en/products/camping-and-hiking/tools-lighting-and-accessories/binoculars/c/900","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|binoculars","label":"/en/products/camping-and-hiking/tools-lighting-and-accessories/binoculars/c/900"}},{"title":"Repair and maintenance","uetTitle":"Repair and maintenance","url":"/products/camping-and-hiking/tools-lighting-and-accessories/repair-and-maintenance/c/1312","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|repair and maintenance","label":"/products/camping-and-hiking/tools-lighting-and-accessories/repair-and-maintenance/c/1312"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|tools and accessories","label":"/en/products/camping-and-hiking/tools-and-accessories/c/277"}},{"title":"Health and safety ","uetTitle":"Health and safety ","url":"/products/camping-and-hiking/health-and-safety/c/1206","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"First aid kits","uetTitle":"First aid kits","url":"/products/camping-and-hiking/health-and-safety/first-aid-kits-and-supplies/first-aid-kits/c/1210","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|first aid kits","label":"/products/camping-and-hiking/health-and-safety/first-aid-kits-and-supplies/first-aid-kits/c/1210"}},{"title":"Bear safety","uetTitle":"Bear safety","url":"/products/camping-and-hiking/health-and-safety/bear-safety/c/1207","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|bear safety","label":"/products/camping-and-hiking/health-and-safety/bear-safety/c/1207"}},{"title":"Bug spray and bug nets","uetTitle":"Bug spray and bug nets","url":"/products/camping-and-hiking/health-and-safety/bug-spray-and-bug-nets/c/1208","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|bug spray and bug nets","label":"/products/camping-and-hiking/health-and-safety/bug-spray-and-bug-nets/c/1208"}},{"title":"Bath and sanitation products","uetTitle":"Bath and sanitation products","url":"/products/camping-and-hiking/health-and-safety/bath-and-sanitation-products/c/804","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|bath and sanitation products","label":"/products/camping-and-hiking/health-and-safety/bath-and-sanitation-products/c/804"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|health and safety ","label":"/products/camping-and-hiking/health-and-safety/c/1206"}},{"title":"Electronics","uetTitle":"Electronics","url":"/products/camping-and-hiking/electronics/c/1108","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"GPS navigation","uetTitle":"GPS navigation","url":"/products/camping-and-hiking/electronics/gps-navigation/c/1139","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|gps navigation","label":"/products/camping-and-hiking/electronics/gps-navigation/c/1139"}},{"title":"Portable power banks","uetTitle":"Portable power banks","url":"/en/products/camping-and-hiking/electronics/chargers-and-adapters/portable-chargers-and-power-packs/c/1570","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|portable power banks","label":"/en/products/camping-and-hiking/electronics/chargers-and-adapters/portable-chargers-and-power-packs/c/1570"}},{"title":"Solar chargers","uetTitle":"Solar chargers","url":"/en/products/camping-and-hiking/electronics/chargers-and-adapters/solar-chargers/c/1136","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|solar chargers","label":"/en/products/camping-and-hiking/electronics/chargers-and-adapters/solar-chargers/c/1136"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|electronics","label":"/products/camping-and-hiking/electronics/c/1108"}},{"title":"Maps and guidebooks","uetTitle":"Maps and guidebooks","url":"/en/products/camping-and-hiking/tools-and-accessories/maps-and-guidebooks/c/1244","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|maps and guidebooks","label":"/en/products/camping-and-hiking/tools-and-accessories/maps-and-guidebooks/c/1244"}},{"title":"Dog gear","uetTitle":"Dog gear","url":"/products/camping-and-hiking/dog-gear/c/1565","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|dog gear","label":"/products/camping-and-hiking/dog-gear/c/1565"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all hike and camp","uetTitle":"Shop all hike and camp","url":"/en/products/camping-and-hiking/c/1549","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|shop all hike and camp","label":"/en/products/camping-and-hiking/c/1549"}},{"title":"New arrivals","uetTitle":"New arrivals","url":"/en/products/camping-and-hiking/c/1549?f=featureCollection%3Anew","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|new arrivals","label":"/en/products/camping-and-hiking/c/1549?f=featurecollection%3anew"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/camping-and-hiking/c/1549?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|deals","label":"/en/products/camping-and-hiking/c/1549?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Hiking and camping tips","uetTitle":"Hiking and camping tips","url":"/en/explore/hiking-and-camping","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|hiking and camping tips","label":"/en/explore/hiking-and-camping"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"hike & camp|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"hike & camp"}},{"title":"Bike","uetTitle":"Bike","url":"#/bike","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Bikes","uetTitle":"Bikes","url":"/products/cycling/bikes/c/854","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Mountain bikes","uetTitle":"Mountain bikes","url":"/products/cycling/bikes/mountain-bikes/c/1527","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|mountain bikes","label":"/products/cycling/bikes/mountain-bikes/c/1527"}},{"title":"Electric bikes","uetTitle":"Electric bikes","url":"/products/cycling/bikes/pedal-assist-electric-bikes/c/1780","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|electric bikes","label":"/products/cycling/bikes/pedal-assist-electric-bikes/c/1780"}},{"title":"Road bikes","uetTitle":"Road bikes","url":"/products/cycling/bikes/road-bikes/c/1528","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|road bikes","label":"/products/cycling/bikes/road-bikes/c/1528"}},{"title":"Urban and commuter bikes","uetTitle":"Urban and commuter bikes","url":"/products/cycling/bikes/urban-commuter-bikes/c/1529","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|urban and commuter bikes","label":"/products/cycling/bikes/urban-commuter-bikes/c/1529"}},{"title":"Gravel and cyclocross bikes","uetTitle":"Gravel and cyclocross bikes","url":"/products/cycling/bikes/cyclocross-bikes/c/296","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|gravel and cyclocross bikes","label":"/products/cycling/bikes/cyclocross-bikes/c/296"}},{"title":"Kids' bikes","uetTitle":"Kids' bikes","url":"/en/products/kids/kids-bikes/c/1559?b=100-1551-854","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|kids' bikes","label":"/en/products/kids/kids-bikes/c/1559?b=100-1551-854"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bikes","label":"/products/cycling/bikes/c/854"}},{"title":"Training and electronics","uetTitle":"Training and electronics","url":"/products/cycling/training-and-electronics/c/298","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Bike trainers","uetTitle":"Bike trainers","url":"/en/products/cycling/training-and-electronics/bike-trainers-and-accessories/bike-trainers/c/1463","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike trainers","label":"/en/products/cycling/training-and-electronics/bike-trainers-and-accessories/bike-trainers/c/1463"}},{"title":"Bike trainer accessories","uetTitle":"Bike trainer accessories","url":"/products/cycling/training-and-electronics/bike-trainers-and-accessories/bike-trainer-accessories/c/1585","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike trainer accessories","label":"/products/cycling/training-and-electronics/bike-trainers-and-accessories/bike-trainer-accessories/c/1585"}},{"title":"Bike computers","uetTitle":"Bike computers","url":"/products/cycling/bike-accessories-and-add-ons/bike-computers/c/1117","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike computers","label":"/products/cycling/bike-accessories-and-add-ons/bike-computers/c/1117"}},{"title":"Fitness trackers","uetTitle":"Fitness trackers","url":"/en/products/cycling/training-and-electronics/bike-computers/heart-rate-monitors/c/1145","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|fitness trackers","label":"/en/products/cycling/training-and-electronics/bike-computers/heart-rate-monitors/c/1145"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|training and electronics","label":"/products/cycling/training-and-electronics/c/298"}},{"title":"Bike helmets and protection","uetTitle":"Bike helmets and protection","url":"/en/products/cycling/bike-accessories-and-add-ons/bike-helmets-and-body-armour/c/1584","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Helmets","uetTitle":"Helmets","url":"/en/products/cycling/bike-accessories-and-add-ons/bike-helmets-and-body-armour/bike-helmets/c/1509","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|helmets","label":"/en/products/cycling/bike-accessories-and-add-ons/bike-helmets-and-body-armour/bike-helmets/c/1509"}},{"title":"Body armour","uetTitle":"Body armour","url":"/en/products/cycling/bike-accessories-and-add-ons/bike-helmets-and-body-armour/body-armour/c/797","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|body armour","label":"/en/products/cycling/bike-accessories-and-add-ons/bike-helmets-and-body-armour/body-armour/c/797"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike helmets and protection","label":"/en/products/cycling/bike-accessories-and-add-ons/bike-helmets-and-body-armour/c/1584"}},{"title":"Clothing","uetTitle":"Clothing","url":"/products/cycling/cycling-clothing/c/1582","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Tops","uetTitle":"Tops","url":"/en/products/cycling/cycling-clothing/cycling-tops/c/287","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|tops","label":"/en/products/cycling/cycling-clothing/cycling-tops/c/287"}},{"title":"Bottoms","uetTitle":"Bottoms","url":"/en/products/cycling/cycling-clothing/cycling-bottoms/c/260","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bottoms","label":"/en/products/cycling/cycling-clothing/cycling-bottoms/c/260"}},{"title":"Accessories","uetTitle":"Accessories","url":"/en/products/cycling/cycling-clothing/cycling-clothing-accessories/c/261","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|accessories","label":"/en/products/cycling/cycling-clothing/cycling-clothing-accessories/c/261"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|clothing","label":"/products/cycling/cycling-clothing/c/1582"}},{"title":"Footwear","uetTitle":"Footwear","url":"/products/cycling/cycling-footwear/c/262","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Cycling shoes","uetTitle":"Cycling shoes","url":"/products/cycling/cycling-footwear/cycling-shoes/c/1496","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|cycling shoes","label":"/products/cycling/cycling-footwear/cycling-shoes/c/1496"}},{"title":"Cycling socks","uetTitle":"Cycling socks","url":"/products/footwear/socks/bike-socks/c/1519?b=100-1551-262","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|cycling socks","label":"/products/footwear/socks/bike-socks/c/1519?b=100-1551-262"}},{"title":"Shoe covers","uetTitle":"Shoe covers","url":"/products/cycling/cycling-footwear/shoe-covers/c/1194","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|shoe covers","label":"/products/cycling/cycling-footwear/shoe-covers/c/1194"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|footwear","label":"/products/cycling/cycling-footwear/c/262"}},{"title":"Bike components","uetTitle":"Bike components","url":"/products/cycling/bike-components/c/819","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Drivetrain systems","uetTitle":"Drivetrain systems","url":"/products/cycling/bike-components/drive-train/c/825","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|drivetrain systems","label":"/products/cycling/bike-components/drive-train/c/825"}},{"title":"Tires, tubes, wheels and hubs","uetTitle":"Tires, tubes, wheels and hubs","url":"/products/cycling/bike-components/tires252c-tubes252c-wheels-and-hubs/c/847","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|tires, tubes, wheels and hubs","label":"/products/cycling/bike-components/tires252c-tubes252c-wheels-and-hubs/c/847"}},{"title":"Pedals and cleats","uetTitle":"Pedals and cleats","url":"/products/cycling/bike-components/pedals-and-cleats/c/842","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|pedals and cleats","label":"/products/cycling/bike-components/pedals-and-cleats/c/842"}},{"title":"Saddles and seat posts","uetTitle":"Saddles and seat posts","url":"/products/cycling/bike-components/saddles-and-seat-posts/c/1815","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|saddles and seat posts","label":"/products/cycling/bike-components/saddles-and-seat-posts/c/1815"}},{"title":"Handlebars and stems","uetTitle":"Handlebars and stems","url":"/en/products/cycling/bike-components/handlebars-and-stems/c/838?merchbox=819stems","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|handlebars and stems","label":"/en/products/cycling/bike-components/handlebars-and-stems/c/838?merchbox=819stems"}},{"title":"Brakes, pads and rotors","uetTitle":"Brakes, pads and rotors","url":"/products/cycling/bike-components/brakes252c-pads-and-rotors/c/820","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|brakes, pads and rotors","label":"/products/cycling/bike-components/brakes252c-pads-and-rotors/c/820"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike components","label":"/products/cycling/bike-components/c/819"}},{"title":"Bags and trailers","uetTitle":"Bags and trailers","url":"/products/cycling/panniers252c-bags-and-racks/c/1370","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Child trailers","uetTitle":"Child trailers","url":"/products/travel-gear/child-transport/child-trailers-and-accessories/c/1264?b=100-1551-1370-1451","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|child trailers","label":"/products/travel-gear/child-transport/child-trailers-and-accessories/c/1264?b=100-1551-1370-1451"}},{"title":"Panniers","uetTitle":"Panniers","url":"/products/cycling/panniers252c-bags-and-racks/bicycle-panniers/c/1373","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|panniers","label":"/products/cycling/panniers252c-bags-and-racks/bicycle-panniers/c/1373"}},{"title":"Backpacks and messenger bags","uetTitle":"Backpacks and messenger bags","url":"/products/cycling/panniers252c-bags-and-racks/bike-backpacks-and-messenger-bags/c/318","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|backpacks and messenger bags","label":"/products/cycling/panniers252c-bags-and-racks/bike-backpacks-and-messenger-bags/c/318"}},{"title":"Handlebar, frame and seat bags","uetTitle":"Handlebar, frame and seat bags","url":"/products/cycling/panniers252c-bags-and-racks/handlebar-frame-and-seat-bags/c/299","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|handlebar, frame and seat bags","label":"/products/cycling/panniers252c-bags-and-racks/handlebar-frame-and-seat-bags/c/299"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bags and trailers","label":"/products/cycling/panniers252c-bags-and-racks/c/1370"}},{"title":"Bike accessories","uetTitle":"Bike accessories","url":"/products/cycling/bike-accessories-and-add-ons/c/813","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Bike lights","uetTitle":"Bike lights","url":"/products/cycling/bike-accessories-and-add-ons/bike-lights/c/1298","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike lights","label":"/products/cycling/bike-accessories-and-add-ons/bike-lights/c/1298"}},{"title":"Bottle cages and water bottles","uetTitle":"Bottle cages and water bottles","url":"/products/cycling/bike-accessories-and-add-ons/bottle-cages-and-water-bottles/c/1583","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bottle cages and water bottles","label":"/products/cycling/bike-accessories-and-add-ons/bottle-cages-and-water-bottles/c/1583"}},{"title":"Bike locks","uetTitle":"Bike locks","url":"/products/cycling/bike-accessories-and-add-ons/bike-locks/c/1308","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike locks","label":"/products/cycling/bike-accessories-and-add-ons/bike-locks/c/1308"}},{"title":"Bike bells and horns","uetTitle":"Bike bells and horns","url":"/products/cycling/bike-accessories-and-add-ons/bike-safety/bike-bells-and-horns/c/814","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike bells and horns","label":"/products/cycling/bike-accessories-and-add-ons/bike-safety/bike-bells-and-horns/c/814"}},{"title":"Fenders","uetTitle":"Fenders","url":"/products/cycling/bike-accessories-and-add-ons/fenders/c/815","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|fenders","label":"/products/cycling/bike-accessories-and-add-ons/fenders/c/815"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike accessories","label":"/products/cycling/bike-accessories-and-add-ons/c/813"}},{"title":"Maintenance and storage","uetTitle":"Maintenance and storage","url":"/products/cycling/bike-tools-and-maintenance/c/855","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Bike tools","uetTitle":"Bike tools","url":"/products/cycling/bike-tools-and-maintenance/bike-tools/c/856","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike tools","label":"/products/cycling/bike-tools-and-maintenance/bike-tools/c/856"}},{"title":"Lubricants and cleaners","uetTitle":"Lubricants and cleaners","url":"/en/products/cycling/bike-tools-and-maintenance/lubrication-cleaning-and-degreasers/c/876","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|lubricants and cleaners","label":"/en/products/cycling/bike-tools-and-maintenance/lubrication-cleaning-and-degreasers/c/876"}},{"title":"Bike pumps","uetTitle":"Bike pumps","url":"/products/cycling/bike-accessories-and-add-ons/bicycle-pumps/c/1384","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike pumps","label":"/products/cycling/bike-accessories-and-add-ons/bicycle-pumps/c/1384"}},{"title":"Bike racks and storage","uetTitle":"Bike racks and storage","url":"/en/products/cycling/bike-tools-and-maintenance/bike-racks-carriers-and-storage/c/258","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|bike racks and storage","label":"/en/products/cycling/bike-tools-and-maintenance/bike-racks-carriers-and-storage/c/258"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|maintenance and storage","label":"/products/cycling/bike-tools-and-maintenance/c/855"}},{"title":"Training food and drinks","uetTitle":"Training food and drinks","url":"/products/run-and-fitness/training-food-and-drinks/c/1580?b=100-1551","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|training food and drinks","label":"/products/run-and-fitness/training-food-and-drinks/c/1580?b=100-1551"}},{"title":"Anti-chafing gels and lotions","uetTitle":"Anti-chafing gels and lotions","url":"/en/products/camping-and-hiking/health-and-safety/bath-and-sanitation-products/anti-chafing-gels-and-lotions/c/805?b=100-1551-298","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|anti-chafing gels and lotions","label":"/en/products/camping-and-hiking/health-and-safety/bath-and-sanitation-products/anti-chafing-gels-and-lotions/c/805?b=100-1551-298"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all cycling","uetTitle":"Shop all cycling","url":"/en/products/cycling/c/1551","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|shop all cycling","label":"/en/products/cycling/c/1551"}},{"title":"New arrivals","uetTitle":"New arrivals","url":"/products/cycling/c/1551?f=featureCollection%3Anew","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|new arrivals","label":"/products/cycling/c/1551?f=featurecollection%3anew"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/cycling/c/1551?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|deals","label":"/en/products/cycling/c/1551?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Cycling tips","uetTitle":"Cycling tips","url":"/en/explore/cycling","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|cycling tips","label":"/en/explore/cycling"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"bike|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"bike"}},{"title":"Climb","uetTitle":"Climb","url":"#/climb","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Climbing gear","uetTitle":"Climbing gear","url":"/products/climbing/c/301","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Harnesses","uetTitle":"Harnesses","url":"/products/climbing/gym-climbing-and-indoor-training/climbing-harnesses/c/957","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|harnesses","label":"/products/climbing/gym-climbing-and-indoor-training/climbing-harnesses/c/957"}},{"title":"Helmets","uetTitle":"Helmets","url":"/products/climbing/rock-climbing/climbing-helmets/c/1508","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|helmets","label":"/products/climbing/rock-climbing/climbing-helmets/c/1508"}},{"title":"Carabiners and draws","uetTitle":"Carabiners and draws","url":"/en/products/climbing/rock-climbing/carabiners-and-draws/c/949","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|carabiners and draws","label":"/en/products/climbing/rock-climbing/carabiners-and-draws/c/949"}},{"title":"Chalk and chalk bags","uetTitle":"Chalk and chalk bags","url":"/products/climbing/bouldering/chalk-and-chalk-bags/c/954","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|chalk and chalk bags","label":"/products/climbing/bouldering/chalk-and-chalk-bags/c/954"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|climbing gear","label":"/products/climbing/c/301"}},{"title":"Trad climbing","uetTitle":"Trad climbing","url":"/products/climbing/rock-climbing/rock-hardware/c/960","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Camming devices","uetTitle":"Camming devices","url":"/products/climbing/rock-climbing/rock-hardware/cams-nuts-and-hexes/camming-devices/c/962","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|camming devices","label":"/products/climbing/rock-climbing/rock-hardware/cams-nuts-and-hexes/camming-devices/c/962"}},{"title":"Nuts, hexes and nut tools","uetTitle":"Nuts, hexes and nut tools","url":"/products/climbing/rock-climbing/rock-hardware/cams-nuts-and-hexes/nuts-hexes-and-nut-tools/c/966","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|nuts, hexes and nut tools","label":"/products/climbing/rock-climbing/rock-hardware/cams-nuts-and-hexes/nuts-hexes-and-nut-tools/c/966"}},{"title":"Aid climbing gear","uetTitle":"Aid climbing gear","url":"/products/climbing/gear/rock-climbing/rock-hardware/aid-climbing-gear/c/961","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|aid climbing gear","label":"/products/climbing/gear/rock-climbing/rock-hardware/aid-climbing-gear/c/961"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|trad climbing","label":"/products/climbing/rock-climbing/rock-hardware/c/960"}},{"title":"Footwear","uetTitle":"Footwear","url":"/products/climbing/climbing-footwear/c/314","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Climbing shoes ","uetTitle":"Climbing shoes ","url":"/products/climbing/climbing-footwear/rock-climbing-shoes/c/1190","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|climbing shoes ","label":"/products/climbing/climbing-footwear/rock-climbing-shoes/c/1190"}},{"title":"Approach shoes","uetTitle":"Approach shoes","url":"/products/footwear/shoes/approach-shoes/c/1493?b=100-301-314","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|approach shoes","label":"/products/footwear/shoes/approach-shoes/c/1493?b=100-301-314"}},{"title":"Mountaineering boots","uetTitle":"Mountaineering boots","url":"/products/climbing/mountaineering-and-ice-climbing/mountaineering-boots/c/1501","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|mountaineering boots","label":"/products/climbing/mountaineering-and-ice-climbing/mountaineering-boots/c/1501"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|footwear","label":"/products/climbing/climbing-footwear/c/314"}},{"title":"Ropes and belay devices","uetTitle":"Ropes and belay devices","url":"/products/climbing/rock-climbing/ropes-cords-and-slings/c/1390","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Dynamic climbing ropes","uetTitle":"Dynamic climbing ropes","url":"/products/climbing/rock-climbing/ropes-cords-and-slings/dynamic-climbing-ropes/c/1392","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|dynamic climbing ropes","label":"/products/climbing/rock-climbing/ropes-cords-and-slings/dynamic-climbing-ropes/c/1392"}},{"title":"Static ropes and cordage","uetTitle":"Static ropes and cordage","url":"/products/climbing/rock-climbing/ropes-cords-and-slings/static-ropes-and-cord/c/1394","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|static ropes and cordage","label":"/products/climbing/rock-climbing/ropes-cords-and-slings/static-ropes-and-cord/c/1394"}},{"title":"Slings and webbing","uetTitle":"Slings and webbing","url":"/products/climbing/rock-climbing/ropes-cords-and-slings/slings-and-webbing/c/967","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|slings and webbing","label":"/products/climbing/rock-climbing/ropes-cords-and-slings/slings-and-webbing/c/967"}},{"title":"Belay devices","uetTitle":"Belay devices","url":"/products/climbing/rock-climbing/uppers-and-downers/belay-devices/c/978","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|belay devices","label":"/products/climbing/rock-climbing/uppers-and-downers/belay-devices/c/978"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|ropes and belay devices","label":"/products/climbing/rock-climbing/ropes-cords-and-slings/c/1390"}},{"title":"Mountaineering and ice climbing","uetTitle":"Mountaineering and ice climbing","url":"/products/climbing/gear/mountaineering-and-ice-climbing/c/1506","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Mountaineering boots","uetTitle":"Mountaineering boots","url":"/products/climbing/mountaineering-and-ice-climbing/mountaineering-boots/c/1501","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|mountaineering boots","label":"/products/climbing/mountaineering-and-ice-climbing/mountaineering-boots/c/1501"}},{"title":"Crampons","uetTitle":"Crampons","url":"/products/climbing/mountaineering-and-ice-climbing/crampons-and-components/c/306","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|crampons","label":"/products/climbing/mountaineering-and-ice-climbing/crampons-and-components/c/306"}},{"title":"Mountaineering axes","uetTitle":"Mountaineering axes","url":"/products/climbing/mountaineering-and-ice-climbing/mountaineering-axes/c/974","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|mountaineering axes","label":"/products/climbing/mountaineering-and-ice-climbing/mountaineering-axes/c/974"}},{"title":"Ice tools","uetTitle":"Ice tools","url":"/products/climbing/mountaineering-and-ice-climbing/ice-tools-and-components/c/968","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|ice tools","label":"/products/climbing/mountaineering-and-ice-climbing/ice-tools-and-components/c/968"}},{"title":"Ice screws","uetTitle":"Ice screws","url":"/products/climbing/mountaineering-and-ice-climbing/ice-protection/c/970","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|ice screws","label":"/products/climbing/mountaineering-and-ice-climbing/ice-protection/c/970"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|mountaineering and ice climbing","label":"/products/climbing/gear/mountaineering-and-ice-climbing/c/1506"}},{"title":"Bouldering","uetTitle":"Bouldering","url":"/products/climbing/bouldering/c/307","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Crash pads","uetTitle":"Crash pads","url":"/products/climbing/bouldering/crash-pads/c/1059","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|crash pads","label":"/products/climbing/bouldering/crash-pads/c/1059"}},{"title":"Rock climbing shoes","uetTitle":"Rock climbing shoes","url":"/products/climbing/climbing-footwear/rock-climbing-shoes/c/1190?b=100-301-307","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|rock climbing shoes","label":"/products/climbing/climbing-footwear/rock-climbing-shoes/c/1190?b=100-301-307"}},{"title":"Chalk and chalk bags","uetTitle":"Chalk and chalk bags","url":"/products/climbing/bouldering/chalk-and-chalk-bags/c/954","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|chalk and chalk bags","label":"/products/climbing/bouldering/chalk-and-chalk-bags/c/954"}},{"title":"Slacklines","uetTitle":"Slacklines","url":"/products/climbing/slacklines/c/1469?b=100-301-307","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|slacklines","label":"/products/climbing/slacklines/c/1469?b=100-301-307"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|bouldering","label":"/products/climbing/bouldering/c/307"}},{"title":"Gym climbing","uetTitle":"Gym climbing","url":"/en/products/climbing/gym-climbing-and-indoor-training/c/308","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Harnesses","uetTitle":"Harnesses","url":"/en/products/climbing/gym-climbing-and-indoor-training/climbing-harnesses/c/957","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|harnesses","label":"/en/products/climbing/gym-climbing-and-indoor-training/climbing-harnesses/c/957"}},{"title":"Chalk and chalk bags","uetTitle":"Chalk and chalk bags","url":"/en/products/climbing/bouldering/chalk-and-chalk-bags/c/954?b=100-301-308","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|chalk and chalk bags","label":"/en/products/climbing/bouldering/chalk-and-chalk-bags/c/954?b=100-301-308"}},{"title":"Belay devices","uetTitle":"Belay devices","url":"/en/products/climbing/rock-climbing/uppers-and-downers/belay-devices/c/978?b=100-301-308","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|belay devices","label":"/en/products/climbing/rock-climbing/uppers-and-downers/belay-devices/c/978?b=100-301-308"}},{"title":"Locking carabiners","uetTitle":"Locking carabiners","url":"/en/products/climbing/rock-climbing/carabiners-and-draws/locking-carabiners/c/951?b=100-301-308","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|locking carabiners","label":"/en/products/climbing/rock-climbing/carabiners-and-draws/locking-carabiners/c/951?b=100-301-308"}},{"title":"Holds","uetTitle":"Holds","url":"/en/products/climbing/gym-climbing-and-indoor-training/climbing-holds/c/1461","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|holds","label":"/en/products/climbing/gym-climbing-and-indoor-training/climbing-holds/c/1461"}},{"title":"Training gear","uetTitle":"Training gear","url":"/en/products/climbing/gym-climbing-and-indoor-training/climbing-training-gear/c/1462","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|training gear","label":"/en/products/climbing/gym-climbing-and-indoor-training/climbing-training-gear/c/1462"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|gym climbing","label":"/en/products/climbing/gym-climbing-and-indoor-training/c/308"}},{"title":"Packs and bags","uetTitle":"Packs and bags","url":"/en/products/climbing/rock-climbing/climbing-packs-and-bags/c/316","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Climbing packs","uetTitle":"Climbing packs","url":"/en/products/climbing/rock-climbing/climbing-packs-and-bags/climbing-packs/c/315","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|climbing packs","label":"/en/products/climbing/rock-climbing/climbing-packs-and-bags/climbing-packs/c/315"}},{"title":"Rope bags","uetTitle":"Rope bags","url":"/en/products/climbing/rock-climbing/ropes-cords-and-slings/rope-bags-and-accessories/c/1393?b=100-301-309-316","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|rope bags","label":"/en/products/climbing/rock-climbing/ropes-cords-and-slings/rope-bags-and-accessories/c/1393?b=100-301-309-316"}},{"title":"Haul bags","uetTitle":"Haul bags","url":"/en/products/packs-and-bags/haul-bags/c/1335?b=100-301-309-316","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|haul bags","label":"/en/products/packs-and-bags/haul-bags/c/1335?b=100-301-309-316"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|packs and bags","label":"/en/products/climbing/rock-climbing/climbing-packs-and-bags/c/316"}},{"title":"Climbing clothing","uetTitle":"Climbing clothing","url":"/products/climbing/clothes/c/286","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Tops","uetTitle":"Tops","url":"/en/products/climbing/clothes/tops/c/284","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|tops","label":"/en/products/climbing/clothes/tops/c/284"}},{"title":"Bottoms","uetTitle":"Bottoms","url":"/en/products/climbing/clothes/bottoms/c/285","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|bottoms","label":"/en/products/climbing/clothes/bottoms/c/285"}},{"title":"Base layers","uetTitle":"Base layers","url":"/en/ideal-for/climbing/products/clothing/base-layers-and-underwear/base-layers-and-underwear/c/273","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|base layers","label":"/en/ideal-for/climbing/products/clothing/base-layers-and-underwear/base-layers-and-underwear/c/273"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|climbing clothing","label":"/products/climbing/clothes/c/286"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all climbing","uetTitle":"Shop all climbing","url":"/en/products/climbing/c/301","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|shop all climbing","label":"/en/products/climbing/c/301"}},{"title":"New arrivals","uetTitle":"New arrivals","url":"/products/climbing/c/301?f=featureCollection%3Anew","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|new arrivals","label":"/products/climbing/c/301?f=featurecollection%3anew"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/climbing/c/301?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|deals","label":"/en/products/climbing/c/301?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Climbing tips","uetTitle":"Climbing tips","url":"/en/explore/climbing","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|climbing tips","label":"/en/explore/climbing"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"climb|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"climb"}},{"title":"Water","uetTitle":"Water","url":"#/water","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Watersports activities","uetTitle":"Watersports activities","url":"/products/watersports/c/1550","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Paddleboarding","uetTitle":"Paddleboarding","url":"/products/watersports/paddleboarding/c/359","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|paddleboarding","label":"/products/watersports/paddleboarding/c/359"}},{"title":"Kayaking","uetTitle":"Kayaking","url":"/products/watersports/kayaking/c/354","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|kayaking","label":"/products/watersports/kayaking/c/354"}},{"title":"Canoeing","uetTitle":"Canoeing","url":"/products/watersports/canoeing/c/350","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|canoeing","label":"/products/watersports/canoeing/c/350"}},{"title":"Snorkelling","uetTitle":"Snorkelling","url":"/en/products/watersports/snorkel-gear/c/1417","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|snorkelling","label":"/en/products/watersports/snorkel-gear/c/1417"}},{"title":"Fitness swimming","uetTitle":"Fitness swimming","url":"/products/watersports/swim-fitness/c/1471?b=100-1550","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|fitness swimming","label":"/products/watersports/swim-fitness/c/1471?b=100-1550"}},{"title":"Surfing","uetTitle":"Surfing","url":"/products/watersports/surfing/c/378","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|surfing","label":"/products/watersports/surfing/c/378"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|watersports activities","label":"/products/watersports/c/1550"}},{"title":"Watersports clothing","uetTitle":"Watersports clothing","url":"/products/watersports/watersports-clothing/c/369","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Wetsuits and neoprene clothing","uetTitle":"Wetsuits and neoprene clothing","url":"/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/c/1058","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|wetsuits and neoprene clothing","label":"/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/c/1058"}},{"title":"Dry suits, tops and bottoms","uetTitle":"Dry suits, tops and bottoms","url":"/products/watersports/watersports-clothing/dry-suits-and-tops/c/1016","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|dry suits, tops and bottoms","label":"/products/watersports/watersports-clothing/dry-suits-and-tops/c/1016"}},{"title":"Rashguards and UPF clothing","uetTitle":"Rashguards and UPF clothing","url":"/en/products/clothing/swimwear/rashguards-and-sunguards/c/1041","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|rashguards and upf clothing","label":"/en/products/clothing/swimwear/rashguards-and-sunguards/c/1041"}},{"title":"Swimwear","uetTitle":"Swimwear","url":"/products/clothing/swimwear/c/1036?b=100-1550-369","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|swimwear","label":"/products/clothing/swimwear/c/1036?b=100-1550-369"}},{"title":"Paddling tops and pants","uetTitle":"Paddling tops and pants","url":"/products/watersports/watersports-clothing/paddling-tops-and-pants/c/385","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|paddling tops and pants","label":"/products/watersports/watersports-clothing/paddling-tops-and-pants/c/385"}},{"title":"Paddling gloves and mitts","uetTitle":"Paddling gloves and mitts","url":"/en/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/paddling-gloves-and-mitts/c/1544","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|paddling gloves and mitts","label":"/en/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/paddling-gloves-and-mitts/c/1544"}},{"title":"Sun hats","uetTitle":"Sun hats","url":"/en/products/clothing/clothing-accessories/headwear/sun-hats/c/998?f=CFIdealForSimple%3AWatersports","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|sun hats","label":"/en/products/clothing/clothing-accessories/headwear/sun-hats/c/998?f=cfidealforsimple%3awatersports"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|watersports clothing","label":"/products/watersports/watersports-clothing/c/369"}},{"title":"PFDs, helmets and safety ","uetTitle":"PFDs, helmets and safety ","url":"/products/watersports/canoeing/pfds-helmets-and-safety-equipment/c/1395","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"PFDs","uetTitle":"PFDs","url":"/products/watersports/canoeing/pfds-helmets-and-safety-equipment/pfds/c/1398","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|pfds","label":"/products/watersports/canoeing/pfds-helmets-and-safety-equipment/pfds/c/1398"}},{"title":"Boat safety","uetTitle":"Boat safety","url":"/en/products/watersports/pfds-helmets-and-safety-equipment/boat-safety-equipment/c/1396","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|boat safety","label":"/en/products/watersports/pfds-helmets-and-safety-equipment/boat-safety-equipment/c/1396"}},{"title":"Helmets","uetTitle":"Helmets","url":"/products/watersports/canoeing/pfds-helmets-and-safety-equipment/paddling-helmets/c/1571","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|helmets","label":"/products/watersports/canoeing/pfds-helmets-and-safety-equipment/paddling-helmets/c/1571"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|pfds, helmets and safety ","label":"/products/watersports/canoeing/pfds-helmets-and-safety-equipment/c/1395"}},{"title":"Footwear","uetTitle":"Footwear","url":"/products/watersports/watersports-footwear/c/376","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Neoprene boots","uetTitle":"Neoprene boots","url":"/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/neoprene-boots/c/374?b=100-1550-376","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|neoprene boots","label":"/products/watersports/watersports-clothing/wetsuits-and-neoprene-clothing/neoprene-boots/c/374?b=100-1550-376"}},{"title":"Water shoes","uetTitle":"Water shoes","url":"/products/watersports/watersports-footwear/water-shoes/c/1494","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|water shoes","label":"/products/watersports/watersports-footwear/water-shoes/c/1494"}},{"title":"Water sandals","uetTitle":"Water sandals","url":"/products/watersports/watersports-footwear/water-sandals/c/1801","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|water sandals","label":"/products/watersports/watersports-footwear/water-sandals/c/1801"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|footwear","label":"/products/watersports/watersports-footwear/c/376"}},{"title":"Dry bags, waterproof cases and portage bags","uetTitle":"Dry bags, waterproof cases and portage bags","url":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/c/1357","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Dry bags","uetTitle":"Dry bags","url":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/dry-bags/c/1358","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|dry bags","label":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/dry-bags/c/1358"}},{"title":"Portage bags","uetTitle":"Portage bags","url":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/portage-bags/c/1362","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|portage bags","label":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/portage-bags/c/1362"}},{"title":"Gear barrels","uetTitle":"Gear barrels","url":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/gear-barrels/c/1359","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|gear barrels","label":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/gear-barrels/c/1359"}},{"title":"Hard cases","uetTitle":"Hard cases","url":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/hard-cases/c/1360","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|hard cases","label":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/hard-cases/c/1360"}},{"title":"Camera and electronics cases","uetTitle":"Camera and electronics cases","url":"/products/camping-and-hiking/electronics/camera-bags2c-tripods-and-accessories/c/1128?b=100-1550-350-1357","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|camera and electronics cases","label":"/products/camping-and-hiking/electronics/camera-bags2c-tripods-and-accessories/c/1128?b=100-1550-350-1357"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|dry bags, waterproof cases and portage bags","label":"/products/watersports/canoeing/dry-bags-waterproof-cases-and-portage-bags/c/1357"}},{"title":"Marine navigation and GPS","uetTitle":"Marine navigation and GPS","url":"/en/products/watersports/marine-navigation/c/364","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|marine navigation and gps","label":"/en/products/watersports/marine-navigation/c/364"}},{"title":"Sun protection","uetTitle":"Sun protection","url":"/en/products/camping-and-hiking/health-and-safety/sun-protection/c/1216","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|sun protection","label":"/en/products/camping-and-hiking/health-and-safety/sun-protection/c/1216"}},{"title":"Books and maps","uetTitle":"Books and maps","url":"/en/products/watersports/c/1550?f=categorySelect%3A938%3AcategorySelect%3A363","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|books and maps","label":"/en/products/watersports/c/1550?f=categoryselect%3a938%3acategoryselect%3a363"}},{"title":"Water - Sunglasses - Nav node V2","uetTitle":"Water - Sunglasses - Nav node V2","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|water - sunglasses - nav node v2","label":""}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all watersports","uetTitle":"Shop all watersports","url":"/en/products/watersports/c/1550","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|shop all watersports","label":"/en/products/watersports/c/1550"}},{"title":"New arrivals","uetTitle":"New arrivals","url":"/products/watersports/c/1550?f=featureCollection%3Anew&sort=newest","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|new arrivals","label":"/products/watersports/c/1550?f=featurecollection%3anew&sort=newest"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/watersports/c/1550?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|deals","label":"/en/products/watersports/c/1550?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Watersports tips","uetTitle":"Watersports tips","url":"/en/explore/watersports","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|watersports tips","label":"/en/explore/watersports"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"water|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"water"}},{"title":"Packs & Travel","uetTitle":"Packs & Travel","url":"#/packsandtravel","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Packs and bags","uetTitle":"Packs and bags","url":"/products/packs-and-bags/c/1326","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Backpacking packs","uetTitle":"Backpacking packs","url":"/products/packs-and-bags/backpacking-packs/c/1338","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|backpacking packs","label":"/products/packs-and-bags/backpacking-packs/c/1338"}},{"title":"Daypacks and school bags","uetTitle":"Daypacks and school bags","url":"/products/packs-and-bags/daypacks-slings-and-school-bags/c/1332","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|daypacks and school bags","label":"/products/packs-and-bags/daypacks-slings-and-school-bags/c/1332"}},{"title":"Child carrier backpacks","uetTitle":"Child carrier backpacks","url":"/products/travel-gear/kid-transport/child-carrier-backpacks/c/1258","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|child carrier backpacks","label":"/products/travel-gear/kid-transport/child-carrier-backpacks/c/1258"}},{"title":"Running packs","uetTitle":"Running packs","url":"/en/products/run-and-fitness/running-packs/c/291","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|running packs","label":"/en/products/run-and-fitness/running-packs/c/291"}},{"title":"Hydration packs and accessories","uetTitle":"Hydration packs and accessories","url":"/en/products/packs-and-bags/hydration-packs-and-accessories/c/640","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|hydration packs and accessories","label":"/en/products/packs-and-bags/hydration-packs-and-accessories/c/640"}},{"title":"Shoulder bags and slings","uetTitle":"Shoulder bags and slings","url":"/products/packs-and-bags/shoulder-bags-and-waist-packs/shoulder-bags-and-purses/c/1346","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|shoulder bags and slings","label":"/products/packs-and-bags/shoulder-bags-and-waist-packs/shoulder-bags-and-purses/c/1346"}},{"title":"Waist packs","uetTitle":"Waist packs","url":"/products/packs-and-bags/shoulder-bags-and-waist-packs/waist-packs/c/1356","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|waist packs","label":"/products/packs-and-bags/shoulder-bags-and-waist-packs/waist-packs/c/1356"}},{"title":"Pack accessories","uetTitle":"Pack accessories","url":"/en/products/packs-and-bags/pack-accessories/c/630","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|pack accessories","label":"/en/products/packs-and-bags/pack-accessories/c/630"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|packs and bags","label":"/products/packs-and-bags/c/1326"}},{"title":"Luggage","uetTitle":"Luggage","url":"/products/packs-and-bags/luggage/c/1350","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Duffle bags","uetTitle":"Duffle bags","url":"/products/packs-and-bags/luggage/duffle-bags/c/1351","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|duffle bags","label":"/products/packs-and-bags/luggage/duffle-bags/c/1351"}},{"title":"Travel packs","uetTitle":"Travel packs","url":"/products/packs-and-bags/luggage/travel-packs/c/1353","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|travel packs","label":"/products/packs-and-bags/luggage/travel-packs/c/1353"}},{"title":"Rolling bags","uetTitle":"Rolling bags","url":"/products/packs-and-bags/luggage/rolling-bags/c/1352","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|rolling bags","label":"/products/packs-and-bags/luggage/rolling-bags/c/1352"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|luggage","label":"/products/packs-and-bags/luggage/c/1350"}},{"title":"Travel accessories","uetTitle":"Travel accessories","url":"/products/travel-gear/travel-accessories/c/600","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Packing organizers","uetTitle":"Packing organizers","url":"/products/travel-gear/travel-accessories/travel-pouches-and-packing-organizers/c/1354","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|packing organizers","label":"/products/travel-gear/travel-accessories/travel-pouches-and-packing-organizers/c/1354"}},{"title":"Money belts and wallets","uetTitle":"Money belts and wallets","url":"/products/travel-gear/money-belts-and-wallets/c/1355","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|money belts and wallets","label":"/products/travel-gear/money-belts-and-wallets/c/1355"}},{"title":"Pillows","uetTitle":"Pillows","url":"/products/travel-gear/travel-accessories/pillows/c/1376","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|pillows","label":"/products/travel-gear/travel-accessories/pillows/c/1376"}},{"title":"Sun protection","uetTitle":"Sun protection","url":"/products/camping-and-hiking/first-aid-health-and-safety/sun-protection/c/1216","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|sun protection","label":"/products/camping-and-hiking/first-aid-health-and-safety/sun-protection/c/1216"}},{"title":"Travel electronics","uetTitle":"Travel electronics","url":"/products/travel-gear/travel-electronics/c/266","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|travel electronics","label":"/products/travel-gear/travel-electronics/c/266"}},{"title":"Locks, tags and flags","uetTitle":"Locks, tags and flags","url":"/locks-tags-and-flags/c/1349","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|locks, tags and flags","label":"/locks-tags-and-flags/c/1349"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|travel accessories","label":"/products/travel-gear/travel-accessories/c/600"}},{"title":"Travel clothing","uetTitle":"Travel clothing","url":"/ideal-for/travel/products/clothing/c/981","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Jackets","uetTitle":"Jackets","url":"/ideal-for/travel/products/clothing/jackets/c/1018","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|jackets","label":"/ideal-for/travel/products/clothing/jackets/c/1018"}},{"title":"Shirts and tops","uetTitle":"Shirts and tops","url":"/ideal-for/travel/products/clothing/shirts-and-tops/c/1044","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|shirts and tops","label":"/ideal-for/travel/products/clothing/shirts-and-tops/c/1044"}},{"title":"Bottoms","uetTitle":"Bottoms","url":"/ideal-for/travel/products/clothing/bottoms/c/1002","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|bottoms","label":"/ideal-for/travel/products/clothing/bottoms/c/1002"}},{"title":"Hats and accessories ","uetTitle":"Hats and accessories ","url":"/ideal-for/travel/products/clothing/clothing-accessories/c/982","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|hats and accessories ","label":"/ideal-for/travel/products/clothing/clothing-accessories/c/982"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|travel clothing","label":"/ideal-for/travel/products/clothing/c/981"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all packs and bags","uetTitle":"Shop all packs and bags","url":"/en/products/packs-and-bags/c/1326","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|shop all packs and bags","label":"/en/products/packs-and-bags/c/1326"}},{"title":"Deals","uetTitle":"Deals","url":"https://www.mec.ca/en/products/packs-and-bags/c/1326?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|deals","label":"https://www.mec.ca/en/products/packs-and-bags/c/1326?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"packs & travel|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"packs & travel"}},{"title":"Run & Fitness","uetTitle":"Run & Fitness","url":"#/run","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Footwear","uetTitle":"Footwear","url":"/products/run-and-fitness/running-and-training-footwear/c/200","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Road running shoes","uetTitle":"Road running shoes","url":"/products/run-and-fitness/running-and-training-footwear/running-shoes/road-running-shoes/c/1731","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|road running shoes","label":"/products/run-and-fitness/running-and-training-footwear/running-shoes/road-running-shoes/c/1731"}},{"title":"Trail running shoes","uetTitle":"Trail running shoes","url":"/products/run-and-fitness/running-and-training-footwear/running-shoes/trail-running-shoes/c/1730","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|trail running shoes","label":"/products/run-and-fitness/running-and-training-footwear/running-shoes/trail-running-shoes/c/1730"}},{"title":"Gym training shoes","uetTitle":"Gym training shoes","url":"/products/run-and-fitness/running-and-training-footwear/gym-training-shoes/c/1495","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|gym training shoes","label":"/products/run-and-fitness/running-and-training-footwear/gym-training-shoes/c/1495"}},{"title":"Traction devices","uetTitle":"Traction devices","url":"/products/run-and-fitness/running-and-training-footwear/traction-devices/c/1204","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|traction devices","label":"/products/run-and-fitness/running-and-training-footwear/traction-devices/c/1204"}},{"title":"Socks","uetTitle":"Socks","url":"/products/run-and-fitness/running-clothing/clothing-accessories/running-and-training-socks/c/1521?b=100-1552-200","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|socks","label":"/products/run-and-fitness/running-clothing/clothing-accessories/running-and-training-socks/c/1521?b=100-1552-200"}},{"title":"Insoles","uetTitle":"Insoles","url":"/en/products/footwear/accessories/insoles/c/1187","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|insoles","label":"/en/products/footwear/accessories/insoles/c/1187"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|footwear","label":"/products/run-and-fitness/running-and-training-footwear/c/200"}},{"title":"Running and fitness clothing","uetTitle":"Running and fitness clothing","url":"/products/run-and-fitness/running-clothing/c/1573","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shirts and tops","uetTitle":"Shirts and tops","url":"/products/run-and-fitness/running-clothing/running-shirts-and-tops/c/1574","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|shirts and tops","label":"/products/run-and-fitness/running-clothing/running-shirts-and-tops/c/1574"}},{"title":"Shorts, tights and pants","uetTitle":"Shorts, tights and pants","url":"/products/run-and-fitness/running-clothing/running-and-fitness-bottoms/c/1578","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|shorts, tights and pants","label":"/products/run-and-fitness/running-clothing/running-and-fitness-bottoms/c/1578"}},{"title":"Jackets","uetTitle":"Jackets","url":"/products/run-and-fitness/running-clothing/running-and-cross-country-jackets/c/1026","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|jackets","label":"/products/run-and-fitness/running-clothing/running-and-cross-country-jackets/c/1026"}},{"title":"Base layers","uetTitle":"Base layers","url":"/en/products/clothing/base-layers-and-underwear/base-layers-and-underwear/c/273","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|base layers","label":"/en/products/clothing/base-layers-and-underwear/base-layers-and-underwear/c/273"}},{"title":"Accessories","uetTitle":"Accessories","url":"/products/run-and-fitness/running-clothing/clothing-accessories/c/1579","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|accessories","label":"/products/run-and-fitness/running-clothing/clothing-accessories/c/1579"}},{"title":"Sports bras","uetTitle":"Sports bras","url":"/products/run-and-fitness/running-clothing/sports-bras/c/1057","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|sports bras","label":"/products/run-and-fitness/running-clothing/sports-bras/c/1057"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|running and fitness clothing","label":"/products/run-and-fitness/running-clothing/c/1573"}},{"title":"Electronics","uetTitle":"Electronics","url":"/products/run-and-fitness/training-running-and-fitness-electronics/c/1567","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Watches","uetTitle":"Watches","url":"/en/products/camping-and-hiking/electronics/watches/c/1153?b=100-1552-1567","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|watches","label":"/en/products/camping-and-hiking/electronics/watches/c/1153?b=100-1552-1567"}},{"title":"Heart rate monitor straps","uetTitle":"Heart rate monitor straps","url":"/en/products/run-and-fitness/training-electronics/sensors-mounts-and-accessories/c/1156","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|heart rate monitor straps","label":"/en/products/run-and-fitness/training-electronics/sensors-mounts-and-accessories/c/1156"}},{"title":"Headphones","uetTitle":"Headphones","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/earphones/c/1138?b=100-1552-1567","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|headphones","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/earphones/c/1138?b=100-1552-1567"}},{"title":"Running headlamps","uetTitle":"Running headlamps","url":"/ideal-for/running/products/camping-and-hiking/tools-lighting-and-accessories/headlamps-and-lighting/headlamps/c/1306?b=100-1552","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|running headlamps","label":"/ideal-for/running/products/camping-and-hiking/tools-lighting-and-accessories/headlamps-and-lighting/headlamps/c/1306?b=100-1552"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|electronics","label":"/products/run-and-fitness/training-running-and-fitness-electronics/c/1567"}},{"title":"Packs and bags","uetTitle":"Packs and bags","url":"/products/run-and-fitness/gym-bags-run-vests-and-hydration-packs/c/291","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Hydration packs","uetTitle":"Hydration packs","url":"/products/packs-and-bags/hydration-packs-and-accessories/hydration-packs/c/1715?b=100-1552-291-640","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|hydration packs","label":"/products/packs-and-bags/hydration-packs-and-accessories/hydration-packs/c/1715?b=100-1552-291-640"}},{"title":"Waist packs","uetTitle":"Waist packs","url":"/ideal-for/running/products/packs-and-bags/shoulder-bags-and-waist-packs/waist-packs/c/1356","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|waist packs","label":"/ideal-for/running/products/packs-and-bags/shoulder-bags-and-waist-packs/waist-packs/c/1356"}},{"title":"Running vests","uetTitle":"Running vests","url":"/products/camping-and-hiking/camp-kitchen/water-bottles-and-reservoirs/running-vests-and-belts/c/1231","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|running vests","label":"/products/camping-and-hiking/camp-kitchen/water-bottles-and-reservoirs/running-vests-and-belts/c/1231"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|packs and bags","label":"/products/run-and-fitness/gym-bags-run-vests-and-hydration-packs/c/291"}},{"title":"Hydration and energy","uetTitle":"Hydration and energy","url":"/products/run-and-fitness/training-food-and-drinks/c/1580","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Water bottles","uetTitle":"Water bottles","url":"/products/camping-and-hiking/camp-kitchen/water-bottles-and-reservoirs/water-bottles/c/1233?b=100-1552","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|water bottles","label":"/products/camping-and-hiking/camp-kitchen/water-bottles-and-reservoirs/water-bottles/c/1233?b=100-1552"}},{"title":"Water bladders","uetTitle":"Water bladders","url":"/products/packs-and-bags/hydration-packs-and-accessories/bladders-reservoirs-and-accessories/c/1229?b=100-1552-291-640","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|water bladders","label":"/products/packs-and-bags/hydration-packs-and-accessories/bladders-reservoirs-and-accessories/c/1229?b=100-1552-291-640"}},{"title":"Energy and protein bars","uetTitle":"Energy and protein bars","url":"/products/camping-and-hiking/kitchen-and-hydration/food-and-drink/snacks-and-energy-bars/energy-and-protein-bars/c/1178?b=100-1552-1580","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|energy and protein bars","label":"/products/camping-and-hiking/kitchen-and-hydration/food-and-drink/snacks-and-energy-bars/energy-and-protein-bars/c/1178?b=100-1552-1580"}},{"title":"Energy gels and chews","uetTitle":"Energy gels and chews","url":"/products/run-and-fitness/training-food-and-drinks/energy-gels-and-chews/c/1179","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|energy gels and chews","label":"/products/run-and-fitness/training-food-and-drinks/energy-gels-and-chews/c/1179"}},{"title":"Energy and recovery drinks","uetTitle":"Energy and recovery drinks","url":"/products/camping-and-hiking/food-and-drink/drinks/energy-and-recovery-drinks/c/1176?b=100-1552-1580","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|energy and recovery drinks","label":"/products/camping-and-hiking/food-and-drink/drinks/energy-and-recovery-drinks/c/1176?b=100-1552-1580"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|hydration and energy","label":"/products/run-and-fitness/training-food-and-drinks/c/1580"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all running","uetTitle":"Shop all running","url":"/en/products/run-and-fitness/c/1552","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|shop all running","label":"/en/products/run-and-fitness/c/1552"}},{"title":"New arrivals","uetTitle":"New arrivals","url":"/en/products/run-and-fitness/c/1552?f=featureCollection%3Anew","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|new arrivals","label":"/en/products/run-and-fitness/c/1552?f=featurecollection%3anew"}},{"title":"Trail run collection","uetTitle":"Trail run collection","url":"/en/products/run-and-fitness/c/1552?f=CFSeasonalCollections%3ATrail+run+collection","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|trail run collection","label":"/en/products/run-and-fitness/c/1552?f=cfseasonalcollections%3atrail+run+collection"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/run-and-fitness/c/1552?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|deals","label":"/en/products/run-and-fitness/c/1552?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Run and fitness tips","uetTitle":"Run and fitness tips","url":"/en/explore/training-and-fitness","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|run and fitness tips","label":"/en/explore/training-and-fitness"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"run & fitness|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"run & fitness"}},{"title":"Snow","uetTitle":"Snow","url":"#/snow","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Backcountry skiing","uetTitle":"Backcountry skiing","url":"/en/products/snow/backcountry-skiing/c/2068","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Skis ","uetTitle":"Skis ","url":"/en/products/snow/backcountry-skiing/skis/c/2069","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|skis ","label":"/en/products/snow/backcountry-skiing/skis/c/2069"}},{"title":"Boots","uetTitle":"Boots","url":"/en/products/snow/backcountry-skiing/boots/c/2072","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|boots","label":"/en/products/snow/backcountry-skiing/boots/c/2072"}},{"title":"Bindings","uetTitle":"Bindings","url":"/en/products/snow/backcountry-skiing/bindings/c/2073","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|bindings","label":"/en/products/snow/backcountry-skiing/bindings/c/2073"}},{"title":"Poles","uetTitle":"Poles","url":"/en/products/snow/backcountry-skiing/poles/c/2071","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|poles","label":"/en/products/snow/backcountry-skiing/poles/c/2071"}},{"title":"Climbing skins","uetTitle":"Climbing skins","url":"/en/products/snow/backcountry-skiing/climbing-skins/c/2076","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|climbing skins","label":"/en/products/snow/backcountry-skiing/climbing-skins/c/2076"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|backcountry skiing","label":"/en/products/snow/backcountry-skiing/c/2068"}},{"title":"Downhill skiing","uetTitle":"Downhill skiing","url":"/en/products/snow/downhill-skiing/c/2099","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Skis","uetTitle":"Skis","url":"/en/products/snow/downhill-skiing/skis/c/2100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|skis","label":"/en/products/snow/downhill-skiing/skis/c/2100"}},{"title":"Boots","uetTitle":"Boots","url":"/en/products/snow/downhill-skiing/boots/c/2104","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|boots","label":"/en/products/snow/downhill-skiing/boots/c/2104"}},{"title":"Bindings","uetTitle":"Bindings","url":"/en/products/snow/downhill-skiing/bindings/c/2101","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|bindings","label":"/en/products/snow/downhill-skiing/bindings/c/2101"}},{"title":"Poles","uetTitle":"Poles","url":"/en/products/snow/downhill-skiing/poles/c/2102","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|poles","label":"/en/products/snow/downhill-skiing/poles/c/2102"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|downhill skiing","label":"/en/products/snow/downhill-skiing/c/2099"}},{"title":"Cross country skiing","uetTitle":"Cross country skiing","url":"/en/products/snow/cross-country-skiing/c/2089","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Classic","uetTitle":"Classic","url":"/en/products/snow/cross-country-skiing/classic/c/2148","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|classic","label":"/en/products/snow/cross-country-skiing/classic/c/2148"}},{"title":"Skate","uetTitle":"Skate","url":"/en/products/snow/cross-country-skiing/skate-skiing/c/2094","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|skate","label":"/en/products/snow/cross-country-skiing/skate-skiing/c/2094"}},{"title":"Off-track","uetTitle":"Off-track","url":"/en/products/snow/cross-country-skiing/off-track/c/2154","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|off-track","label":"/en/products/snow/cross-country-skiing/off-track/c/2154"}},{"title":"Ski wax and tuning","uetTitle":"Ski wax and tuning","url":"/en/ideal-for/cross_._country-skiing/products/snow/ski-tuning-tools/wax/c/2132","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski wax and tuning","label":"/en/ideal-for/cross_._country-skiing/products/snow/ski-tuning-tools/wax/c/2132"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|cross country skiing","label":"/en/products/snow/cross-country-skiing/c/2089"}},{"title":"Snowboarding","uetTitle":"Snowboarding","url":"/en/products/snow/snowboarding/c/2106","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Snowboards","uetTitle":"Snowboards","url":"/en/products/snow/snowboarding/snowboards/c/2107","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowboards","label":"/en/products/snow/snowboarding/snowboards/c/2107"}},{"title":"Snowboard bindings","uetTitle":"Snowboard bindings","url":"/en/products/snow/snowboarding/snowboard-bindings/c/2108","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowboard bindings","label":"/en/products/snow/snowboarding/snowboard-bindings/c/2108"}},{"title":"Snowboard boots","uetTitle":"Snowboard boots","url":"/en/products/snow/snowboarding/boots/c/2109","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowboard boots","label":"/en/products/snow/snowboarding/boots/c/2109"}},{"title":"Splitboards","uetTitle":"Splitboards","url":"/en/products/snow/snowboarding/splitboards/c/2110","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|splitboards","label":"/en/products/snow/snowboarding/splitboards/c/2110"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowboarding","label":"/en/products/snow/snowboarding/c/2106"}},{"title":"Snowshoeing","uetTitle":"Snowshoeing","url":"/en/products/snow/snowshoeing/c/2117","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Snowshoes","uetTitle":"Snowshoes","url":"/en/products/snow/snowshoeing/snowshoes/c/2118","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowshoes","label":"/en/products/snow/snowshoeing/snowshoes/c/2118"}},{"title":"Winter traction devices","uetTitle":"Winter traction devices","url":"/en/products/camping-and-hiking/hiking-footwear/footwear-accessories/traction-devices/c/1204?b=100-2067-2117","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|winter traction devices","label":"/en/products/camping-and-hiking/hiking-footwear/footwear-accessories/traction-devices/c/1204?b=100-2067-2117"}},{"title":"Winter boots","uetTitle":"Winter boots","url":"/en/products/footwear/boots/winter-boots/active-winter-boots/c/8000?b=100-2067-2117","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|winter boots","label":"/en/products/footwear/boots/winter-boots/active-winter-boots/c/8000?b=100-2067-2117"}},{"title":"Poles","uetTitle":"Poles","url":"/en/products/snow/backcountry-skiing/poles/c/2071?b=100-2067-2117","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|poles","label":"/en/products/snow/backcountry-skiing/poles/c/2071?b=100-2067-2117"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowshoeing","label":"/en/products/snow/snowshoeing/c/2117"}},{"title":"Clothing","uetTitle":"Clothing","url":"/en/products/snow/ski-clothes/c/2123","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Jackets","uetTitle":"Jackets","url":"/en/products/snow/ski-clothes/ski-board-jackets/c/1027","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|jackets","label":"/en/products/snow/ski-clothes/ski-board-jackets/c/1027"}},{"title":"Ski and snow pants","uetTitle":"Ski and snow pants","url":"/en/products/snow/ski-clothes/pants/c/2126","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski and snow pants","label":"/en/products/snow/ski-clothes/pants/c/2126"}},{"title":"Base layers","uetTitle":"Base layers","url":"/en/products/snow/ski-clothes/baselayers/c/2124","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|base layers","label":"/en/products/snow/ski-clothes/baselayers/c/2124"}},{"title":"Fleece and mid-layers","uetTitle":"Fleece and mid-layers","url":"/en/products/clothing/fleece-hoodies-and-sweaters/c/271?f=CFIdealForSimple%3ASnowsports","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|fleece and mid-layers","label":"/en/products/clothing/fleece-hoodies-and-sweaters/c/271?f=cfidealforsimple%3asnowsports"}},{"title":"Gloves and mittens","uetTitle":"Gloves and mittens","url":"/products/snowsports/downhill-skiing/clothes/ski-gloves-and-mitts/c/1547","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|gloves and mittens","label":"/products/snowsports/downhill-skiing/clothes/ski-gloves-and-mitts/c/1547"}},{"title":"Toques","uetTitle":"Toques","url":"/en/products/clothing/clothing-accessories/headwear/toques-and-beanies/c/1000?b=100-2067-2123-1104","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|toques","label":"/en/products/clothing/clothing-accessories/headwear/toques-and-beanies/c/1000?b=100-2067-2123-1104"}},{"title":"Snowsport socks","uetTitle":"Snowsport socks","url":"/en/products/snow/ski-clothes/snowsport-socks/c/1107","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowsport socks","label":"/en/products/snow/ski-clothes/snowsport-socks/c/1107"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|clothing","label":"/en/products/snow/ski-clothes/c/2123"}},{"title":"Essentials","uetTitle":"Essentials","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Helmets","uetTitle":"Helmets","url":"/en/products/snow/ski-snowboard-helmets/c/2138","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|helmets","label":"/en/products/snow/ski-snowboard-helmets/c/2138"}},{"title":"Goggles","uetTitle":"Goggles","url":"/en/products/snow/ski-snowboard-goggles/c/2137","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|goggles","label":"/en/products/snow/ski-snowboard-goggles/c/2137"}},{"title":"Glacier sunglasses","uetTitle":"Glacier sunglasses","url":"/en/products/snow/alpine-sunglasses/c/2139","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|glacier sunglasses","label":"/en/products/snow/alpine-sunglasses/c/2139"}},{"title":"Backpacks","uetTitle":"Backpacks","url":"/en/products/snow/ski-snowboard-backpacks/c/2136","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|backpacks","label":"/en/products/snow/ski-snowboard-backpacks/c/2136"}},{"title":"Ski straps","uetTitle":"Ski straps","url":"/en/products/snow/ski-straps/c/2142","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski straps","label":"/en/products/snow/ski-straps/c/2142"}},{"title":"Racks","uetTitle":"Racks","url":"/en/products/snow/ski-snowboard-racks/c/2140","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|racks","label":"/en/products/snow/ski-snowboard-racks/c/2140"}},{"title":"Ski and snowboard bags","uetTitle":"Ski and snowboard bags","url":"/en/products/snow/ski-snowboard-bags/c/2141","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski and snowboard bags","label":"/en/products/snow/ski-snowboard-bags/c/2141"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|essentials"}},{"title":"Avalanche safety gear","uetTitle":"Avalanche safety gear","url":"/en/products/snow/avalanche-safety-gear/c/2081","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Avalanche airbags","uetTitle":"Avalanche airbags","url":"/en/products/snow/avalanche-safety-gear/avalanche-air-bag/c/2084","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|avalanche airbags","label":"/en/products/snow/avalanche-safety-gear/avalanche-air-bag/c/2084"}},{"title":"Avalanche transceivers","uetTitle":"Avalanche transceivers","url":"/en/products/snow/avalanche-safety-gear/avalanche-beacons-transceivers/c/2086","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|avalanche transceivers","label":"/en/products/snow/avalanche-safety-gear/avalanche-beacons-transceivers/c/2086"}},{"title":"Avalanche shovels and saws","uetTitle":"Avalanche shovels and saws","url":"/en/products/snow/avalanche-safety-gear/avalanche-shovels-saws/c/2082","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|avalanche shovels and saws","label":"/en/products/snow/avalanche-safety-gear/avalanche-shovels-saws/c/2082"}},{"title":"Snow analysis","uetTitle":"Snow analysis","url":"/en/products/snow/avalanche-safety-gear/snow-analysis/c/2087","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snow analysis","label":"/en/products/snow/avalanche-safety-gear/snow-analysis/c/2087"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|avalanche safety gear","label":"/en/products/snow/avalanche-safety-gear/c/2081"}},{"title":"Ski tuning and tools","uetTitle":"Ski tuning and tools","url":"/en/products/snow/ski-tuning-tools/c/2131","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Ski wax","uetTitle":"Ski wax","url":"/en/products/snow/ski-tuning-tools/wax/c/2132","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski wax","label":"/en/products/snow/ski-tuning-tools/wax/c/2132"}},{"title":"Ski base cleaners","uetTitle":"Ski base cleaners","url":"/en/products/snow/ski-tuning-tools/cleaner/c/2133","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski base cleaners","label":"/en/products/snow/ski-tuning-tools/cleaner/c/2133"}},{"title":"Ski sharpening tools","uetTitle":"Ski sharpening tools","url":"/en/products/snow/ski-tuning-tools/sharpening-tools/c/2134","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski sharpening tools","label":"/en/products/snow/ski-tuning-tools/sharpening-tools/c/2134"}},{"title":"Ski wax stands, vises and tables","uetTitle":"Ski wax stands, vises and tables","url":"/en/products/snow/ski-tuning-tools/wax-stands-vise-tables/c/2135","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski wax stands, vises and tables","label":"/en/products/snow/ski-tuning-tools/wax-stands-vise-tables/c/2135"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|ski tuning and tools","label":"/en/products/snow/ski-tuning-tools/c/2131"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all snowsports","uetTitle":"Shop all snowsports","url":"/en/products/snow/c/2067","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|shop all snowsports","label":"/en/products/snow/c/2067"}},{"title":"New arrivals","uetTitle":"New arrivals","url":"/en/products/snow/c/2067?f=featureCollection%3Anew","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|new arrivals","label":"/en/products/snow/c/2067?f=featurecollection%3anew"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/snow/c/2067?f=featureCollection%3Aonclearance%3AfeatureCollection%3Aonsale","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|deals","label":"/en/products/snow/c/2067?f=featurecollection%3aonclearance%3afeaturecollection%3aonsale"}},{"title":"Snowsports tips","uetTitle":"Snowsports tips","url":"/en/explore/snowsports","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|snowsports tips","label":"/en/explore/snowsports"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"snow|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"snow"}},{"title":"Electronics","uetTitle":"Electronics","url":"#/electronics","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":["slide"]},"subnav":[{"title":"Watches and fitness trackers","uetTitle":"Watches and fitness trackers","url":"/products/run-and-fitness/training-running-and-fitness-electronics/c/1567","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"GPS watches","uetTitle":"GPS watches","url":"/products/run-and-fitness/training-running-and-fitness-electronics/running-watches/c/1155","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|gps watches","label":"/products/run-and-fitness/training-running-and-fitness-electronics/running-watches/c/1155"}},{"title":"Altimeter / barometer watches","uetTitle":"Altimeter / barometer watches","url":"/products/camping-and-hiking/electronics/watches/altimeter-barometer-watches/c/1154","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|altimeter / barometer watches","label":"/products/camping-and-hiking/electronics/watches/altimeter-barometer-watches/c/1154"}},{"title":"Sport watches","uetTitle":"Sport watches","url":"/products/camping-and-hiking/electronics/watches/sport-watches/c/1161","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|sport watches","label":"/products/camping-and-hiking/electronics/watches/sport-watches/c/1161"}},{"title":"Fitness trackers","uetTitle":"Fitness trackers","url":"/products/run-and-fitness/training-running-and-fitness-electronics/fitness-and-activity-trackers/c/1110","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|fitness trackers","label":"/products/run-and-fitness/training-running-and-fitness-electronics/fitness-and-activity-trackers/c/1110"}},{"title":"Sensors and accessories","uetTitle":"Sensors and accessories","url":"/products/camping-and-hiking/electronics/watches/sensors-mounts-and-accessories/c/1156","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|sensors and accessories","label":"/products/camping-and-hiking/electronics/watches/sensors-mounts-and-accessories/c/1156"}},{"title":"Bike computers","uetTitle":"Bike computers","url":"/products/cycling/training-and-electronics/bike-computers/c/1117","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|bike computers","label":"/products/cycling/training-and-electronics/bike-computers/c/1117"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|watches and fitness trackers","label":"/products/run-and-fitness/training-running-and-fitness-electronics/c/1567"}},{"title":"GPS and tranceivers","uetTitle":"GPS and tranceivers","url":"/products/camping-and-hiking/electronics/gps-navigation/c/1139","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Handheld GPS","uetTitle":"Handheld GPS","url":"/products/camping-and-hiking/electronics/gps-navigation/handheld-gps/c/1249","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|handheld gps","label":"/products/camping-and-hiking/electronics/gps-navigation/handheld-gps/c/1249"}},{"title":"Satellite communicators and locators","uetTitle":"Satellite communicators and locators","url":"/products/camping-and-hiking/health-and-safety/survival-and-emergency-gear/satellite-communicators-and-locators/c/1149","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|satellite communicators and locators","label":"/products/camping-and-hiking/health-and-safety/survival-and-emergency-gear/satellite-communicators-and-locators/c/1149"}},{"title":"Avalanche transceivers","uetTitle":"Avalanche transceivers","url":"/products/snowsports/backcountry-skiing/avalanche-and-backcountry-safety-gear/avalanche-beacons-and-transceivers/c/800","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|avalanche transceivers","label":"/products/snowsports/backcountry-skiing/avalanche-and-backcountry-safety-gear/avalanche-beacons-and-transceivers/c/800"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|gps and tranceivers","label":"/products/camping-and-hiking/electronics/gps-navigation/c/1139"}},{"title":"Cameras and accessories ","uetTitle":"Cameras and accessories ","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/action-cameras-and-accessories/c/1817","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Action cameras","uetTitle":"Action cameras","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/action-cameras-and-accessories/pov-helmet-cameras/c/1150","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|action cameras","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/action-cameras-and-accessories/pov-helmet-cameras/c/1150"}},{"title":"Accessories and mounts","uetTitle":"Accessories and mounts","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/action-cameras-and-accessories/camera-accessories-and-mounts/c/1129","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|accessories and mounts","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/action-cameras-and-accessories/camera-accessories-and-mounts/c/1129"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|cameras and accessories ","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/action-cameras-and-accessories/c/1817"}},{"title":"Music systems","uetTitle":"Music systems","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/c/1569","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Radios and music players","uetTitle":"Radios and music players","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/radios-and-bluetooth-speakers/c/1167","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|radios and music players","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/radios-and-bluetooth-speakers/c/1167"}},{"title":"Headphones","uetTitle":"Headphones","url":"/products/camping-and-hiking/electronics/audio-and-video-electronics/earphones/c/1138","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|headphones","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/earphones/c/1138"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|music systems","label":"/products/camping-and-hiking/electronics/audio-and-video-electronics/c/1569"}},{"title":"Solar and portable power ","uetTitle":"Solar and portable power ","url":"/products/camping-and-hiking/electronics/chargers-and-adapters/c/1132","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Solar chargers","uetTitle":"Solar chargers","url":"/products/camping-and-hiking/electronics/chargers-and-adapters/solar-chargers/c/1136","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|solar chargers","label":"/products/camping-and-hiking/electronics/chargers-and-adapters/solar-chargers/c/1136"}},{"title":"Portable power","uetTitle":"Portable power","url":"/products/camping-and-hiking/electronics/chargers-and-adapters/portable-chargers-and-power-packs/c/1570","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|portable power","label":"/products/camping-and-hiking/electronics/chargers-and-adapters/portable-chargers-and-power-packs/c/1570"}},{"title":"Batteries","uetTitle":"Batteries","url":"/products/camping-and-hiking/electronics/batteries/c/1113","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|batteries","label":"/products/camping-and-hiking/electronics/batteries/c/1113"}},{"title":"Adapters","uetTitle":"Adapters","url":"/products/camping-and-hiking/electronics/chargers-and-adapters/adapters/c/1133","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|adapters","label":"/products/camping-and-hiking/electronics/chargers-and-adapters/adapters/c/1133"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|solar and portable power ","label":"/products/camping-and-hiking/electronics/chargers-and-adapters/c/1132"}},{"title":"Electronics cases","uetTitle":"Electronics cases","url":"/products/camping-and-hiking/electronics/camera-bags2c-tripods-and-accessories/c/1128","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|electronics cases","label":"/products/camping-and-hiking/electronics/camera-bags2c-tripods-and-accessories/c/1128"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all electronics","uetTitle":"Shop all electronics","url":"/products/camping-and-hiking/electronics/c/1108","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|shop all electronics","label":"/products/camping-and-hiking/electronics/c/1108"}},{"title":"Deals","uetTitle":"Deals","url":"/en/products/camping-and-hiking/electronics/c/1108?f=featureCollection%3Aonsale%3AfeatureCollection%3Aonclearance","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|deals","label":"/en/products/camping-and-hiking/electronics/c/1108?f=featurecollection%3aonsale%3afeaturecollection%3aonclearance"}},{"title":"Gift cards","uetTitle":"Gift cards","url":"/en/product/5027-227/MEC-E-Gift-Card","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-activities","action":"electronics|gift cards","label":"/en/product/5027-227/mec-e-gift-card"}}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"activities","label":"electronics"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"activities","label":""}},{"title":"Brands","uetTitle":"Brands","url":"","image":"","skipSubNav":false,"features":{"horizontal":["noSubnav","megaBrands"],"vertical":["slide"]},"subnav":[{"title":"Top brands","uetTitle":"Top brands","url":"","image":"","skipSubNav":false,"features":{"horizontal":["imageList"],"vertical":["noPhoto"]},"subnav":[{"title":"MEC","uetTitle":"MEC","url":"/en/brand/mec/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h75/h64/9057980153886/MEC.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|mec","label":"/en/brand/mec/products/c/100"}},{"title":"Salomon","uetTitle":"Salomon","url":"/en/brand/salomon/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h13/he3/9057980547102/salomon.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|salomon","label":"/en/brand/salomon/products/c/100"}},{"title":"Garmin","uetTitle":"Garmin","url":"/en/brand/garmin/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h54/h22/9057980350494/garmin.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|garmin","label":"/en/brand/garmin/products/c/100"}},{"title":"Patagonia","uetTitle":"Patagonia","url":"/en/brand/patagonia/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h2d/hf6/9057980284958/patagonia.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|patagonia","label":"/en/brand/patagonia/products/c/100"}},{"title":"Arc'teryx","uetTitle":"Arc'teryx","url":"/en/brand/arc%27teryx/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h56/hcd/9057980219422/arcteryx.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|arc'teryx","label":"/en/brand/arc%27teryx/products/c/100"}},{"title":"The North Face","uetTitle":"The North Face","url":"/en/brand/the-north-face/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h0b/hb4/9057980481566/theNorthFace.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|the north face","label":"/en/brand/the-north-face/products/c/100"}},{"title":"Smartwool","uetTitle":"Smartwool","url":"/brand/smartwool/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/h49/h40/9151477153822/20-057-SmartwoolCoop-Web-D5-NavBarLogo-2x1-Nov9.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|smartwool","label":"/brand/smartwool/products/c/100"}},{"title":"Merrell","uetTitle":"Merrell","url":"/brand/merrell/products/c/100","image":"https://cdn.mec.ca/medias/sys_master/images/images/hb4/hcf/9156663672862/merrell-2x1-1-.png","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"top brands|merrell","label":"/brand/merrell/products/c/100"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"brands","label":"top brands"}},{"title":"Featured brands","uetTitle":"Featured brands","url":"","image":"","skipSubNav":false,"features":{"horizontal":["accordion"],"vertical":[]},"subnav":[{"title":"Prana","uetTitle":"Prana","url":"/en/brand/prana/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|prana","label":"/en/brand/prana/products/c/100"}},{"title":"Merrell","uetTitle":"Merrell","url":"/en/brand/merrell/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|merrell","label":"/en/brand/merrell/products/c/100"}},{"title":"Osprey","uetTitle":"Osprey","url":"/en/brand/osprey/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|osprey","label":"/en/brand/osprey/products/c/100"}},{"title":"Tentree","uetTitle":"Tentree","url":"/en/brand/Tentree/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|tentree","label":"/en/brand/tentree/products/c/100"}},{"title":"Nemo","uetTitle":"Nemo","url":"/en/brand/nemo/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|nemo","label":"/en/brand/nemo/products/c/100"}},{"title":"Keen","uetTitle":"Keen","url":"/en/p/keen","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|keen","label":"/en/p/keen"}},{"title":"Fjallraven","uetTitle":"Fjallraven","url":"/en/brand/fjallraven/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|fjallraven","label":"/en/brand/fjallraven/products/c/100"}},{"title":"Scarpa","uetTitle":"Scarpa","url":"/en/brand/scarpa/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|scarpa","label":"/en/brand/scarpa/products/c/100"}},{"title":"MSR","uetTitle":"MSR","url":"/en/brand/msr/products/c/100","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|msr","label":"/en/brand/msr/products/c/100"}},{"title":"Black Diamond","uetTitle":"Black Diamond","url":"/en/p/black-diamond","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-brands","action":"featured brands|black diamond","label":"/en/p/black-diamond"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"brands","label":"featured brands"}}],"groups":[{"title":"","url":"","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"Shop all brands","uetTitle":"Shop all brands","url":"/en/brands-all","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[]}],"groups":[]}],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"brands","label":""}},{"title":"About us","uetTitle":"About us","url":"#/aboutmec","image":"","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[{"title":"About MEC","uetTitle":"About MEC","url":"/en/explore/about-mec","image":"https://cdn.mec.ca/medias/sys_master/images/images/h20/h94/9019175141406/group-of-camping-friends-on-beach-Hero-5x2-AboutMEC.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"about mec"}},{"title":"MEC stores","uetTitle":"MEC stores","url":"/en/stores","image":"https://cdn.mec.ca/medias/sys_master/images/images/h49/h2c/9019174354974/MEC-Kelowna-Exterior-5x2.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"mec stores"}},{"title":"Help centre","uetTitle":"Help centre","url":"/en/explore/support","image":"https://cdn.mec.ca/medias/sys_master/images/images/h38/hcf/8835103784990/8834535948318.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"help centre"}},{"title":"Expert appointments","uetTitle":"Expert appointments","url":"/en/explore/expert-appointments","image":"https://cdn.mec.ca/medias/sys_master/images/images/hc7/hdc/9189971558430/21-007-ExpertAppts-web-D3-megamenu.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"expert appointments"}},{"title":"How-to articles","uetTitle":"How-to articles","url":"/en/explore/learn","image":"https://cdn.mec.ca/medias/sys_master/images/images/h3f/hf9/9129782312990/20-045-BrandAwareness-web-D4-MegaMenu-Aug20-ENFR.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"how-to articles"}},{"title":"MEC Blog","uetTitle":"MEC Blog","url":"/en/blog","image":"https://cdn.mec.ca/medias/sys_master/images/images/hdb/hee/9019173765150/SLorencePhoto-camplife16-065.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"mec blog"}},{"title":"Outdoor Impact","uetTitle":"Outdoor Impact","url":"/en/explore/outdoor-impact","image":"https://cdn.mec.ca/medias/sys_master/images/images/h27/ha7/9189971623966/21-009-Social-Impact-web-D6-megamenu-5x2-EN.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"outdoor impact"}},{"title":"Social & environmental accountability","uetTitle":"Social & environmental accountability","url":"/en/explore/sustainability-innovation","image":"https://cdn.mec.ca/medias/sys_master/images/images/hcc/h1e/9019175338014/16-IT-0005-hybris-Sustainability-1.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"social & environmental accountability"}},{"title":"MEC ambassadors","uetTitle":"MEC ambassadors","url":"/en/ambassadors","image":"https://cdn.mec.ca/medias/sys_master/images/images/h46/hd3/9207978885150/Ambassador-HeroImage-1-.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"mec ambassadors"}},{"title":"Bike service","uetTitle":"Bike service","url":"/en/explore/bike-service","image":"https://cdn.mec.ca/medias/sys_master/images/images/h6b/h6e/9019174551582/16-IT-0005-hybris-BikeShop.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"bike service"}},{"title":"Ski service","uetTitle":"Ski service","url":"/en/explore/ski-shop","image":"https://cdn.mec.ca/medias/sys_master/images/images/h81/h44/9019174748190/16-IT-0005-hybris-SkiShop.jpg","skipSubNav":false,"features":{"horizontal":[],"vertical":[]},"subnav":[],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level2","action":"about us","label":"ski service"}}],"groups":[],"mecUetData":{"category":"uet-mega-menu-v2-level1","action":"about us","label":""}}],"groups":[]}

    MEC.outage = {"timeToOutageStartMinutes":-1,"timeToOutageEndMinutes":-1,"status":"NO_OUTAGE","inOutage":false};


    /*]]>*/
</script>
<script type="text/javascript">
	/*<![CDATA[*/
	ACC.addons = {};	//JS holder for addons properties


		ACC.addons.meccheckoutaddon = [];

				ACC.addons.meccheckoutaddon['key.2'] = 'value 2';

				ACC.addons.meccheckoutaddon['key.1'] = 'value 1';

		ACC.addons.smarteditaddon = [];

		ACC.addons.assistedservicestorefront = [];

				ACC.addons.assistedservicestorefront['asm.timer.min'] = 'min';

	/*]]>*/
</script>


<!-- This variable rrparms is declared in javaScriptVariables.tag (master.tag) read comment there -->
<script>
	MEC.data.rrparms = {"eventType":"productLayoutPage","apiKey":"1eaaaefab7262d51","rrServer":"cdn","region":"en","userId":"","sessionId":"Y101802120-1a32aa8b-52a2-4bd5-a658-7ad044874c50","placementType":["item_page.product1_rr","item_page.product2_rr","item_page.product3_rr"],"itemId":"5050-315","itemName":"Patagonia Quandary Pants - Women's","categoryId":"1008","cartValue":0};
</script><script src="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/js/vendors.js"></script>

<script src="https://do9m2ht361ti1.cloudfront.net/_ui/static/react-16.13.1.js"></script>
        <script src="https://do9m2ht361ti1.cloudfront.net/_ui/static/react-dom-16.13.1.js"></script>
    <script src="https://cdn.mec.ca/en/translations"></script>

<script src="https://do9m2ht361ti1.cloudfront.net/_ui/build-741/responsive/js/core.js"></script>


<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"errorBeacon":"bam-cell.nr-data.net","licenseKey":"5dfbfbeddb","agent":"","beacon":"bam-cell.nr-data.net","applicationTime":292,"applicationID":"25572410","transactionName":"ZVxWbUdRWkRSVE1ZX1wWZ0lHWVpQcFhXREJdVVhcRx9kRVxTTFNEYlhTXHZfWkNBWFVcVUAWREtaVEFUR3NcRFFbVQ==","queueTime":0}</script></body>
</html>
'''