from django.db import models

# Create your models here.

class HistoryDataETH(models.Model):
    # Raw data columns
    # some comments
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(unique=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close= models.FloatField()
    volume = models.FloatField()
    close_time = models.BigIntegerField()
    quote_asset_volume = models.FloatField()
    num_trades = models.PositiveIntegerField()

    # Derived columns

    hour_sin = models.FloatField(null=True)
    hour_cos = models.FloatField(null=True)
    day_sin = models.FloatField(null=True)
    day_cos = models.FloatField(null=True)
    mon_sin = models.FloatField(null=True)
    mon_cos = models.FloatField(null=True)
    weekday_sin = models.FloatField(null=True)
    weekday_cos = models.FloatField(null=True)
    year = models.PositiveIntegerField(null=True) # !!! IntegerField
    RATIO_close_and_MA3 = models.FloatField(null=True)
    RATIO_close_and_MA6 = models.FloatField(null=True)
    RATIO_close_and_MA12 = models.FloatField(null=True)
    RATIO_close_and_MA24 = models.FloatField(null=True)
    RATIO_close_and_MA48 = models.FloatField(null=True)
    RATIO_close_and_MA96 = models.FloatField(null=True)
    RATIO_close_and_MA192 = models.FloatField(null=True)
    RATIO_close_and_MA384 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA3 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA6 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA12 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA24 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA48 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA96 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA192 = models.FloatField(null=True)
    RATIO_quote_asset_volume_and_MA384 = models.FloatField(null=True)
    RATIO_num_trades_and_MA3 = models.FloatField(null=True)
    RATIO_num_trades_and_MA6 = models.FloatField(null=True)
    RATIO_num_trades_and_MA12 = models.FloatField(null=True)
    RATIO_num_trades_and_MA24 = models.FloatField(null=True)
    RATIO_num_trades_and_MA48 = models.FloatField(null=True)
    RATIO_num_trades_and_MA96 = models.FloatField(null=True)
    RATIO_num_trades_and_MA192 = models.FloatField(null=True)
    RATIO_num_trades_and_MA384 = models.FloatField(null=True)
    RATIO_close_and_STD3 = models.FloatField(null=True)
    RATIO_close_and_STD6 = models.FloatField(null=True)
    RATIO_close_and_STD12 = models.FloatField(null=True)
    RATIO_close_and_STD24 = models.FloatField(null=True)
    RATIO_close_and_STD48 = models.FloatField(null=True)
    RATIO_close_and_STD96 = models.FloatField(null=True)
    RATIO_close_and_STD192 = models.FloatField(null=True)
    RATIO_close_and_STD384 = models.FloatField(null=True)
    RSI_3_close = models.FloatField(null=True)
    RSI_6_close = models.FloatField(null=True)
    RSI_12_close = models.FloatField(null=True)
    RSI_24_close = models.FloatField(null=True)
    RSI_48_close = models.FloatField(null=True)
    RSI_96_close = models.FloatField(null=True)
    RSI_192_close = models.FloatField(null=True)
    RSI_384_close = models.FloatField(null=True)
    predicted = models.TextField(max_length=2, null=True)


    