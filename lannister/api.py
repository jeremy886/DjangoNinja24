from ninja import Router

router = Router()


@router.get("/home")
def home(request):
    return "A Lannister always pays their debts"


@router.get("/rock/{int:height}")
def rock(request, height: int):
    return f"Casterly Rock is {height + 1}m tall"
