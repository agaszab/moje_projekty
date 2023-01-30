import random


def init():
    board = {}
    for i in range(1, 10):
        board[i] = '_'
    return board


def display_board(board):
    ### Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
    ### i wyświetla go w oknie konsoli.
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")


def enter_move(board, mozliwosci):
    ### Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
    ### prosi użytkownika o wykonanie ruchu,
    ### sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
    print(
        "Podaj gdzie wstawić znak wg współrzędnych: \n | I-y rząd: 1,2,3 |\n | II-i rząd: 4,5,6 |\n | III-i rząd: 7,8,9 |")
    print("Wolne pola:", mozliwosci)
    print("")
    ruch = 1
    try:
        ruch = int(input("Po podaniu pola wcisnij enter."))
    except:
        print("Podałeś złą wartość")
        ruch = 0

    if ruch in board.keys():
        if board[ruch] == '_':
            board[ruch] = 'x'
        else:
            print("To pole jest już zajęte")
            ruch = 0
    else:
        print("Nieprawidłowy parametr")
        ruch = 0

    return ruch


def make_list_of_free_fields(board):
    ### Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól;
    ### lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
    mozliwosci = []
    for klucz, wartosc in board.items():
        if wartosc == "_":
            mozliwosci.append(klucz)
    return mozliwosci


def victory_for(board, sing):
    ### Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
    ### czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.

    if (board[1] == sing and board[2] == sing and board[3] == sing) or (
            board[4] == sing and board[5] == sing and board[6] == sing) or (
            board[7] == sing and board[8] == sing and board[9] == sing):
        if sing == "x":
            print("You winn!")
        else:
            print("Computer wins")
        return False

    if (board[1] == sing and board[4] == sing and board[7] == sing) or (
            board[2] == sing and board[5] == sing and board[8] == sing) or (
            board[3] == sing and board[6] == sing and board[9] == sing):
        if sing == "x":
            print("You winn!")
        else:
            print("Computer wins")
        return False

    if (board[1] == sing and board[5] == sing and board[9] == sing) or (
            board[3] == sing and board[5] == sing and board[7] == sing):
        if sing == "x":
            print("You winn!")
        else:
            print("Computer wins")
        return False
    return True


def draw_move(board, mozliwosci):
    ### Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
    a = random.choice(mozliwosci)
    if a in board.keys():
        if board[a] == '_':
            board[a] = '0'
    return board


board = init()
display_board(board)
gra = True
while gra:
    mozliwosci = make_list_of_free_fields(board)
    ruch = enter_move(board, mozliwosci)
    gra = victory_for(board, "x")
    if gra == False:
        break
    if ruch == 0:
        continue
    mozliwosci = make_list_of_free_fields(board)
    draw_move(board, mozliwosci)
    gra = victory_for(board, "0")
    display_board(board)
    if gra == False:
        break
