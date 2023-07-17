with open("../main/pipeline/word_segmentation/VnVocab.txt", encoding="utf-8") as f:
    _set_vocab = set(f.read().split(", "))
with open("../main/data/words_pre_person_location.txt", encoding="utf-8") as f:
    _WORDS_PRE_PERSON_LOCATION = set(f.read().split())

_COUNTRY_L_NAME = {'đảo ascension', 'san marino', 'quần đảo faroe', 'hy lạp', 'cộng hoà trung phi', 'saint lucia', 'wallis và futuna', 'bồ đào nha', 'đảo norfolk', 'quần đảo cocos', 'trinidad và tobago', 'đài loan', 'cộng hoà congo', 'chdcnd triều tiên', 'sri lanka', 'phần lan', 'bosna và hercegovina', 'cộng hoà séc', 'trung quốc', 'hà lan', 'diego garcia', 'saint pierre và miquelon', 'hoa kỳ', 'burkina faso', 'ả rập xê-út', 'saint martin', 'costa rica', 'thổ nhĩ kỳ', 'thành vatican', 'ca-ri-bê hà lan', 'ba lan', 'el salvador', 'quần đảo bắc mariana', 'tây sahara', 'samoa thuộc mỹ', 'thái lan', 'na uy', 'cape verde', 'papua new guinea', 'tristan da cunha', 'liên bang micronesia', 'mông cổ', 'quần đảo cook', 'quần đảo solomon', 'đảo giáng sinh', 'triều tiên', 'quần đảo pitcairn', 'polynesia thuộc pháp', 'ả rập saudi', 'nam cực', 'quần đảo virgin', 'sierra leone', 'hồng kông', 'bờ biển ngà', 'chdc congo', 'new zealand', 'việt nam', 'quần đảo falkland', 'antigua và barbuda', 'turks và caicos', 'quần đảo cayman', 'trung phi', 'saint helena', 'ấn độ', 'svalbard và jan mayen', 'saint barthélemy', 'guinea xích đạo', 'đảo man', 'quần đảo marshall', 'guiana thuộc pháp', 'saint vincent và grenadines', 'cộng hoà dominica', 'miến điện', 'turk và caicos', 'tây ban nha', 'são tomé và príncipe', 'đông timor', 'vương quốc anh', 'new caledonia', 'cabo verde', 'nhật bản', 'thuỵ sĩ', 'saint kitts và nevis', 'bosnia và herzegovina', 'nam phi', 'đảo somoa thuộc mỹ', 'ai cập', 'ceuta và melilla', 'thuỵ điển', 'nam sudan', 'sint maarten', 'đan mạch', 'puerto rico', 'hàn quốc', 'quần đảo canary'}
_COUNTRY_S_NAME = {'maldives', 'uruguay', 'vanuatu', 'lesotho', 'georgia', 'gibraltar', 'macedonia', 'colombia', 'tajikistan', 'namibia', 'uae', 'gabon', 'guadeloupe', 'mauritius', 'guatemala', 'kenya', 'niue', 'congo', 'israel', 'eritrea', 'brunei', 'iceland', 'uzbekistan', 'guernsey', 'malawi', 'bermuda', 'burundi', 'canada', 'moldova', 'liechtenstein', 'dominica', 'guinée', 'philippines', 'ý', 'oman', 'pakistan', 'tonga', 'curaçao', 'fiji', 'samoa', 'algérie', 'nga', 'montserrat', 'algeria', 'niger', 'chile', 'singapore', 'mexico', 'turkmenistan', 'brasil', 'slovenia', 'tchad', 'tokelau', 'suriname', 'macau', 'anguilla', 'croatia', 'argentina', 'guam', 'latvia', 'li-băng', 'malta', 'jordan', 'somali', 'zimbabwe', 'réunion', 'peru', 'honduras', 'guinea', 'djibouti', 'ghana', 'úc', 'grenada', 'bhutan', 'paraguay', 'azerbaijan', 'nauru', 'gambia', 'bahrain', 'senegal', 'belarus', 'guinea-bissau', 'swaziland', 'andorra', 'belize', 'kyrgyzstan', 'i-rắc', 'bangladesh', 'áo', 'li-bi', 'haiti', 'zambia', 'togo', 'venezuela', 'nepal', 'litva', 'myanmar', 'angola', 'jersey', 'monaco', 'barbados', 'đức', 'lít-va', 'qatar', 'sudan', 'romania', 'montenegro', 'ukraina', 'madagascar', 'seychelles', 'indonesia', 'philippin', 'ukraine', 'brazil', 'yemen', 'bahamas', 'méxico', 'mozambique', 'ai-len', 'aruba', 'bulgaria', 'syria', 'palestine', 'rwanda', 'bungari', 'bénin', 'kazakhstan', 'uganda', 'timor-leste', 'serbia', 'martinique', 'iraq', 'mayotte', 'pháp', 'slovakia', 'tanzania', 'mỹ', 'mauritania', 'liberia', 'bolivia', 'ethiopia', 'séc', 'tunisia', 'somalia', 'macao', 'mali', 'lào', 'benin', 'libya', 'tuvalu', 'hungari', 'guyana', 'kuwait', 'luxembourg', 'liban', 'maroc', 'albania', 'guiné-bissau', 'ireland', 'gruzia', 'campuchia', 'jamaica', 'estonia', 'malaysia', 'micronesia', 'panama', 'hungary', 'românia', 'síp', 'ecuador', 'vatican', 'palau', 'kosovo', 'iran', 'chad', 'comoros', 'kiribati', 'bỉ', 'botswana', 'albani', 'cameroon', 'nigeria', 'ma-rốc', 'afghanistan', 'armenia', 'cô-oét', 'greenland', 'cuba', 'nicaragua'}
_WORLD_COMPANY = {'ibm', 'myspace', 'mercedes', 'spotify', 'bmw', 'ford', 'starbucks', 'lenovo', 'prada', 'linkedin', 'blackberry', 'walmart', 'hitachi', 'bbc', 'kfc', 'iphone', 'verizon', 'amazon', 'citibank', 'dell', 'subway', 'westpac', 'yahoo', 'canon', 'foxconn', 'rbc', 'mercedes-benz', 'cnn', 'carrefour', 'hermes', 'pepsi', 'coca-cola', 't-mobile', 'samsung', 'ups', 'kodak', 'cisco', 'intel', 'hp', 'digg', 'tencent', 'vodafone', 'google', 'visa', 'vmware', 'microsoft', 'android', 'facebook', 'mcdonalds', 'gucci', 'ebay', 'aldi', 'nokia', 'ikea', 'adobe', 'panasonic', 'mastercard', 'apple', 'nissan', 'toyota', 'fedex', 'sony', 'lego', 'loreal', 'paypal', 'acer', 'toshiba', 'honda', 'adidas', 'guardian', 'disney', 'baidu', 'mcdonald', 'nike', 'cvs', 'mtv', 'zara', 'youtube', 'siemens', 'motorola', 'colgate', 'twitter', 'gillette', 'oracle'}
_VN_LOCATIONS = {'chí linh', 'thanh sơn', 'bến cầu', 'thạnh phú', 'bến tre', 'kiến thuỵ', 'lệ thuỷ', 'vĩnh cửu', 'kiên hải', 'tuyên quang', 'thống nhất', 'hà đông', 'đà lạt', 'thái bình', 'krông pắk', 'quận 6', 'trực ninh', 'tam đường', 'mai châu', 'hương sơn', 'trà bồng', 'thuận bắc', 'đồng văn', 'quận 11', 'lâm hà', 'hoài ân', 'khoái châu', 'bắc bình', 'văn giang', 'quảng hà', 'quỳnh phụ', 'hậu giang', 'phú quý', 'hải dương', 'yên lạc', 'lạc thuỷ', 'định hoá', 'sìn hồ', 'cẩm mỹ', 'mỹ xuyên', 'sơn hà', 'hoà vang', 'trần văn thời', 'thủ dầu một', 'tuy an', 'xuyên mộc', 'điện bàn', 'lạc sơn', 'tuy hoà', 'tây hồ', 'sa thầy', 'thiệu hoá', 'phan thiết', 'cao lãnh', 'cồn cỏ', 'điện biên đông', 'vĩnh bảo', 'bạch thông', 'hưng yê', 'tân biên', 'mộc châu', 'quế phong', 'quận 1', 'quận 7', 'yên khánh', 'quảng bình', 'bà rịa', 'trà lĩnh', 'trường sa', 'hạ long', 'đông triều', 'thới bình', 'đà nẵng', 'quận 9', 'lai vung', 'tam kỳ', 'tiền giang', 'tư nghĩa', 'bảo yên', 'châu thành', 'phong điền', 'phan rang-tháp chàm', 'vĩnh thuận', 'yên thuỷ', 'kon rẫy', 'diễn châu', 'thanh chương', 'đồng xoài', 'bình giang', 'lộc bình', 'gò quao', 'cần giuộc', 'phú ninh', 'trấn yên', 'thốt nốt', 'gia viễn', 'na rì', 'dĩ an', 'phù cát', 'lâm thao', 'lộc ninh', 'hồng ngự', 'triệu sơn', 'lý nhân', 'việt yên', 'biên hoà', 'phan rang tháp chàm', 'tây trà', 'nam trà my', 'bình chánh', 'tam bình', 'vĩnh yên', 'ngọc lạc', 'kỳ anh', 'cẩm giàng', 'an biên', 'đan phượng', 'hưng hà', 'đăk glei', 'kim sơn', 'bố trạch', 'yên định', 'bình xuyên', 'chợ mới', 'việt trì', 'gia lộc', 'giồng trôm', 'phú quốc', 'giồng riềng', 'đức linh', 'tuần giáo', 'yên mô', 'cai lậy', 'bác ái', 'núi thành', 'văn yên', 'điện biên phủ', 'lạng giang', 'cẩm phả', 'phú lộc', 'đông sơn', 'long thành', 'cát tiên', 'tương dương', 'ia grai', 'nhơn trạch', 'quận 4', 'quảng uyên', 'vĩnh thạnh', 'quế sơn', 'gio linh', 'vũng liêm', 'mai sơn', 'văn chấn', 'tam dương', 'bình định', 'ba vì', 'hàm tân', 'cao bằng', 'đầm dơi', 'bình sơn', 'bảo lộc', 'an dương', 'dầu tiếng', 'chợ đồn', 'ninh kiều', 'xín mần', 'phụng hiệp', 'ba đình', "đăk r'lấp", 'triệu phong', 'nghi xuân', 'thường tín', 'đại lộc', 'phú vang', 'đông hà', 'thạch hà', 'chi lăng', 'chư păh', 'ngũ hành sơn', 'chợ gạo', 'nghệ an', 'na hang', 'bến lức', 'bình minh', 'phú yên', 'vĩnh hưng', 'tân phú', 'tân hiệp', 'điện biên', 'tiên phước', 'cầu giấy', 'từ sơn', 'kiên giang', 'yên thành', 'hoàng su phì', 'ba chẽ', 'đình lập', 'ninh giang', 'văn quan', 'đạ huoai', 'hậu lộc', 'vị thuỷ', 'quận 10', 'qui nhơn', 'thuận châu', 'thủ đức', 'kế sách', 'krông năng', 'vĩnh lợi', 'cù lao dung', 'đại từ', 'đak pơ', 'quận 12', 'lục yên', 'kim động', 'sa đéc', 'cái răng', 'ân thi', 'ngọc hồi', 'ngô quyền', 'sông hinh', 'nghĩa lộ', 'quảng ngãi', 'thanh hà', 'rạch giá', 'mỹ hào', 'tri tôn', 'quận 3', 'ngân sơn', 'như xuân', 'long hồ', 'bình gia', 'tiểu cần', 'văn bàn', 'hà tây', "m'đrăk", 'đức phổ', 'đăk glong', 'gia lai', 'gia nghĩa', 'gò dầu', 'quốc oai', 'thường xuân', 'cát hải', 'trà vinh', 'thanh miện', 'bảo thắng', 'sơn hoà', 'khánh vĩnh', 'hà nam', 'lê chân', 'mường lát', 'thanh hoá', 'đống đa', 'krông bông', 'bạc liêu', 'cần giờ', 'hòn đất', 'duyên hải', 'yên mỹ', 'đức cơ', 'hạ hoà', 'bát xát', 'cao phong', 'thuận thành', 'đạ tẻh', 'cao lộc', 'định quán', 'quản bạ', 'chiêm hoá', 'bắc hà', 'lai châu', 'xuân lộc', 'hoà bình', 'phước long', 'quang bình', 'nam giang', 'long phú', 'tân phước', 'sài gòn', 'hồng dân', 'yên bình', 'ba bể', 'krông pa', 'lương sơn', 'yên bái', 'châu phú', 'phù ninh', 'hồng lĩnh', 'ninh bình', 'lục nam', 'quan hoá', 'mù căng chải', 'móng cái', 'lý sơn', 'cờ đỏ', 'bá thước', 'long đất', 'gò vấp', 'chư prông', 'yên dũng', 'an minh', 'cần đước', 'quảng xương', 'kon plông', 'huế', 'chợ lách', 'bến cát', 'can lộc', 'trạm tấu', 'mường nhé', 'hồng bàng', 'đắk nông', 'kỳ sơn', 'đức huệ', 'thanh oai', 'bình lục', 'lang chánh', 'khánh sơn', 'gò công', 'hải châu', 'vũ thư', 'thanh xuân', 'hạ lang', 'bà rịa vũng tàu', 'gia lâm', 'mỏ cày', 'quảng trạch', 'tiên du', 'văn lâm', 'hương khê', 'đoan hùng', 'vạn ninh', 'đắk lắk', 'sa pa', 'xuân trường', 'ninh hoà', 'đồ sơn', 'tiên lãng', 'hiệp hoà', 'lục ngạn', 'kim bảng', 'quận 5', 'thanh khê', 'lăk', 'long mỹ', 'quảng trị', 'mỹ đức', 'ia pa', 'yên hưng', 'vân đồn', 'tân hồng', 'tuyên hoá', 'duy tiên', 'buôn ma thuột', 'trảng bom', 'kông chro', 'lấp vò', 'anh sơn', 'thái thuỵ', 'đầm hà', 'võ nhai', 'hiệp đức', 'chơn thành', 'lạng sơn', 'an lão', 'thông nông', 'tiên yên', 'hội an', 'u minh', 'mường chà', 'sơn tịnh', "ea h'leo", 'hải lăng', 'sơn tây', 'phủ lý', 'hưng yên', 'hương thuỷ', 'an khê', 'càng long', 'đông hải', 'tam nông', 'lập thạch', 'phổ yên', 'thạnh hoá', 'bù đăng', 'vũng tầu', 'quỳnh lưu', 'ea súp', 'bình phước', 'nghĩa hành', 'cam lộ', 'hữu lũng', 'sốp cộp', 'quảng điền', 'sông cầu', 'vĩnh châu', 'phú xuyên', 'tân châu', 'gia bình', 'long an', 'tràng định', 'sầm sơn', 'tân an', 'hải hậu', 'lâm đồng', 'tây giang', 'nam sách', 'hoàn kiếm', 'ứng hoà', 'tam điệp', 'hải phòng', 'quận 8', 'hàm thuận bắc', 'yên minh', 'tĩnh gia', 'nguyên bình', 'thái nguyên', 'bắc giang', 'hóc môn', 'nông cống', 'trùng khánh', 'phú nhuận', 'la gi', 'tây sơn', 'quan sơn', 'thuận an', 'năm căn', 'đăk tô', 'thoại sơn', 'sóc sơn', 'mộ đức', 'hoằng hoá', 'hoành bồ', 'hàm thuận nam', 'than uyên', 'thanh ba', 'bình thuỷ', 'đô lương', 'vĩnh long', 'yên châu', 'phù yên', 'hoa lư', 'sơn dương', 'an phú', 'ayun pa', 'tịnh biên', 'krông nô', 'đồng hới', 'thuỷ nguyên', 'nghĩa hưng', 'quảng ninh', 'ba tri', 'hướng hoá', 'mang yang', 'cần thơ', 'con cuông', 'vân canh', 'mỹ lộc', 'nghi lộc', 'phú giáo', 'vị thanh', 'diên khánh', 'ngã năm', 'uông bí', 'nam đông', 'tân uyên', 'sóc trăng', 'phước sơn', 'ninh sơn', 'lào cai', 'buôn đôn', 'ninh thuận', 'kim bôi', 'hoài đức', "cư m'gar", 'gò công tây', 'tiên lữ', 'kiến an', 'bỉm sơn', 'tân hưng', 'nhà bè', 'cẩm xuyên', 'mê linh', 'tây ninh', 'yên thế', 'kinh môn', 'đông giang', 'phú lương', 'trà ôn', 'quỳnh nhai', 'liên chiểu', 'kim thành', 'long xuyên', 'ý yên', 'gò công đông', 'vụ bản', 'hà tĩnh', 'bắc yên', 'đất đỏ', 'quận 2', 'mường khương', 'thanh liêm', 'bình thạnh', 'thạnh trị', 'ba tơ', 'trà cú', 'đăk mil', 'phù mỹ', 'cẩm thuỷ', 'ea kar', 'đông hưng', 'phục hoà', 'bắc quang', 'đông anh', 'bình dương', 'krông ana', 'minh long', 'trảng bàng', 'củ chi', 'hoà an', 'tân lạc', 'bắc trà my', 'hà trung', 'mường lay', 'phú thọ', 'cầu ngang', 'châu đức', 'bắc mê', 'cư jút', 'châu đốc', 'hoài nhơn', 'cái nước', 'bù đốp', 'tân kỳ', 'kbang', 'đăk song', 'thanh bình', 'thừa thiên huế', 'tuy phong', 'kiên lương', 'sơn trà', 'vị xuyên', 'nga sơn', 'hai bà trưng', 'khánh hoà', 'cửa lò', 'bắc sơn', 'phúc thọ', 'bình đại', 'thanh thuỷ', 'quế võ', 'bình tân', 'vĩnh linh', 'pleiku', 'tứ kỳ', 'thủ thừa', 'bảo lâm', 'đồng hỷ', 'nam định', 'vĩnh lộc', 'yên lập', 'đơn dương', 'thừa thiên-huế', 'minh hoá', 'tiền hải', 'đồng xuân', 'nha trang', 'hương trà', 'đồng nai', 'nho quan', 'mang thít', 'long khánh', 'tháp mười', 'giá rai', 'đà bắc', 'hưng nguyên', 'yên sơn', 'tuy phước', 'cầu kè', 'tủa chùa', 'ngọc hiển', 'phúc yên', 'thăng bình', 'hoàng mai', 'long biên', 'hà quảng', 'hà tiên', 'đa krông', 'vũ quang', 'chư sê', 'thạch an', 'mỹ tú', 'tân thạnh', 'nam trực', 'đăk hà', 'giao thuỷ', 'vinh', 'phù cừ', 'vĩnh phúc', 'thọ xuân', 'dương minh châu', 'kon tum', 'hồ chí minh', 'pác nặm', 'quỳ châu', 'bắc kạn', 'bà rịa-vũng tàu', 'bạch long vĩ', 'chương mỹ', 'ô môn', 'bình liêu', 'từ liêm', 'mường tè', 'lạc dương', 'tân yên', 'đồng tháp', 'phú tân', 'krông búk', 'vãn lãng', 'sơn động', 'hàm yên', 'sơn la', 'cô tô', 'mèo vạc', 'di linh', 'đức trọng', 'mộc hoá', 'sông mã', 'cái bè', 'tánh linh', 'kiến xương', 'lương tài', 'nam đàn', 'đak đoa', 'thạch thất', 'duy xuyên', 'thạch thành', 'yên phong', 'bắc ninh', 'an nhơn', 'bình long', 'tân trụ', 'quỳ hợp', 'hoàng sa', 'cam ranh', 'phú hoà', 'nghĩa đàn', 'mường la', 'hoà thành', 'phú bình', 'si ma cai', 'bảo lạc', 'sông công', 'hà nội', 'mỹ tho', 'quảng nam', 'cà mau', 'côn đảo', 'như thanh', 'việt nam', 'tân thành', 'an giang', 'đức hoà', 'đức thọ', 'đồng phù', 'vĩnh tường', 'tân bình', 'hà giang', 'phong thổ', 'thanh trì', 'bình thuận', 'ninh hải', 'ninh phước'}
_VN_FIRST_SENT_WORDS = {'vượt', 'điện', 'nhìn', 'đảo', 'phim', 'riêng', 'cty', 'luật', 'ong', 'tháp', 'trong', 'bến', 'động', 'cúng', 'miền', 'giải', 'đêm', 'fred', 'ấp', 'tùng', 'bọn', 'bố', 'vợ', 'chỗ', 'sinh', 'liệu', 'vẫn', 'bóng', 'bởi', 'thương', 'lập', 'thư', 'nhưng', 'theo', 'rời', 'còn', 'trưởng', 'cục', 'viên', 'chắc', 'nay', 'rồi', 'đài', 'cảng', 'website', 'cách', 'giờ', 'phó', 'nhánh', 'đợt', 'cầu', 'khi', 'cụm', 'nhà', 'hạng', 'tại', 'tim', 'metro', 'bản', 'đoạn', 'dãy', 'được', 'chuyện', 'ngày', 'toyota', 'biển', 'giọng', 'tự', 'nài', 'đĩa', 'đường', 'rừng', 'cô', 'gọi', 'sân', 'hai', 'thành', 'núi', 'tỉnh', 'em', 'viện', 'thằng', 'chị', 'má', 'anh', 'tập', 'cụ', 'neil', 'sâm', 'lính', 'cống', 'cháu', 'về', 'đồn', 'chính', 'nghe', 'bảng', 'như', 'trời', 'nghỉ', 'với', 'con', 'ra', 'trục', 'bệnh', 'vốn', 'tết', 'cò', 'đầm', 'chợ', 'dắt', 'hầm', 'chú', 'tàu', 'wikipedia', 'vùng', 'nguyên', 'trại', 'bộ', 'thôn', 'bế', 'đoàn', 'nàng', 'khu', 'kênh', 'khắp', 'chủ', 'ban', 'đèo', 'tuy', 'dì', 'mỗi', 'hàng', 'vịnh', 'nhóm', 'số', 'làm', 'hết', 'quyền', 'trùm', 'dòng', 'sông', 'nghĩa', 'chứ', 'đến', 'tờ', 'virus', 'vụ', 'ngành', 'thuyền', 'chùa', 'chờ', 'đồng', 'bé', 'quê', 'thấy', 'các', 'biết', 'hôm', 'lúc', 'lái', 'dù', 'lao', 'đội', 'vàng', 'cùng', 'là', 'quận', 'bầu', 'tới', 'chàng', 'trên', 'ba', 'đất', 'hội', 'nếu', 'một', 'ngay', 'trạm', 'đi', 'hoặc', 'xe', 'giữa', 'phòng', 'khách', 'sau', 'hồi', 'đọc', 'nguồn', 'mẹ', 'chồng', 'cậu', 'bên', 'băng', 'già', 'nhớ', 'bà', 'song', 'kungfu', 'những', 'dân', 'cuốn', 'buôn', 'giao', 'tuồng', 'gần', 'trừ', 'lang', 'tân', 'huyện', 'cặp', 'cũng', 'của', 'bạn', 'gà', 'gái', 'tên', 'lên', 'taxi', 'bốn', 'nhiễm', 'sang', 'đèn', 'và', 'chữ', 'ngoài', 'sợ', 'mặt', 'phố', 'thầy', 'đầu', 'phần', 'bác', 'chúc', 'nhờ', 'tiếng', 'chiếc', 'hiện', 'toàn', 'xã', 'vậy', 'đảng', 'đỉnh', 'quí', 'từ', 'quĩ', 'trán', 'giặc', 'gặp', 'tướng', 'có', 'cha', 'sao', 'phía', 'trường', 'người', 'họ', 'nơi', 'hồ', 'mà', 'sách', 'pha', 'xóm', 'hỏi', 'trước', 'sở', 'năm', 'ông', 'quân', 'bỗng', 'làng', 'để', 'cho', 'cả', 'cửa', 'đền', 'do', 'ôi', 'chống', 'trà', 'lão', 'mắt', 'quít', 'phường', 'hay', 'cu', 'vì', 'vietcombank', 'báo', 'mong', 'họp', 'việc', 'tuyển', 'bar', 'vào', 'nước', 'giới', 'xem', 'thuốc', 'nhiều'}
_VN_MIDDLE_NAMES = {'hà', 'nguyễn', 'linh', 'ánh', 'vân', 'tiến', 'bảo', 'trúc', 'như', 'văn', 'thu', 'nam', 'thời', 'quang', 'trọng', 'hữu', 'mạnh', 'thành', 'hùng', 'thiện', 'thanh', 'đắc', 'đình', 'phi', 'xuân', 'ninh', 'thảo', 'thái', 'trung', 'mai', 'vũ', 'trường', 'vô', 'quốc', 'tường', 'thiên', 'mỹ', 'thùy', 'hoành', 'cảnh', 'ưng', 'mộng', 'diệu', 'hồng', 'tố', 'quỳnh', 'chí', 'duy', 'tú', 'kế', 'bé', 'nữ', 'việt', 'lệnh', 'bội', 'hoa', 'anh', 'lệ', 'quý', 'viết', 'thuỳ', 'bửu', 'hoàng', 'cao', 'thuý', 'gia', 'công', 'hoài', 'đức', 'qui', 'thi', 'diễm', 'đinh', 'nhất', 'minh', 'huy', 'vĩnh', 'khắc', 'miên', 'phương', 'tuấn', 'phú', 'hải', 'phúc', 'an', 'thế', 'lê', 'tuyết', 'khánh', 'huyền', 'chính', 'lan', 'bá', 'thị', 'sơn', 'danh', 'ngọc', 'tôn', 'nguyên', 'thúy', 'kim', 'đăng', 'bích', 'phước', 'kiều', 'tấn', 'bao', 'tử', 'nhật', 'huỳnh', 'nguyệt', 'cẩm', 'doãn'}
_VN_FAMILY_NAMES = {'lâm', 'hương', 'ngô', 'vương', 'hà', 'vũ', 'hường', 'giang', 'chi', 'văn', 'huỳnh', 'quy', 'tô', 'thân', 'trần', 'hông', 'hoàng', 'vinh', 'bửu', 'võ', 'ưng', 'hồ', 'trịnh', 'trương', 'đào', 'đỗ', 'phạm', 'qui', 'vĩnh', 'đặng', 'mai', 'phan', 'bưu', 'la', 'lương', 'dương', 'bảo', 'lưu', 'lê', 'diệp', 'hồng', 'nguyễn', 'đoàn', 'tạ', 'nguyên', 'doãn', 'lý', 'lan', 'bùi', 'diêu', 'huyên', 'miên', 'huyền', 'tôn', 'trân', 'tằng', 'bao', 'từ', 'cao', 'công', 'ngọc', 'mạc', 'đinh'}

