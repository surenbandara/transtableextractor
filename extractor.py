import fitz  # PyMuPDF



def read_pdf(pdf_bytes):
    to_text=""
    # Open the PDF file
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

    # Iterate through each page
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Get the text of the page
        text = page.get_text()

        # Print or process the text as needed
        to_text+=text

    # Close the PDF file
    pdf_document.close()

    return to_text

# Example usage with your provided file
def text_extra(path):

    to_text = read_pdf(path)


    header1 = "No\nDate\nWaybill \nId\nCustomer Name\nPhone \nNumber\nAddress\nCOD\nRider Name\n"

    tex=to_text.replace(header1,"")

    index = 1
    tot_text=[]

    in_li=[tex.split("\n"+str(index)+"\n")[1]]

    further = True
    while further:

        index+=1
        divider=in_li[0].split("\n"+str(index)+"\n")
        if(len(divider)>1):
            in_li[0]=divider[1]
            in_li.append(divider[0])
        else:

            further = False
    las = in_li.pop(0)
    in_li.append(las)
    tot_text+=in_li
    

    return tot_text



###############################################################################################
def date_iden(lis):
    try:
        year = lis.pop(0)
        if(lis[0][2]=="-"):
            month = lis.pop(0)
        else:
            for detail in lis:
                if (detail[2]== "-"):
                    month = detail
                    lis.remove(detail)
                    break
        return year+month
    except Exception as e :
        return None

def waybillId_iden(lis):
    try:
        return  lis.pop(0)

    except Exception as e :
        return None


def name_idn(lis):
    try:
        name=""
        dele_li=[]
        for i in lis:
            if(not i[:-1].isdigit()):
                dele_li.append(i)
                name=name+i+" "
            else:
                name=name[:-1]
                break

        for k in dele_li:
            lis.remove(k)
        return name
    except Exception as e :
        return None

def number_idn(lis):
    try:
        number=[]
        dele_li=[]
        for i in lis:
            if(i[:-1].isdigit()):
                dele_li.append(i)
                number.append(i)
            else:
                break

        for k in dele_li:
            lis.remove(k)
        return number

    except Exception as e :
        return None


def address_idn(lis , ridername):
    try:
        ridername_lower = ridername.lower()
        adress=""
        dele_li=[]
        for i in lis:
            if (not ridername_lower in i.lower()) and (not i.isdigit()):
                dele_li.append(i)
                adress=adress+i+" "
            else:
                adress=adress[:-1]
                break

        for k in dele_li:
            lis.remove(k)
        return adress

    except Exception as e :
        return None

def COD_idn(lis):
   
    try:
        cod = lis.pop(0).split(" ")[0]
        if(cod.isdigit()):
            return int(cod.split(" ")[0])
        
        else:
            return None
    except Exception as e :
        return None



def setup_idn(lis,ridername):
    date = date_iden(lis)
    id = waybillId_iden(lis)
    name = name_idn(lis)
    numbers = number_idn(lis)
    address = address_idn(lis, ridername) 
    COD = COD_idn(lis)

    return {"date":date , "id" :id,
               "name" : name, "numbers" : numbers , 
               "address" : address , "COD" : COD}

######################################################################

def main(ridername, pdf_byte):
    tot_text = text_extra(pdf_byte)
    data = []
    for i in tot_text:

        data.append(setup_idn(i.split("\n"),ridername))

    return data
    

