from django.shortcuts import render
from .controllers import pred

def calculate(request):
    if request.method == 'POST':
        income = request.POST['name']
        num_family = int(request.POST['num_family'])
        num_kids = int(request.POST['num_kids'])
        
        pred_res = pred([income, num_family, num_kids])

        
        calculations = [
            f"Hello!, here's your budget recommendation",
            f"{'Kesehatan'}: Rp{pred_res[0]}",
            f"{'Pendidikan'}: Rp{pred_res[1]}",
            f"{'Pangan'}: Rp{pred_res[2]}",
            f"{'Tabungan'}: Rp{pred_res[3]}",
            f"{'Keinginan'}: Rp{pred_res[4]}",
            f"{'Operational'}: Rp{pred_res[5]}",
            f"{'Fixed Expenses'}: Rp{pred_res[6]}",
        ]
        return render(request, 'home.html', {'calculations': calculations})
    return render(request, 'home.html')