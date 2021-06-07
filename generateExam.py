import qrcode as qr
import os
from PIL import Image
from fpdf import FPDF
import openpyxl as opxl

r = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def SwitchFrThreeChoices(argument):
    switcher = {
        5: "./model/fr/5x3.png",
        6: "./model/fr/6x3.png",
        7: "./model/fr/7x3.png",
        8: "./model/fr/8x3.png",
        9: "./model/fr/9x3.png",
        10: "./model/fr/10x3.png",
        11: "./model/fr/11x3.png",
        12: "./model/fr/12x3.png",
        13: "./model/fr/13x3.png",
        14: "./model/fr/14x3.png",
        15: "./model/fr/15x3.png",
        16: "./model/fr/16x3.png",
        17: "./model/fr/17x3.png",
        18: "./model/fr/18x3.png",
        19: "./model/fr/19x3.png",
        20: "./model/fr/20x3.png",
    }
    return switcher.get(argument)


def SwitchFrFourChoices(argument):
    switcher = {
        5: "./model/fr/5x4.png",
        6: "./model/fr/6x4.png",
        7: "./model/fr/7x4.png",
        8: "./model/fr/8x4.png",
        9: "./model/fr/9x4.png",
        10: "./model/fr/10x4.png",
        11: "./model/fr/11x4.png",
        12: "./model/fr/12x4.png",
        13: "./model/fr/13x4.png",
        14: "./model/fr/14x4.png",
        15: "./model/fr/15x4.png",
        16: "./model/fr/16x4.png",
        17: "./model/fr/17x4.png",
        18: "./model/fr/18x4.png",
        19: "./model/fr/19x4.png",
        20: "./model/fr/20x4.png",
    }
    return switcher.get(argument, "nothing")


def SwitchFrFiveChoices(argument):
    switcher = {
        5: "./model/fr/5x5.png",
        6: "./model/fr/6x5.png",
        7: "./model/fr/7x5.png",
        8: "./model/fr/8x5.png",
        9: "./model/fr/9x5.png",
        10: "./model/fr/10x5.png",
        11: "./model/fr/11x5.png",
        12: "./model/fr/12x5.png",
        13: "./model/fr/13x5.png",
        14: "./model/fr/14x5.png",
        15: "./model/fr/15x5.png",
        16: "./model/fr/16x5.png",
        17: "./model/fr/17x5.png",
        18: "./model/fr/18x5.png",
        19: "./model/fr/19x5.png",
        20: "./model/fr/20x5.png",
    }
    return switcher.get(argument)


def SwitchArThreeChoices(argument):
    switcher = {
        5: "./model/ar/ar5x3.png",
        6: "./model/ar/ar6x3.png",
        7: "./model/ar/ar7x3.png",
        8: "./model/ar/ar8x3.png",
        9: "./model/ar/ar9x3.png",
        10: "./model/ar/ar10x3.png",
        11: "./model/ar/ar11x3.png",
        12: "./model/ar/ar12x3.png",
        13: "./model/ar/ar13x3.png",
        14: "./model/ar/ar14x3.png",
        15: "./model/ar/ar15x3.png",
        16: "./model/ar/ar16x3.png",
        17: "./model/ar/ar17x3.png",
        18: "./model/ar/ar18x3.png",
        19: "./model/ar/ar19x3.png",
        20: "./model/ar/ar20x3.png",
    }
    return switcher.get(argument)


def SwitchArFourChoices(argument):
    switcher = {
        5: "./model/ar/ar5x4.png",
        6: "./model/ar/ar6x4.png",
        7: "./model/ar/ar7x4.png",
        8: "./model/ar/ar8x4.png",
        9: "./model/ar/ar9x4.png",
        10: "./model/ar/ar10x4.png",
        11: "./model/ar/ar11x4.png",
        12: "./model/ar/ar12x4.png",
        13: "./model/ar/ar13x4.png",
        14: "./model/ar/ar14x4.png",
        15: "./model/ar/ar15x4.png",
        16: "./model/ar/ar16x4.png",
        17: "./model/ar/ar17x4.png",
        18: "./model/ar/ar18x4.png",
        19: "./model/ar/ar19x4.png",
        20: "./model/ar/ar20x4.png",
    }
    return switcher.get(argument)


