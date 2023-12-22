from django.http import HttpResponse

from ninja import Router

router = Router()


@router.get('/ruler')
def ruler(request, gender):
    if gender == "m":
        return "Hello Khal"

    return "Hello Khaleesi"


@router.get('/horses')
def horses(request, num: int):
    horses = ["horses" for _ in range(num)]
    return "\n".join(horses)


@router.get('/food/{item}')
def food(request, item: str):
    return f"I love {item}"


@router.get('/drank/{int:count}')
def drank(request, count: int):
    return f"I drank {count} cups of fermented horse milk"


@router.get('/swords')
def swords(request, response: HttpResponse):
    response.set_cookie("curve", "bendy")
    return f"Swords are pointy"
