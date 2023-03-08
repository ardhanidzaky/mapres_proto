import catboost as cb
from composition_stats import clr, clr_inv

PRED_COL = ['kesehatan', 'pendidikan', 'pangan', 'saving', 'wants', 'operational', 'fixed']

def pred(to_pred, income):
    preds = []

    for col in PRED_COL:
        model = cb.CatBoostRegressor()
        model.load_model('ml_models/{}_model.cbm'.format(col))

        pred_single = model.predict(to_pred)
        preds.append(pred_single)

    res = clr_inv(preds)
    index = 0

    res_bgt = {}
    for col in PRED_COL:
        res_bgt['{}'.format(col.capitalize())] = '{:.0f}'.format(res[index]*income*1000)
        
        index += 1

    return res_bgt