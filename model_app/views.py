from django.shortcuts import render
from .controllers import pred

def calculate(request):
    if request.method == 'POST':
        income = int(request.POST['income'])
        num_family = int(request.POST['num_family'])
        num_kids = int(request.POST['num_kids'])

        pred_res = pred([income/1000, num_family, num_kids], income/1000)

        calculations = [
            f"{'Kesehatan'}: Rp {pred_res['Kesehatan']}",
            f"{'Pendidikan'}: Rp {pred_res['Pendidikan']}",
            f"{'Pangan'}: Rp {pred_res['Pangan']}",
            f"{'Tabungan'}: Rp {pred_res['Saving']}",
            f"{'Keinginan'}: Rp {pred_res['Wants']}",
            f"{'Operational'}: Rp {pred_res['Operational']}",
            f"{'Fixed Expenses'}: Rp {pred_res['Fixed']}",
        ]
        return render(request, 'home.html', {'calculations': calculations})
    return render(request, 'home.html')