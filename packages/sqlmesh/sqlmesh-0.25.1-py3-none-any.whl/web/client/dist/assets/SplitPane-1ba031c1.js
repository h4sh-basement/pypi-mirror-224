import{aj as xe,R as se,j as Ee}from"./index-ba4e7745.js";var le={exports:{}},De="SECRET_DO_NOT_PASS_THIS_OR_YOU_WILL_BE_FIRED",Te=De,Ae=Te;function ce(){}function fe(){}fe.resetWarningCache=ce;var _e=function(){function i(s,u,v,p,g,l){if(l!==Ae){var h=new Error("Calling PropTypes validators directly is not supported by the `prop-types` package. Use PropTypes.checkPropTypes() to call them. Read more at http://fb.me/use-check-prop-types");throw h.name="Invariant Violation",h}}i.isRequired=i;function n(){return i}var o={array:i,bigint:i,bool:i,func:i,number:i,object:i,string:i,symbol:i,any:i,arrayOf:n,element:i,elementType:i,instanceOf:n,node:i,objectOf:n,oneOf:n,oneOfType:n,shape:n,exact:n,checkPropTypes:fe,resetWarningCache:ce};return o.PropTypes=o,o};le.exports=_e();var we=le.exports;const c=xe(we);var b=typeof window<"u"?window:null,K=b===null,G=K?void 0:b.document,x="addEventListener",E="removeEventListener",Z="getBoundingClientRect",N="_a",D="_b",_="_c",H="horizontal",T=function(){return!1},Me=K?"calc":["","-webkit-","-moz-","-o-"].filter(function(i){var n=G.createElement("div");return n.style.cssText="width:"+i+"calc(9px)",!!n.style.length}).shift()+"calc",pe=function(i){return typeof i=="string"||i instanceof String},oe=function(i){if(pe(i)){var n=G.querySelector(i);if(!n)throw new Error("Selector "+i+" did not match a DOM element");return n}return i},m=function(i,n,o){var s=i[n];return s!==void 0?s:o},q=function(i,n,o,s){if(n){if(s==="end")return 0;if(s==="center")return i/2}else if(o){if(s==="start")return 0;if(s==="center")return i/2}return i},Re=function(i,n){var o=G.createElement("div");return o.className="gutter gutter-"+n,o},Pe=function(i,n,o){var s={};return pe(n)?s[i]=n:s[i]=Me+"("+n+"% - "+o+"px)",s},je=function(i,n){var o;return o={},o[i]=n+"px",o},ue=function(i,n){if(n===void 0&&(n={}),K)return{};var o=i,s,u,v,p,g,l;Array.from&&(o=Array.from(o));var h=oe(o[0]),A=h.parentNode,w=getComputedStyle?getComputedStyle(A):null,L=w?w.flexDirection:null,U=m(n,"sizes")||o.map(function(){return 100/o.length}),F=m(n,"minSize",100),O=Array.isArray(F)?F:o.map(function(){return F}),M=m(n,"maxSize",1/0),W=Array.isArray(M)?M:o.map(function(){return M}),y=m(n,"expandToMin",!1),z=m(n,"gutterSize",10),j=m(n,"gutterAlign","center"),Y=m(n,"snapOffset",30),de=Array.isArray(Y)?Y:o.map(function(){return Y}),V=m(n,"dragInterval",1),I=m(n,"direction",H),X=m(n,"cursor",I===H?"col-resize":"row-resize"),ve=m(n,"gutter",Re),ee=m(n,"elementStyle",Pe),me=m(n,"gutterStyle",je);I===H?(s="width",u="clientX",v="left",p="right",g="clientWidth"):I==="vertical"&&(s="height",u="clientY",v="top",p="bottom",g="clientHeight");function C(r,e,t,a){var d=ee(s,e,t,a);Object.keys(d).forEach(function(f){r.style[f]=d[f]})}function ge(r,e,t){var a=me(s,e,t);Object.keys(a).forEach(function(d){r.style[d]=a[d]})}function $(){return l.map(function(r){return r.size})}function te(r){return"touches"in r?r.touches[0][u]:r[u]}function re(r){var e=l[this.a],t=l[this.b],a=e.size+t.size;e.size=r/this.size*a,t.size=a-r/this.size*a,C(e.element,e.size,this[D],e.i),C(t.element,t.size,this[_],t.i)}function ye(r){var e,t=l[this.a],a=l[this.b];this.dragging&&(e=te(r)-this.start+(this[D]-this.dragOffset),V>1&&(e=Math.round(e/V)*V),e<=t.minSize+t.snapOffset+this[D]?e=t.minSize+this[D]:e>=this.size-(a.minSize+a.snapOffset+this[_])&&(e=this.size-(a.minSize+this[_])),e>=t.maxSize-t.snapOffset+this[D]?e=t.maxSize+this[D]:e<=this.size-(a.maxSize-a.snapOffset+this[_])&&(e=this.size-(a.maxSize+this[_])),re.call(this,e),m(n,"onDrag",T)($()))}function ne(){var r=l[this.a].element,e=l[this.b].element,t=r[Z](),a=e[Z]();this.size=t[s]+a[s]+this[D]+this[_],this.start=t[v],this.end=t[p]}function Se(r){if(!getComputedStyle)return null;var e=getComputedStyle(r);if(!e)return null;var t=r[g];return t===0?null:(I===H?t-=parseFloat(e.paddingLeft)+parseFloat(e.paddingRight):t-=parseFloat(e.paddingTop)+parseFloat(e.paddingBottom),t)}function ie(r){var e=Se(A);if(e===null||O.reduce(function(f,S){return f+S},0)>e)return r;var t=0,a=[],d=r.map(function(f,S){var P=e*f/100,k=q(z,S===0,S===r.length-1,j),B=O[S]+k;return P<B?(t+=B-P,a.push(0),B):(a.push(P-B),P)});return t===0?r:d.map(function(f,S){var P=f;if(t>0&&a[S]-t>0){var k=Math.min(t,a[S]-t);t-=k,P=f-k}return P/e*100})}function he(){var r=this,e=l[r.a].element,t=l[r.b].element;r.dragging&&m(n,"onDragEnd",T)($()),r.dragging=!1,b[E]("mouseup",r.stop),b[E]("touchend",r.stop),b[E]("touchcancel",r.stop),b[E]("mousemove",r.move),b[E]("touchmove",r.move),r.stop=null,r.move=null,e[E]("selectstart",T),e[E]("dragstart",T),t[E]("selectstart",T),t[E]("dragstart",T),e.style.userSelect="",e.style.webkitUserSelect="",e.style.MozUserSelect="",e.style.pointerEvents="",t.style.userSelect="",t.style.webkitUserSelect="",t.style.MozUserSelect="",t.style.pointerEvents="",r.gutter.style.cursor="",r.parent.style.cursor="",G.body.style.cursor=""}function ze(r){if(!("button"in r&&r.button!==0)){var e=this,t=l[e.a].element,a=l[e.b].element;e.dragging||m(n,"onDragStart",T)($()),r.preventDefault(),e.dragging=!0,e.move=ye.bind(e),e.stop=he.bind(e),b[x]("mouseup",e.stop),b[x]("touchend",e.stop),b[x]("touchcancel",e.stop),b[x]("mousemove",e.move),b[x]("touchmove",e.move),t[x]("selectstart",T),t[x]("dragstart",T),a[x]("selectstart",T),a[x]("dragstart",T),t.style.userSelect="none",t.style.webkitUserSelect="none",t.style.MozUserSelect="none",t.style.pointerEvents="none",a.style.userSelect="none",a.style.webkitUserSelect="none",a.style.MozUserSelect="none",a.style.pointerEvents="none",e.gutter.style.cursor=X,e.parent.style.cursor=X,G.body.style.cursor=X,ne.call(e),e.dragOffset=te(r)-e.end}}U=ie(U);var R=[];l=o.map(function(r,e){var t={element:oe(r),size:U[e],minSize:O[e],maxSize:W[e],snapOffset:de[e],i:e},a;if(e>0&&(a={a:e-1,b:e,dragging:!1,direction:I,parent:A},a[D]=q(z,e-1===0,!1,j),a[_]=q(z,!1,e===o.length-1,j),L==="row-reverse"||L==="column-reverse")){var d=a.a;a.a=a.b,a.b=d}if(e>0){var f=ve(e,I,t.element);ge(f,z,e),a[N]=ze.bind(a),f[x]("mousedown",a[N]),f[x]("touchstart",a[N]),A.insertBefore(f,t.element),a.gutter=f}return C(t.element,t.size,q(z,e===0,e===o.length-1,j),e),e>0&&R.push(a),t});function ae(r){var e=r.i===R.length,t=e?R[r.i-1]:R[r.i];ne.call(t);var a=e?t.size-r.minSize-t[_]:r.minSize+t[D];re.call(t,a)}l.forEach(function(r){var e=r.element[Z]()[s];e<r.minSize&&(y?ae(r):r.minSize=e)});function be(r){var e=ie(r);e.forEach(function(t,a){if(a>0){var d=R[a-1],f=l[d.a],S=l[d.b];f.size=e[a-1],S.size=t,C(f.element,f.size,d[D],f.i),C(S.element,S.size,d[_],S.i)}})}function Oe(r,e){R.forEach(function(t){if(e!==!0?t.parent.removeChild(t.gutter):(t.gutter[E]("mousedown",t[N]),t.gutter[E]("touchstart",t[N])),r!==!0){var a=ee(s,t.a.size,t[D]);Object.keys(a).forEach(function(d){l[t.a].element.style[d]="",l[t.b].element.style[d]=""})}})}return{setSizes:be,getSizes:$,collapse:function(e){ae(l[e])},destroy:Oe,parent:A,pairs:R}};function J(i,n){var o={};for(var s in i)Object.prototype.hasOwnProperty.call(i,s)&&n.indexOf(s)===-1&&(o[s]=i[s]);return o}var Q=function(i){function n(){i.apply(this,arguments)}return i&&(n.__proto__=i),n.prototype=Object.create(i&&i.prototype),n.prototype.constructor=n,n.prototype.componentDidMount=function(){var s=this.props;s.children;var u=s.gutter,v=J(s,["children","gutter"]),p=v;p.gutter=function(g,l){var h;return u?h=u(g,l):(h=document.createElement("div"),h.className="gutter gutter-"+l),h.__isSplitGutter=!0,h},this.split=ue(this.parent.children,p)},n.prototype.componentDidUpdate=function(s){var u=this,v=this.props;v.children;var p=v.minSize,g=v.sizes,l=v.collapsed,h=J(v,["children","minSize","sizes","collapsed"]),A=h,w=s.minSize,L=s.sizes,U=s.collapsed,F=["maxSize","expandToMin","gutterSize","gutterAlign","snapOffset","dragInterval","direction","cursor"],O=F.map(function(y){return u.props[y]!==s[y]}).reduce(function(y,z){return y||z},!1);if(Array.isArray(p)&&Array.isArray(w)){var M=!1;p.forEach(function(y,z){M=M||y!==w[z]}),O=O||M}else Array.isArray(p)||Array.isArray(w)?O=!0:O=O||p!==w;if(O)A.minSize=p,A.sizes=g||this.split.getSizes(),this.split.destroy(!0,!0),A.gutter=function(y,z,j){return j.previousSibling},this.split=ue(Array.from(this.parent.children).filter(function(y){return!y.__isSplitGutter}),A);else if(g){var W=!1;g.forEach(function(y,z){W=W||y!==L[z]}),W&&this.split.setSizes(this.props.sizes)}Number.isInteger(l)&&(l!==U||O)&&this.split.collapse(l)},n.prototype.componentWillUnmount=function(){this.split.destroy(),delete this.split},n.prototype.render=function(){var s=this,u=this.props;u.sizes,u.minSize,u.maxSize,u.expandToMin,u.gutterSize,u.gutterAlign,u.snapOffset,u.dragInterval,u.direction,u.cursor,u.gutter,u.elementStyle,u.gutterStyle,u.onDrag,u.onDragStart,u.onDragEnd,u.collapsed;var v=u.children,p=J(u,["sizes","minSize","maxSize","expandToMin","gutterSize","gutterAlign","snapOffset","dragInterval","direction","cursor","gutter","elementStyle","gutterStyle","onDrag","onDragStart","onDragEnd","collapsed","children"]),g=p;return se.createElement("div",Object.assign({},{ref:function(l){s.parent=l}},g),v)},n}(se.Component);Q.propTypes={sizes:c.arrayOf(c.number),minSize:c.oneOfType([c.number,c.arrayOf(c.number)]),maxSize:c.oneOfType([c.number,c.arrayOf(c.number)]),expandToMin:c.bool,gutterSize:c.number,gutterAlign:c.string,snapOffset:c.oneOfType([c.number,c.arrayOf(c.number)]),dragInterval:c.number,direction:c.string,cursor:c.string,gutter:c.func,elementStyle:c.func,gutterStyle:c.func,onDrag:c.func,onDragStart:c.func,onDragEnd:c.func,collapsed:c.number,children:c.arrayOf(c.element)};Q.defaultProps={sizes:void 0,minSize:void 0,maxSize:void 0,expandToMin:void 0,gutterSize:void 0,gutterAlign:void 0,snapOffset:void 0,dragInterval:void 0,direction:void 0,cursor:void 0,gutter:void 0,elementStyle:void 0,gutterStyle:void 0,onDrag:void 0,onDragStart:void 0,onDragEnd:void 0,collapsed:void 0,children:void 0};const Ie=Q;function Fe({className:i,children:n,sizes:o,minSize:s,maxSize:u,direction:v,expandToMin:p,snapOffset:g}){return Ee.jsx(Ie,{className:i,sizes:o,expandToMin:p,gutterAlign:"center",gutterSize:3,direction:v,minSize:s,maxSize:u,snapOffset:g,children:n})}export{Fe as S};
