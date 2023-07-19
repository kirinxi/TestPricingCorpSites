from dataclasses import dataclass

#pricelist Global
#@dataclass
class StandardPriceList:
    standard_1d1y: str = '$37.99'
    standard_1d1y_renewal: str = '$47.99'
    standard_3d1y: str = '$44.99'
    standard_3d1y_renewal: str = '$56.99'
    standard_5d1y: str = '$51.99'
    standard_5d1y_renewal: str = '$65.99'
    standard_1d2y: str = '$75.99'
    standard_1d2y_renewal: str = '$95.98'
    standard_1d2y_renewal_disclaimer: str = '$47.99'
    standard_3d2y: str = '$90.99'
    standard_3d2y_renewal: str = '$113.98'
    standard_3d2y_renewal_disclaimer: str = '$56.99'
    standard_5d2y: str = '$104.99'
    standard_5d2y_renewal: str = '$131.98'
    standard_5d2y_renewal_disclaimer: str = '$65.99'

@dataclass
class PlusPriceList:
    plus_1d1y: str = '$45.99'
    plus_1d1y_renewal: str = '$57.99'
    plus_3d1y: str = '$52.99'
    plus_3d1y_renewal: str = '$66.99'
    plus_5d1y: str = '$59.99'
    plus_5d1y_renewal: str = '$75.99'
    plus_1d2y: str = '$91.99'
    plus_1d2y_renewal: str = '$115.98'
    plus_1d2y_renewal_disclaimer: str = '$57.99'
    plus_3d2y: str = '$106.99'
    plus_3d2y_renewal: str = '$133.98'
    plus_3d2y_renewal_disclaimer: str = '$66.99'
    plus_5d2y: str = '$120.99'
    plus_5d2y_renewal: str = '$151.98'
    plus_5d2y_renewal_disclaimer: str = '$75.99'

@dataclass
class PremiumPriceList:
    premium_1d1y: str = '$46.99'
    premium_1d1y_renewal: str = '$59.99'
    premium_3d1y: str = '$54.99'
    premium_3d1y_renewal: str = '$68.99'
    premium_5d1y: str = '$61.99'
    premium_5d1y_renewal: str = '$77.99'
    premium_10d1y: str = '$78.99'
    premium_10d1y_renewal: str = '$99.98'
    premium_1d2y: str = '$94.99'
    premium_1d2y_renewal: str = '$119.98'
    premium_1d2y_renewal_disclaimer: str = '$59.99'
    premium_3d2y: str = '$109.99'
    premium_3d2y_renewal: str = '$137.98'
    premium_3d2y_renewal_disclaimer: str = '$68.99'
    premium_5d2y: str = '$123.99'
    premium_5d2y_renewal: str = '$155.98'
    premium_5d2y_renewal_disclaimer: str = '$77.99'
    premium_10d2y: str = '$158.99'
    premium_10d2y_renewal: str = '$199.98'
    premium_10d2y_renewal_disclaimer: str = '$99.99'




