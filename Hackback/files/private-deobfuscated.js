'use strict';
/** @type {!Array} */
var a = ["WxIjwr7DusO8GsKvRwB+wq3DuMKrwrLDgcOiwrY1KEEgG8KCwq7Dl8K3", "AcOMwqvDqQgCw4/Ct2nDtMKhZcKDwqTCpTsyw7nChsOQXMO5W8KpDsOtNCDDvAjCgyk=", "w5HDr8O7dDRmMMKJw4jDlVRnwrt7w7s0wo1aw7sAQsKsfsOEw4XDsRjClMOwFzrCmzpvCAjCuBzDssK9F8O4wqZnWsKh"];
(function(params, i) {
  /**
   * @param {number} isLE
   * @return {undefined}
   */
  var write = function(isLE) {
    for (; --isLE;) {
      params["push"](params["shift"]());
    }
  };
  write(++i);
})(a, 102);
/**
 * @param {string} i
 * @param {string} a
 * @return {?}
 */
var b = function(i, a) {
  /** @type {number} */
  i = i - 0;
  var key = a[i];
  if (b["MsULmv"] === undefined) {
    (function() {
      var PL$14;
      try {
        var evaluate = Function("return (function() " + '{}.constructor("return this")( )' + ");");
        PL$14 = evaluate();
      } catch (h) {
        /** @type {!Window} */
        PL$14 = window;
      }
      /** @type {string} */
      var colorProps = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
      if (!PL$14["atob"]) {
        /**
         * @param {?} Y
         * @return {?}
         */
        PL$14["atob"] = function(Y) {
          var str = String(Y)["replace"](/=+$/, "");
          /** @type {number} */
          var i = 0;
          var y;
          var x;
          /** @type {number} */
          var n = 0;
          /** @type {string} */
          var pix_color = "";
          for (; x = str["charAt"](n++); ~x && (y = i % 4 ? y * 64 + x : x, i++ % 4) ? pix_color = pix_color + String["fromCharCode"](255 & y >> (-2 * i & 6)) : 0) {
            x = colorProps["indexOf"](x);
          }
          return pix_color;
        };
      }
    })();
    /**
     * @param {string} data
     * @param {!Object} fn
     * @return {?}
     */
    var testcase = function(data, fn) {
      /** @type {!Array} */
      var p = [];
      /** @type {number} */
      var u = 0;
      var b;
      /** @type {string} */
      var testResult = "";
      /** @type {string} */
      var tempData = "";
      /** @type {string} */
      data = atob(data);
      /** @type {number} */
      var val = 0;
      var key = data["length"];
      for (; val < key; val++) {
        /** @type {string} */
        tempData = tempData + ("%" + ("00" + data["charCodeAt"](val)["toString"](16))["slice"](-2));
      }
      /** @type {string} */
      data = decodeURIComponent(tempData);
      /** @type {number} */
      var i = 0;
      for (; i < 256; i++) {
        /** @type {number} */
        p[i] = i;
      }
      i = 0;
      for (; i < 256; i++) {
        /** @type {number} */
        u = (u + p[i] + fn["charCodeAt"](i % fn["length"])) % 256;
        b = p[i];
        p[i] = p[u];
        p[u] = b;
      }
      i = 0;
      u = 0;
      var PL$19 = 0;

      for (; PL$19 < data["length"]; PL$19++) {
        i = (i + 1) % 256;
        u = (u + p[i]) % 256;
        b = p[i];
        p[i] = p[u];
        p[u] = b;
        testResult = testResult + String["fromCharCode"](data["charCodeAt"](PL$19) ^ p[(p[i] + p[u]) % 256]);
      }
      return testResult;
    };
    /** @type {function(string, !Object): ?} */
    b["OoACcd"] = testcase;
    b["qSLwGk"] = {};
    /** @type {boolean} */
    b["MsULmv"] = !![];
  }
  var C = b["qSLwGk"][i];
  if (C === undefined) {
    if (b["pIjlQB"] === undefined) {
      /** @type {boolean} */
      b["pIjlQB"] = !![];
    }
    key = b["OoACcd"](key, a);
    b["qSLwGk"][i] = key;
  } else {
    key = C;
  }
  return key;
};

var x = "Secure Login Bypass";
var z = b("0x0", "P]S6");
var h = b("0x1", "r7TY");
var y = b("0x2", "DAqg");
var t = "?action=(show,list,exec,init)";
var s = "&site=(twitter,paypal,facebook,hackthebox)";
var i = "&password=********";
var k = "&session=";
var w = "Nothing more to say";
