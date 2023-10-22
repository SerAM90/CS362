from credit_card_validator import credit_card_validator
import unittest

'''
VISA: 16 digits, starting with 4.
'''
class TestValidateCreditCard(unittest.TestCase):
    def test_1(self):
        self.assertFalse(credit_card_validator("")) #empty string test

    '''
    Visa: 16 digits, starting with 4.
    '''
    def test_2(self):
        self.assertTrue(credit_card_validator("4111111111111111")) #visa boundary test - correct length

    def test_3(self):
        self.assertFalse(credit_card_validator("4234567810111212")) #visa boundary test - too many numbers at 16

    def test_4(self):
        self.assertFalse(credit_card_validator("47895642389865478")) #visa boundary test - too many numbers at 17
    def test_5(self):
        self.assertFalse(credit_card_validator("478956423898654788")) #visa boundary test - too many numbers at 18
    def test_6(self):
        self.assertFalse(credit_card_validator("478956423898654")) #visa wrong at 15
    def test_7(self):    
        self.assertFalse(credit_card_validator("47895642389865")) #visa wrong at 14
    #wrong prefix
    def test_52(self):
        self.assertFalse(credit_card_validator("3234567810111212")) #wrong prefix, right length
    def test_53(self):
        self.assertFalse(credit_card_validator("2345678101112124")) #wrong prefix, right length
    def test_54(self):
        self.assertFalse(credit_card_validator("323456781011121")) #wrong prefix, wrong length
    def test_55(self):
        self.assertFalse(credit_card_validator("23456781011121245")) #wrong prefix, wrong length
    #5
    def test_56(self):
        self.assertFalse(credit_card_validator("5234567810111212")) #wrong prefix, right length
    def test_57(self):
        self.assertFalse(credit_card_validator("5345678101112124")) #wrong prefix, right length
    def test_58(self):
        self.assertFalse(credit_card_validator("523456781011121")) #wrong prefix, wrong length
    def test_59(self):
        self.assertFalse(credit_card_validator("53456781011121245")) #wrong prefix, wrong length
    #6
    def test_60(self):
        self.assertFalse(credit_card_validator("6234567810111212")) #wrong prefix, right length
    def test_61(self):
        self.assertFalse(credit_card_validator("6345678101112124")) #wrong prefix, right length
    def test_62(self):
        self.assertFalse(credit_card_validator("623456781011121")) #wrong prefix, wrong length
    def test_63(self):
        self.assertFalse(credit_card_validator("63456781011121245")) #wrong prefix, wrong length
    '''     
    MasterCard: 16 digits, starting with 51 through 55, or 2221 through 2720.
    '''
    #2221-2720 test
    def test_8(self):
        self.assertFalse(credit_card_validator("2720123547894512")) #mastercard boundary test -16 
    def test_9(self):
        self.assertTrue(credit_card_validator("2720123547894512")) #mastercard boundary test -16
    def test_10(self):
        self.assertTrue(credit_card_validator("2221123547894512")) #mastercard boundary test -16
    def test_11(self):
        self.assertFalse(credit_card_validator("2221123547894512")) #mastercard boundary test -16 
    #15
    def test_12(self):
        self.assertFalse(credit_card_validator("272012354789451")) #mastercard boundary test -15 
    def test_13(self):
        self.assertTrue(credit_card_validator("272012354789451")) #mastercard boundary test -15
    def test_14(self):
        self.assertTrue(credit_card_validator("222112354789451")) #mastercard boundary test -15
    def test_15(self):
        self.assertFalse(credit_card_validator("222112354789451")) #mastercard boundary test -15 
    #14
    def test_16(self):
        self.assertFalse(credit_card_validator("27201235478945")) #mastercard boundary test -14 
    def test_17(self):
        self.assertTrue(credit_card_validator("27201235478945")) #mastercard boundary test -14
    def test_18(self):
        self.assertTrue(credit_card_validator("22211235478945")) #mastercard boundary test -14
    def test_19(self):
        self.assertFalse(credit_card_validator("22211235478945")) #mastercard boundary test -14 
    #51-55 test
    def test_20(self):
        self.assertFalse(credit_card_validator("5520123547894512")) #mastercard boundary test -16 
    def test_21(self):
        self.assertTrue(credit_card_validator("5520123547894512")) #mastercard boundary test -16
    def test_22(self):
        self.assertTrue(credit_card_validator("5121123547894512")) #mastercard boundary test -16
    def test_23(self):
        self.assertFalse(credit_card_validator("5121123547894512")) #mastercard boundary test -16 
    #15
    def test_24(self):
        self.assertFalse(credit_card_validator("552012354789451")) #mastercard boundary test -15 
    def test_25(self):
        self.assertTrue(credit_card_validator("552012354789451")) #mastercard boundary test -15
    def test_26(self):
        self.assertTrue(credit_card_validator("512112354789451")) #mastercard boundary test -15
    def test_27(self):
        self.assertFalse(credit_card_validator("512112354789451")) #mastercard boundary test -15 
    #14
    def test_28(self):
        self.assertFalse(credit_card_validator("55201235478945")) #mastercard boundary test -14 
    def test_29(self):
        self.assertTrue(credit_card_validator("55201235478945")) #mastercard boundary test -14
    def test_30(self):
        self.assertTrue(credit_card_validator("51211235478945")) #mastercard boundary test -14
    def test_31(self):
        self.assertFalse(credit_card_validator("51211235478945")) #mastercard boundary test -14 
    #wrong prefix   
    def test_40(self):
        self.assertFalse(credit_card_validator("2620123547894512")) #wrong prefix, right length
    def test_41(self):
        self.assertFalse(credit_card_validator("2721123547894512")) #wrong prefix, right length
    def test_42(self):
        self.assertFalse(credit_card_validator("5021123547894512")) #wrong prefix, right length
    def test_43(self):
        self.assertFalse(credit_card_validator("5221123547894512")) #wrong prefix, right length
    def test_44(self):
        self.assertFalse(credit_card_validator("5421123547894512")) #wrong prefix, right length
    def test_45(self):
        self.assertFalse(credit_card_validator("5621123547894512")) #wrong prefix, right length
    ''''''
    def test_46(self):
        self.assertFalse(credit_card_validator("262012354789451")) #wrong prefix, wrong length//15
    def test_47(self):
        self.assertFalse(credit_card_validator("272112354789451")) #wrong prefix, wrong length//15
    def test_48(self):
        self.assertFalse(credit_card_validator("502112354789451")) #wrong prefix, wrong length//15
    def test_49(self):
        self.assertFalse(credit_card_validator("522112354789455")) #wrong prefix, wrong length//15
    def test_50(self):
        self.assertFalse(credit_card_validator("542112354789451")) #wrong prefix, wrong length//15
    def test_51(self):
        self.assertFalse(credit_card_validator("562112354789451")) #wrong prefix, wrong length//15
    ''''''
    def test_64(self):
        self.assertFalse(credit_card_validator("26201235478945121")) #wrong prefix, wrong length//17
    def test_65(self):
        self.assertFalse(credit_card_validator("27211235478945121")) #wrong prefix, wrong length//17
    def test_66(self):
        self.assertFalse(credit_card_validator("50211235478945121")) #wrong prefix, wrong length//17
    def test_67(self):
        self.assertFalse(credit_card_validator("52211235478945152")) #wrong prefix, wrong length//17
    def test_68(self):
        self.assertFalse(credit_card_validator("54211235478945151")) #wrong prefix, wrong length//17
    def test_69(self):
        self.assertFalse(credit_card_validator("56211235478945151")) #wrong prefix, wrong length//17

    '''
    American Express: 15 digits, starting with 34 or 37.
    '''
    #37
    def test_32(self):
        self.assertTrue(credit_card_validator("378282246310005"))  #amex boundary test - correct with 15 digits
    
    def test_33(self):
        self.assertFalse(credit_card_validator("3782822463100089"))  #amex boundary test - too many numbers at 16
    def test_34(self):
        self.assertFalse(credit_card_validator("37828224631000898"))  #amex boundary test - too many numbers at 17
    def test_34(self):
        self.assertFalse(credit_card_validator("37828224631008")) #too few at 14
    def test_34(self):
        self.assertFalse(credit_card_validator("3782822463100")) #too few at 13
    #34
    def test_35(self):
        self.assertTrue(credit_card_validator("348282246310005"))  #amex boundary test - correct with 15 digits
    
    def test_36(self):
        self.assertFalse(credit_card_validator("3482822463100089"))  #amex boundary test - too many numbers at 16
    def test_37(self):
        self.assertFalse(credit_card_validator("34828224631000898"))  #amex boundary test - too many numbers at 17
    def test_38(self):
        self.assertFalse(credit_card_validator("37006638890768")) #too few at 14
    def test_39(self):
        self.assertFalse(credit_card_validator("3482822463100")) #too few at 13
    #wrong prefix
    def test_70(self):
        self.assertTrue(credit_card_validator("388282246310005"))  #wrong prefix, right length
    
    def test_71(self):
        self.assertFalse(credit_card_validator("3882822463100080"))  #wrong prefix, right length
    def test_72(self):
        self.assertFalse(credit_card_validator("3882822463100089"))  #wrong prefix, right length
    def test_73(self):
        self.assertFalse(credit_card_validator("38828224631008")) #wrong prefix, wrong length//14
    def test_74(self):
        self.assertFalse(credit_card_validator("38828224631000")) #wrong prefix, wrong length//14
    def test_75(self):
        self.assertFalse(credit_card_validator("3882822463100855")) #wrong prefix, wrong length//16
    def test_76(self):
        self.assertFalse(credit_card_validator("3882822463100066")) #wrong prefix, wrong length//16
    def test_77(self):
        self.assertTrue(credit_card_validator("388282246310005"))  #wrong prefix, right length
    
    def test_78(self):
        self.assertFalse(credit_card_validator("3582822463100089"))  #wrong prefix, right length
    def test_79(self):
        self.assertFalse(credit_card_validator("358282246310008"))  #wrong prefix, right length
    def test_80(self):
        self.assertFalse(credit_card_validator("35828224631008")) #wrong prefix, wrong length//14
    def test_81(self):
        self.assertFalse(credit_card_validator("35828224631000")) #wrong prefix, wrong length//14
    def test_82(self):
        self.assertFalse(credit_card_validator("3582822463100855")) #wrong prefix, wrong length//16
    def test_82(self):
        self.assertFalse(credit_card_validator("3582822463100066")) #wrong prefix, wrong length//16

    #
    def test_83(self):
        self.assertFalse(credit_card_validator("328282246310008"))  #wrong prefix, right length
    def test_84(self):
        self.assertFalse(credit_card_validator("338282246310008"))  #wrong prefix, right length
    def test_85(self):
        self.assertFalse(credit_card_validator("368282246310008"))  #wrong prefix, right length
    def test_86(self):
        self.assertFalse(credit_card_validator("388282246310008"))  #wrong prefix, right length
    def test_87(self):
        self.assertFalse(credit_card_validator("398282246310008"))  #wrong prefix, right length    
    #
    def test_88(self):
        self.assertFalse(credit_card_validator("32828224631000"))  #wrong prefix, wrong length//14
    def test_89(self):
        self.assertFalse(credit_card_validator("33828224631008"))  #wrong prefix, wrong length//14
    def test_90(self):
        self.assertFalse(credit_card_validator("36828224631008"))  #wrong prefix, wrong length//14
    def test_91(self):
        self.assertFalse(credit_card_validator("38828224631008"))  #wrong prefix, wrong length//14
    def test_92(self):
        self.assertFalse(credit_card_validator("39828224630008"))  #wrong prefix, wrong length//14
    #
    def test_93(self):
        self.assertFalse(credit_card_validator("3282822463100022"))  #wrong prefix, wrong length//16
    def test_94(self):
        self.assertFalse(credit_card_validator("3382822463100822"))  #wrong prefix, wrong length//16
    def test_95(self):
        self.assertFalse(credit_card_validator("3682822463100822"))  #wrong prefix, wrong length//16
    def test_96(self):
        self.assertFalse(credit_card_validator("3882822463100822"))  #wrong prefix, wrong length//16
    def test_97(self):
        self.assertFalse(credit_card_validator("3982822463000822"))  #wrong prefix, wrong length//16
    


    # def test_12(self):
    #     self.assertFalse(credit_card_validator("3782822463100")) #amex boundary test - too few numbers at 13
    
    # def test_13(self):
    #     self.assertFalse(credit_card_validator("378282246310000")) #amex boundary test - too many numbers at 15
    
    # def test_14(self):
    #     self.assertFalse(credit_card_validator("37828224631000")) #amex boundary test - too many numbers at 14
    
    # ''''''
    # def test_15(self):
    #     self.assertFalse(credit_card_validator("3482822463100")) #amex boundary test - too few numbers at 13
    
    # def test_16(self):
    #     self.assertFalse(credit_card_validator("348282246310000")) #amex boundary test - too many numbers at 15
    
    # def test_17(self):
    #     self.assertFalse(credit_card_validator("34828224631000")) #amex boundary test - too many numbers at 14
    # def test_18(self):
    #     self.assertTrue(credit_card_validator("348282246310005"))  #amex boundary test - correct with 15 digits

    # def test_19(self):
    #     self.assertFalse(credit_card_validator("348282246310008987"))  #amex boundary test - too many numbers at 18

    # def test_20(self):
    #     self.assertTrue(credit_card_validator("5582822463100055"))  #mastercard boundary test - correct with 16 digits
    # def test_21(self):
    #     self.assertFalse(credit_card_validator("558282246310005"))  #mastercard boundary test - too few numbers at 15
    # def test_22(self):
    #     self.assertFalse(credit_card_validator("55828224631000555"))  #mastercard boundary test - too many numbers at 17
    # def test_23(self):
    #     self.assertFalse(credit_card_validator("558282246310005555"))  #mastercard boundary test - too many numbers at 18
    # def test_24(self):
    #     self.assertFalse(credit_card_validator("55828224631000"))  #mastercard boundary test - too many numbers at 14
    # def test_25(self):
    #     self.assertTrue(credit_card_validator("5182822463100055"))  #mastercard boundary test - correct with 16 digits
    # def test_26(self):
    #     self.assertFalse(credit_card_validator("518282246310005"))  #mastercard boundary test - too few numbers at 15
    # def test_27(self):
    #     self.assertFalse(credit_card_validator("51828224631000555"))  #mastercard boundary test - too many numbers at 17
    # def test_28(self):
    #     self.assertFalse(credit_card_validator("518282246310005555"))  #mastercard boundary test - too many numbers at 18
    # def test_29(self):
    #     self.assertFalse(credit_card_validator("51828224631000"))  #mastercard boundary test - too many numbers at 14
    # ''''''
    # def test_30(self):
    #     self.assertTrue(credit_card_validator("2720254897631547"))  #mastercard boundary test - correct with 16 digits
    # def test_31(self):
    #     self.assertFalse(credit_card_validator("272025489763154"))  #mastercard boundary test - too few numbers at 15
    # def test_32(self):
    #     self.assertFalse(credit_card_validator("27202548976315477"))  #mastercard boundary test - too many numbers at 17
    # def test_33(self):
    #     self.assertFalse(credit_card_validator("272025489763154777"))  #mastercard boundary test - too many numbers at 18
    # def test_34(self):
    #     self.assertFalse(credit_card_validator("27202548976315"))  #mastercard boundary test - too few numbers at 14
    # def test_35(self):
    #     self.assertTrue(credit_card_validator("272025489763154"))  #mastercard boundary test - correct with 15 digits
    # def test_36(self):
    #     self.assertTrue(credit_card_validator("2221000000000009"))  #mastercard boundary test - correct with 16 digits
    # def test_37(self):
    #     self.assertFalse(credit_card_validator("2221000000000009"))  #mastercard boundary test - wrong with 17 digits
    # def test_38(self):
    #     self.assertFalse(credit_card_validator("22210000000000094"))  #mastercard boundary test - wrong with 18 digits
    # def test_39(self):
    #     self.assertFalse(credit_card_validator("222100000000045"))  #mastercard boundary test - wrong with 15 digits
    # def test_40(self):
    #     self.assertFalse(credit_card_validator("22210000000000"))  #mastercard boundary test - wrong with 14 digits      
    # def test_6(self):
    #     self.assertFalse(credit_card_validator("22210000000000009"))
    
    # def test_7(self):
    #     self.assertFalse(credit_card_validator("378956423898654"))
    # def test_8(self):
    #     self.assertFalse(credit_card_validator("378956423898654"))
    # def test_9(self):
    #     self.assertTrue(credit_card_validator("378956423898654"))

    # def test_11(self):
    #     self.assertFalse(credit_card_validator("47895642389865"))
    ''''''
    



if __name__ == '__main__':
    unittest.main()