def SwitchArFiveChoices(argument):
    switcher = {
        5: "./model/ar/ar5x5.png",
        6: "./model/ar/ar6x5.png",
        7: "./model/ar/ar7x5.png",
        8: "./model/ar/ar8x5.png",
        9: "./model/ar/ar9x5.png",
        10: "./model/ar/ar10x5.png",
        11: "./model/ar/ar11x5.png",
        12: "./model/ar/ar12x5.png",
        13: "./model/ar/ar13x5.png",
        14: "./model/ar/ar14x5.png",
        15: "./model/ar/ar15x5.png",
        16: "./model/ar/ar16x5.png",
        17: "./model/ar/ar17x5.png",
        18: "./model/ar/ar18x5.png",
        19: "./model/ar/ar19x5.png",
        20: "./model/ar/ar20x5.png",
    }
    return switcher.get(argument)


def loadAnswerSheet(questions, choices, lang):
    if lang == 'fr' or lang == 'en':
        if choices == 3:
            for x in r:
                if questions == x:
                    sheet = SwitchFrThreeChoices(x)
        elif choices == 4:
            for x in r:
                if questions == x:
                    sheet = SwitchFrFourChoices(x)
        elif choices == 5:
            for x in r:
                if questions == x:
                    sheet = SwitchFrFiveChoices(x)
    elif lang == 'ar':
        if choices == 3:
            for x in r:
                if questions == x:
                    sheet = SwitchArThreeChoices(x)
        elif choices == 4:
            for x in r:
                if questions == x:
                    sheet = SwitchArFourChoices(x)
        elif choices == 5:
            for x in r:
                if questions == x:
                    sheet = SwitchArFiveChoices(x)
    return sheet


def loadstdntinfo(workbook, number_of_students):
    global academiex, _classx, levelx, subjectx, semesterx, sessionx, directionx
    wb = opxl.load_workbook(f'{workbook}')
    sh1 = wb['NotesCC']
    names = []
    massar_id = []

    academie = sh1['D7'].value
    academiex = f'أكاديمية: {academie}'
    level = sh1['D9'].value
    levelx = f'المستوى: {level}'
    semester = sh1['D11'].value
    semesterx = f'الدورة: {semester}'
    session = sh1['D13'].value
    sessionx = f'السنة الدراسية: {session}'
    _class = sh1['I9'].value
    _classx = f'القسم: {_class}'
    direction = sh1['I7'].value
    directionx = f'م.الإقليمية: {direction}'
    subject = sh1['O11'].value
    subjectx = f'المادة: {subject}'

    names_column = sh1['D18':f'D{18+number_of_students}']
    for cell in names_column:
        for x in cell:
            names.append(x.value)

    massar_column = sh1['C18':f'C{18+number_of_students}']
    for cell in massar_column:
        for x in cell:
            massar_id.append(x.value)
    print(names)
    print(massar_id)
    return names, massar_id, _class


def genQR(exam_id, questions, choices, names, massar_id, _class):
    QR = []
    qrFilename = []
    for x in len(names):
        i = 1
        while os.path.exists("./qr/code%s.png" % i):
            i += 1
        fileName = ("./qr/code%s.png" % i)
        qrFilename.append(fileName)
        qrCode = qr.make((exam_id, questions, choices, names[x], massar_id[x], _class))
        QR.append(qrCode)
        QR[x].save(fileName)
    return qrFilename


def merge(QR, sheet):
    sheet = Image.open(sheet)
    sheetFileName = []
    for x in range(0, len(QR)):
        i = 1
        while os.path.exists("./sh/sheet%s.png" % i):
            i += 1
        fileName = ("./sh/sheet%s.png" % i)
        sheetFileName.append(fileName)
        code = Image.open(QR[x]).resize((280, 280))
        sheet.paste(code, (918, 640))
        sheet.save(fileName)
    return sheetFileName


def genPDF(sheetFileName):
    pdf = FPDF()
    pdf.set_auto_page_break(0)
    for imageFile in sheetFileName:
        cover = Image.open(imageFile)
        width, height = cover.size
        width, height = float(width * 0.264583), float(height * 0.264583)
        pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}
        orientation = 'P' if width < height else 'L'
        width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
        height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']
        pdf.add_page(orientation=orientation)
        pdf.image(imageFile, 0, 0, width, height)
    pdf.output("exam.pdf", "F")


def clean(qr, sheet):
    for f in qr:
        os.remove(f)
    for f in sheet:
        os.remove(f)


def generateExam(questions, choices, workbook, number_of_students, lang, exam_id):
    sheet = loadAnswerSheet(questions, choices, lang)
    names, massar_id, _class = loadstdntinfo(workbook, number_of_students)
    QR = genQR(exam_id, questions, choices, names, massar_id, _class)
    imagelist = merge(QR, sheet)
    genPDF(imagelist)
    clean(QR,imagelist)

#generateExam(20, 5, "./gg.xlsx", 39, "fr", 1)

names, massar_id, _class = loadstdntinfo("./gg.xlsx", 39)
genQR(5, 20, 5, names, massar_id, _class)


