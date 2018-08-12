from multimidia import Multimidia

class Card:
    id: int
    dificuldade: float
    tag: list
    questao: str
    opcoes: list
    opcaoCorreta: str
    multimidia: Multimidia
    infoAdicional: str

    def createCard(self, id: int, dificuldade: float, tag: list, questao:str,
                   opcoes: list, opcaoCorreta:str ,multimidia: Multimidia, infoAdicional: str):
        new_card = Card()
        new_card.id = id
        new_card.dificuldade = dificuldade
        new_card.tag = tag
        new_card.questao = questao
        new_card.opcoes = opcoes
        new_card.opcaoCorreta = opcaoCorreta
        new_card.multimidia = multimidia
        new_card.infoAdicional = infoAdicional
        return new_card

    def removeBlankSpaces(self, stringArray):
        newArray = []
        for string in stringArray:
            newArray.append(string.strip())
        return newArray

    def dictToCard(self, currentJsonCard):
        return self.createCard(
            currentJsonCard['id'],
            currentJsonCard['dificuldade'],
            self.removeBlankSpaces(str.split(currentJsonCard['tag'], sep=',')),
            currentJsonCard['questao'],
            [
                currentJsonCard['opcao1'],
                currentJsonCard['opcao2'],
                currentJsonCard['opcao3'],
                currentJsonCard['opcao4']
            ],
            currentJsonCard['opcaoCorreta'],
            Multimidia(currentJsonCard['tipo'], currentJsonCard['src']),
            currentJsonCard['informacaoAdicional']
        )

    def reprJSON(self):
        return dict(
            id=self.id,
            dificuldade=self.dificuldade,
            tag=self.tag,
            questao=self.questao,
            opcoes=self.opcoes,
            opcaoCorreta=self.opcaoCorreta,
            multimidia=self.multimidia,
            infoAdicional=self.infoAdicional
        )