class Vocabulary:
    def __init__(self):
        self._VN_DICT = _set_vocab
        self._COUNTRY_L_NAME = _COUNTRY_L_NAME
        self._COUNTRY_S_NAME = _COUNTRY_S_NAME
        self._WORLD_COMPANY = _WORLD_COMPANY
        self._VN_LOCATIONS = _VN_LOCATIONS
        self._VN_FIRST_SENT_WORDS = _VN_FIRST_SENT_WORDS
        self._VN_MIDDLE_NAMES = _VN_MIDDLE_NAMES
        self._VN_FAMILY_NAMES = _VN_FAMILY_NAMES
        self._VN_PRONOUNS = _WORDS_PRE_PERSON_LOCATION

    @property
    def VN_DICT(self):
        return set(word for word in self._VN_DICT)

    @property
    def COUNTRY_L_NAME(self):
        return self._COUNTRY_L_NAME

    @COUNTRY_L_NAME.setter
    def COUNTRY_L_NAME(self, value):
        self._COUNTRY_L_NAME.add(value)

    @property
    def COUNTRY_S_NAME(self):
        return self._COUNTRY_S_NAME

    @COUNTRY_S_NAME.setter
    def COUNTRY_S_NAME(self, value):
        self._COUNTRY_S_NAME.add(value)

    @property
    def VN_LOCATIONS(self):
        return self._VN_LOCATIONS

    @VN_LOCATIONS.setter
    def VN_LOCATIONS(self, value):
        self._VN_LOCATIONS.add(value)

    @property
    def WORLD_COMPANY(self):
        return self._WORLD_COMPANY

    @WORLD_COMPANY.setter
    def WORLD_COMPANY(self, value):
        self._WORLD_COMPANY.add(value)

    @property
    def VN_FIRST_SENT_WORDS(self):
        return self._VN_FIRST_SENT_WORDS

    @VN_FIRST_SENT_WORDS.setter
    def VN_FIRST_SENT_WORDS(self, value):
        self._VN_FIRST_SENT_WORDS.add(value)

    @property
    def VN_MIDDLE_NAMES(self):
        return self._VN_MIDDLE_NAMES

    @VN_MIDDLE_NAMES.setter
    def VN_MIDDLE_NAMES(self, value):
        self._VN_MIDDLE_NAMES.add(value)

    @property
    def VN_FAMILY_NAMES(self):
        return self._VN_FAMILY_NAMES

    @VN_FAMILY_NAMES.setter
    def VN_FAMILY_NAMES(self, value):
        self._VN_FAMILY_NAMES.add(value)


    @property
    def VN_PRONOUNS(self):
        return self._VN_PRONOUNS

    @VN_PRONOUNS.setter
    def VN_PRONOUNS(self, value):
        self._VN_PRONOUNS.add(value)