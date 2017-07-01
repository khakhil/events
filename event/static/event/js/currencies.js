var Currency = {
  rates: {"USD":1.0,"EUR":1.11006,"GBP":1.42803,"CAD":0.753364,"ARS":0.0674036,"AUD":0.751815,"BRL":0.273238,"CLP":0.00146972,"CNY":0.153836,"CYP":0.397899,"CZK":0.0410504,"DKK":0.148841,"EEK":0.0709459,"HKD":0.128892,"HUF":0.0035809,"ISK":0.00792079,"INR":0.0148853,"JMD":0.00823384,"JPY":0.00878427,"LVL":1.57949,"LTL":0.321497,"MTL":0.293496,"MXN":0.0563357,"NZD":0.668297,"NOK":0.117974,"PLN":0.259443,"SGD":0.726536,"SKK":21.5517,"SIT":175.439,"ZAR":0.0643608,"KRW":0.000841915,"SEK":0.119787,"CHF":1.01303,"TWD":0.0304178,"UYU":0.0314465,"MYR":0.243843,"BSD":1.0,"CRC":0.00189007,"RON":0.248458,"PHP":0.0214823,"AED":0.272257,"VEB":0.000159129,"IDR":7.65314e-05,"TRY":0.348255,"THB":0.0285225,"TTD":0.153257,"ILS":0.25693,"SYP":0.00529616,"XCD":0.37037,"COP":0.000313696,"RUB":0.0142964,"HRK":0.146771,"KZT":0.00291426,"TZS":0.000458295,"XPT":960.292,"SAR":0.266695,"NIO":0.0352113,"LAK":0.000123762,"OMR":2.5974,"AMD":0.00204474,"CDF":0.0010917,"KPW":0.00786073,"SPL":6.0,"KES":0.00986388,"ZWD":0.00276319,"KHR":0.000251256,"MVR":0.0664452,"GTQ":0.129525,"BZD":0.50505,"BYR":4.84262e-05,"LYD":0.725426,"DZD":0.0091191,"BIF":0.000650407,"GIP":1.42803,"BOB":0.147275,"XOF":0.00169228,"STD":4.53823e-05,"NGN":0.00502513,"PGK":0.326664,"ERN":0.095511,"MWK":0.00144227,"CUP":0.0377358,"GMD":0.025582,"CVE":0.0100908,"BTN":0.0148853,"XAF":0.00169228,"UGX":0.000298329,"MAD":0.10234,"MNT":0.000489716,"LSL":0.0643608,"XAG":15.3854,"TOP":0.4352,"SHP":1.42803,"RSD":0.00907275,"HTG":0.0162338,"MGA":0.000314961,"MZN":0.0198216,"FKP":1.42803,"BWP":0.0876,"HNL":0.0444444,"PYG":0.000175285,"JEP":1.42803,"EGP":0.111734,"LBP":0.000664275,"ANG":0.564972,"WST":0.3775,"TVD":0.751815,"GYD":0.00488878,"GGP":1.42803,"NPR":0.0093633,"KMF":0.00225638,"IRR":3.31455e-05,"XPD":569.343,"SRD":0.252525,"TMM":5.71429e-05,"SZL":0.0643608,"MOP":0.125137,"BMD":1.0,"XPF":0.00930234,"ETB":0.0467181,"JOD":1.41303,"MDL":0.050813,"MRO":0.0032,"YER":0.00465549,"BAM":0.567567,"AWG":0.558659,"PEN":0.298196,"VEF":0.159129,"SLL":0.000249252,"KYD":1.24538,"AOA":0.00632291,"TND":0.495417,"TJS":0.127079,"SCR":0.0749906,"LKR":0.0068956,"DJF":0.00565611,"GNF":0.000132802,"VUV":0.00946074,"SDG":0.164745,"IMP":1.42803,"GEL":0.41232,"FJD":0.478698,"DOP":0.0221828,"XDR":1.3955,"MUR":0.0281928,"MMK":0.00082713,"LRD":0.011812,"BBD":0.5,"ZMK":8.78735e-05,"XAU":1236.66,"VND":4.48632e-05,"UAH":0.0378788,"TMT":0.285714,"IQD":0.00090386,"BGN":0.567665,"KGS":0.0138496,"RWF":0.00130716,"BHD":2.65252,"UZS":0.00034965,"PKR":0.00956023,"MKD":0.0181587,"AFN":0.014652,"NAD":0.0643608,"BDT":0.0127714,"AZN":0.609533,"SOS":0.00163132,"QAR":0.274635,"PAB":1.0,"CUC":1.0,"SVC":0.114286,"SBD":0.1263,"ALL":0.0080782,"BND":0.726536,"KWD":3.32557,"GHS":0.259774,"ZMW":0.0878735,"XBT":415.2,"NTD":0.0337206},
  convert: function(amount, from, to) {
    return (amount * this.rates[from]) / this.rates[to];
  }
};
