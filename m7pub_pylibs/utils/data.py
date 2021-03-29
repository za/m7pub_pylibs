#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2009, MARIMORE Inc Tokyo, Japan.
# Contributed by 
#       Iqbal Abdullah <iqbal@marimore.co.jp>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
#   *   Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#   *   Redistributions in binary form must reproduce the above copyright notice, 
#       this list of conditions and the following disclaimer in the documentation 
#       and/or other materials provided with the distribution.
#   *   Neither the name of the MARIMORE Inc nor the names of its contributors 
#       may be used to endorse or promote products derived from this software 
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
General reusable data
"""

__author__      = "Iqbal Abdullah <iqbal@marimore.co.jp>"
__date__        = "$LastChangedDate$"
__version__     = "$LastChangedRevision$"

WORLD_COUNTRIES = (

("AF", "AFGHANISTAN"),
("AX", "ÅLAND ISLANDS"),
("AL", "ALBANIA"),
("DZ", "ALGERIA"),
("AS", "AMERICAN SAMOA"),
("AD", "ANDORRA"),
("AO", "ANGOLA"),
("AI", "ANGUILLA"),
("AQ", "ANTARCTICA"),
("AG", "ANTIGUA AND BARBUDA"),
("AR", "ARGENTINA"),
("AM", "ARMENIA"),
("AW", "ARUBA"),
("AU", "AUSTRALIA"),
("AT", "AUSTRIA"),
("AZ", "AZERBAIJAN"),
("BS", "BAHAMAS"),
("BH", "BAHRAIN"),
("BD", "BANGLADESH"),
("BB", "BARBADOS"),
("BY", "BELARUS"),
("BE", "BELGIUM"),
("BZ", "BELIZE"),
("BJ", "BENIN"),
("BM", "BERMUDA"),
("BT", "BHUTAN"),
("BO", "BOLIVIA"),
("BA", "BOSNIA AND HERZEGOVINA"),
("BW", "BOTSWANA"),
("BV", "BOUVET ISLAND"),
("BR", "BRAZIL"),
("IO", "BRITISH INDIAN OCEAN TERRITORY"),
("BN", "BRUNEI DARUSSALAM"),
("BG", "BULGARIA"),
("BF", "BURKINA FASO"),
("BI", "BURUNDI"),
("KH", "CAMBODIA"),
("CM", "CAMEROON"),
("CA", "CANADA"),
("CV", "CAPE VERDE"),
("KY", "CAYMAN ISLANDS"),
("CF", "CENTRAL AFRICAN REPUBLIC"),
("TD", "CHAD"),
("CL", "CHILE"),
("CN", "CHINA"),
("CX", "CHRISTMAS ISLAND"),
("CC", "COCOS (KEELING) ISLANDS"),
("CO", "COLOMBIA"),
("KM", "COMOROS"),
("CG", "REPUBLIC OF CONGO"),
("CD", "DR CONGO"),
("CK", "COOK ISLANDS"),
("CR", "COSTA RICA"),
("CI", "CÔTE D'IVOIRE"),
("HR", "CROATIA"),
("CU", "CUBA"),
("CY", "CYPRUS"),
("CZ", "CZECH REPUBLIC"),
("DK", "DENMARK"),
("DJ", "DJIBOUTI"),
("DM", "DOMINICA"),
("DO", "DOMINICAN REPUBLIC"),
("EC", "ECUADOR"),
("EG", "EGYPT"),
("SV", "EL SALVADOR"),
("GQ", "EQUATORIAL GUINEA"),
("ER", "ERITREA"),
("EE", "ESTONIA"),
("ET", "ETHIOPIA"),
("FK", "FALKLAND ISLANDS (MALVINAS)"),
("FO", "FAROE ISLANDS"),
("FJ", "FIJI"),
("FI", "FINLAND"),
("FR", "FRANCE"),
("GF", "FRENCH GUIANA"),
("PF", "FRENCH POLYNESIA"),
("TF", "FRENCH SOUTHERN TERRITORIES"),
("GA", "GABON"),
("GM", "GAMBIA"),
("GE", "GEORGIA"),
("DE", "GERMANY"),
("GH", "GHANA"),
("GI", "GIBRALTAR"),
("GR", "GREECE"),
("GL", "GREENLAND"),
("GD", "GRENADA"),
("GP", "GUADELOUPE"),
("GU", "GUAM"),
("GT", "GUATEMALA"),
("GG", "GUERNSEY"),
("GN", "GUINEA"),
("GW", "GUINEA-BISSAU"),
("GY", "GUYANA"),
("HT", "HAITI"),
("HM", "HEARD ISLAND AND MCDONALD ISLANDS"),
("VA", "HOLY SEE (VATICAN CITY STATE)"),
("HN", "HONDURAS"),
("HK", "HONG KONG"),
("HU", "HUNGARY"),
("IS", "ICELAND"),
("IN", "INDIA"),
("ID", "INDONESIA"),
("IR", "IRAN"),
("IQ", "IRAQ"),
("IE", "IRELAND"),
("IM", "ISLE OF MAN"),
("IL", "ISRAEL"),
("IT", "ITALY"),
("JM", "JAMAICA"),
("JP", "JAPAN"),
("JE", "JERSEY"),
("JO", "JORDAN"),
("KZ", "KAZAKHSTAN"),
("KE", "KENYA"),
("KI", "KIRIBATI"),
("KP", "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),
("KR", "KOREA, REPUBLIC OF"),
("KW", "KUWAIT"),
("KG", "KYRGYZSTAN"),
("LA", "LAO PEOPLE'S DEMOCRATIC REPUBLIC"),
("LV", "LATVIA"),
("LB", "LEBANON"),
("LS", "LESOTHO"),
("LR", "LIBERIA"),
("LY", "LIBYAN ARAB JAMAHIRIYA"),
("LI", "LIECHTENSTEIN"),
("LT", "LITHUANIA"),
("LU", "LUXEMBOURG"),
("MO", "MACAO"),
("MK", "MACEDONIA"),
("MG", "MADAGASCAR"),
("MW", "MALAWI"),
("MY", "MALAYSIA"),
("MV", "MALDIVES"),
("ML", "MALI"),
("MT", "MALTA"),
("MH", "MARSHALL ISLANDS"),
("MQ", "MARTINIQUE"),
("MR", "MAURITANIA"),
("MU", "MAURITIUS"),
("YT", "MAYOTTE"),
("MX", "MEXICO"),
("FM", "MICRONESIA"),
("MD", "MOLDOVA"),
("MC", "MONACO"),
("MN", "MONGOLIA"),
("ME", "MONTENEGRO"),
("MS", "MONTSERRAT"),
("MA", "MOROCCO"),
("MZ", "MOZAMBIQUE"),
("MM", "MYANMAR"),
("NA", "NAMIBIA"),
("NR", "NAURU"),
("NP", "NEPAL"),
("NL", "NETHERLANDS"),
("AN", "NETHERLANDS ANTILLES"),
("NC", "NEW CALEDONIA"),
("NZ", "NEW ZEALAND"),
("NI", "NICARAGUA"),
("NE", "NIGER"),
("NG", "NIGERIA"),
("NU", "NIUE"),
("NF", "NORFOLK ISLAND"),
("MP", "NORTHERN MARIANA ISLANDS"),
("NO", "NORWAY"),
("OM", "OMAN"),
("PK", "PAKISTAN"),
("PW", "PALAU"),
("PS", "PALESTINIAN TERRITORY"),
("PA", "PANAMA"),
("PG", "PAPUA NEW GUINEA"),
("PY", "PARAGUAY"),
("PE", "PERU"),
("PH", "PHILIPPINES"),
("PN", "PITCAIRN"),
("PL", "POLAND"),
("PT", "PORTUGAL"),
("PR", "PUERTO RICO"),
("QA", "QATAR"),
("RE", "REUNION"),
("RO", "ROMANIA"),
("RU", "RUSSIAN FEDERATION"),
("RW", "RWANDA"),
("BL", "SAINT BARTHÉLEMY"),
("SH", "SAINT HELENA"),
("KN", "SAINT KITTS AND NEVIS"),
("LC", "SAINT LUCIA"),
("MF", "SAINT MARTIN"),
("PM", "SAINT PIERRE AND MIQUELON"),
("VC", "SAINT VINCENT AND THE GRENADINES"),
("WS", "SAMOA"),
("SM", "SAN MARINO"),
("ST", "SAO TOME AND PRINCIPE"),
("SA", "SAUDI ARABIA"),
("SN", "SENEGAL"),
("RS", "SERBIA"),
("SC", "SEYCHELLES"),
("SL", "SIERRA LEONE"),
("SG", "SINGAPORE"),
("SK", "SLOVAKIA"),
("SI", "SLOVENIA"),
("SB", "SOLOMON ISLANDS"),
("SO", "SOMALIA"),
("ZA", "SOUTH AFRICA"),
("GS", "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS"),
("ES", "SPAIN"),
("LK", "SRI LANKA"),
("SD", "SUDAN"),
("SR", "SURINAME"),
("SJ", "SVALBARD AND JAN MAYEN"),
("SZ", "SWAZILAND"),
("SE", "SWEDEN"),
("CH", "SWITZERLAND"),
("SY", "SYRIAN ARAB REPUBLIC"),
("TW", "TAIWAN"),
("TJ", "TAJIKISTAN"),
("TZ", "TANZANIA"),
("TH", "THAILAND"),
("TL", "TIMOR-LESTE"),
("TG", "TOGO"),
("TK", "TOKELAU"),
("TO", "TONGA"),
("TT", "TRINIDAD AND TOBAGO"),
("TN", "TUNISIA"),
("TR", "TURKEY"),
("TM", "TURKMENISTAN"),
("TC", "TURKS AND CAICOS ISLANDS"),
("TV", "TUVALU"),
("UG", "UGANDA"),
("UA", "UKRAINE"),
("AE", "UNITED ARAB EMIRATES"),
("GB", "UNITED KINGDOM"),
("US", "UNITED STATES"),
("UM", "UNITED STATES MINOR OUTLYING ISLANDS"),
("UY", "URUGUAY"),
("UZ", "UZBEKISTAN"),
("VU", "VANUATU"),
("VE", "VENEZUELA"),
("VN", "VIET NAM"),
("VG", "BRITISH VIRGIN ISLANDS"),
("VI", "U.S VIRGIN ISLANDS"),
("WF", "WALLIS AND FUTUNA"),
("EH", "WESTERN SAHARA"),
("YE", "YEMEN"),
("ZM", "ZAMBIA"),
("ZW", "ZIMBABWE"),

)
""" 
.. warning:: This is DEPRECATED and is not maintained. Please use other data sources such as django-countries_ or `Umpirsky's Data`_ instead. 

A list of the ISO 3166-2 country codes and country names for convenience. 

.. _django-countries: http://pypi.python.org/pypi/django-countries/1.0.2
.. _`Umpirsky's Data`: http://dev.umpirsky.com/list-of-all-countries-in-all-languages-and-all-data-formats/

"""

# Offset from UTC in seconds, and human readable name
WORLD_TIME_ZONES = (

("-43200", "UTC -12:00 International Date Line West"),
("-39600", "UTC -11:00 Coordinated Universal Time-11"),
("-36000", "UTC -10:00 Aleutian Islands, Hawaii"),
("-36000", "UTC -10:00 Hawaii"),
("-34200", "UTC -9:30 Marquesas Islands"),
("-32400", "UTC -9:00 Alaska"),
("-32400", "UTC -9:00 Coordinated Universal Time-09"),
("-28800", "UTC -8:00 Baja California"),
("-28800", "UTC -8:00 Coordinated Universal Time-08"),
("-28800", "UTC -8:00 Pacific Time (US & Canada)"),
("-25200", "UTC -7:00 Arizona"),
("-25200", "UTC -7:00 Chihuahua, La Paz, Mazatian"),
("-25200", "UTC -7:00 Mountain Time (US & Canada)"),
("-25200", "UTC -7:00 Yukon"),
("-21600", "UTC -6:00 Central America"),
("-21600", "UTC -6:00 Central Time (US & Canada)"),
("-21600", "UTC -6:00 Easter Island"),
("-21600", "UTC -6:00 Guadalajara, Mexico City, Monterrey"),
("-21600", "UTC -6:00 Saskatchewan"),
("-18000", "UTC -5:00 Bogota, Lima, Quito, Rio Branco, Chetumal"),
("-18000", "UTC -5:00 Chetumal"),
("-18000", "UTC -5:00 Eastern Time (US & Canada)"),
("-18000", "UTC -5:00 Haiti"),
("-18000", "UTC -5:00 Havana"),
("-18000", "UTC -5:00 Indiana (East)"),
("-18000", "UTC -5:00 Turks and Caicos"),
("-14400", "UTC -4:00 Ascuncion"),
("-14400", "UTC -4:00 Atlantic Time (Canada)"),
("-14400", "UTC -4:00 Caracas"),
("-14400", "UTC -4:00 Cuaiba"),
("-14400", "UTC -4:00 Georgetown, La Paz, Manaus, San Juan"),
("-14400", "UTC -4:00 Santiago"),
("-12600", "UTC -3:30 Newfoundland"),
("-10800", "UTC -3:00 Araguaina"),
("-10800", "UTC -3:00 Brasilia"),
("-10800", "UTC -3:00 Cayenne, Fortaleza"),
("-10800", "UTC -3:00 City of Buenos Aires"),
("-10800", "UTC -3:00 Greenland"),
("-10800", "UTC -3:00 Montevideo"),
("-10800", "UTC -3:00 Punta Arenas"),
("-10800", "UTC -3:00 Saint Pierre and Miquelon"),
("-10800", "UTC -3:00 Salvador"),
("-7200", "UTC -2:00 Coordinated Universal Time-02"),
("-3600", "UTC -1:00 Azores"),
("-3600", "UTC -1:00 Cabo Verde Is."),
("0", "UTC +0:00 Coordinated Universal Time"),
("0", "UTC +0:00 Dublin, Edinburgh, Lisbon, London"),
("0", "UTC +0:00 Monrovia, Reykjavik"),
("0", "UTC +0:00 Sao Tome"),
("3600", "UTC +1:00 Casablanca"),
("3600", "UTC +1:00 Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna"),
("3600", "UTC +1:00 Belgrade, Bratislava, Budapest, Ljubljana, Prague"),
("3600", "UTC +1:00 Brussels, Copenhagen, Madrid, Paris"),
("3600", "UTC +1:00 Sarajevo, Skopje, Warsaw, Zagreb"),
("3600", "UTC +1:00 West Central Africa"),
("7200", "UTC +2:00 Amman"),
("7200", "UTC +2:00 Athens, Bucharest"),
("7200", "UTC +2:00 Beirut"),
("7200", "UTC +2:00 Cairo"),
("7200", "UTC +2:00 Damascus"),
("7200", "UTC +2:00 Gaza, Hebron"),
("7200", "UTC +2:00 Harare, Pretoria"),
("7200", "UTC +2:00 Helsinki, Kyiv, Riga, Sofia, Talinn, Vilnius"),
("7200", "UTC +2:00 Jerussalem"),
("7200", "UTC +2:00 Kaliningrad"),
("7200", "UTC +2:00 Khartoum"),
("7200", "UTC +2:00 Tripoli"),
("7200", "UTC +2:00 Windhoek"),
("10800", "UTC +3:00 Baghdad"),
("10800", "UTC +3:00 Istanbul"),
("10800", "UTC +3:00 Kuwait, Riyadh"),
("10800", "UTC +3:00 Minsk"),
("10800", "UTC +3:00 Moscow, St. Petersburg"),
("10800", "UTC +3:00 Nairobi"),
("12600", "UTC +3:30 Tehran"),
("14400", "UTC +4:00 Abu Dhabi, Muscat"),
("14400", "UTC +4:00 Astrakhan, Ulyanovsk"),
("14400", "UTC +4:00 Baku"),
("14400", "UTC +4:00 Izhevsk, Samara"),
("14400", "UTC +4:00 Port Louis"),
("14400", "UTC +4:00 Saratov"),
("14400", "UTC +4:00 Tbilisi"),
("14400", "UTC +4:00 Volgograd"),
("14400", "UTC +4:00 Yerevan"),
("16200", "UTC +4:30 Kabul"),
("18000", "UTC +5:00 Ashgabat, Tashkent"),
("18000", "UTC +5:00 Ekateriburg"),
("18000", "UTC +5:00 Islamabad, Karachi"),
("18000", "UTC +5:00 Qyzylorda"),
("19800", "UTC +5:30 Chennai, Kolkata, Mumbai, New Delhi"),
("19800", "UTC +5:30 Sri Jayawerdenepura"),
("20700", "UTC +5:45 Kathmandu"),
("21600", "UTC +6:00 Astana"),
("21600", "UTC +6:00 Dhaka"),
("21600", "UTC +6:00 Omsk"),
("23400", "UTC +6:30 Yangon (Rangoon)"),
("25200", "UTC +7:00 Bangkok, Hanoi, Jakarta"),
("25200", "UTC +7:00 Barnaul, Gorno-Altaysk"),
("25200", "UTC +7:00 Hovd"),
("25200", "UTC +7:00 Krasnoyarsk"),
("25200", "UTC +7:00 Novosibirsk"),
("25200", "UTC +7:00 Tomsk"),
("28800", "UTC +8:00 Beijing, Chongqing, Hong Kong, Urumqi"),
("28800", "UTC +8:00 Irkutsk"),
("28800", "UTC +8:00 Kuala Lumpur, Singapore"),
("28800", "UTC +8:00 Perth"),
("28800", "UTC +8:00 Taipei"),
("28800", "UTC +8:00 Ulaanbaatar"),
("31500", "UTC +8:45 Eucla"),
("32400", "UTC +9:00 Osaka, Sapporo, Tokyo"),
("32400", "UTC +9:00 Chita"),
("32400", "UTC +9:00 Pyongyang"),
("32400", "UTC +9:00 Seoul"),
("32400", "UTC +9:00 Yakutsk"),
("34200", "UTC +9:30 Adelaide"),
("34200", "UTC +9:30 Darwin"),
("36000", "UTC +10:00 Brisbane"),
("36000", "UTC +10:00 Canberra, Melbourne, Sydney"),
("36000", "UTC +10:00 Port Moresby, Hobart"),
("36000", "UTC +10:00 Hobart"),
("36000", "UTC +10:00 Vladivostok"),
("38700", "UTC +10:30 Lord Howe Island"),
("39600", "UTC +11:00 Bougainville Island"),
("39600", "UTC +11:00 Chokurdakh"),
("39600", "UTC +11:00 Magadan"),
("39600", "UTC +11:00 Norfolk Island"),
("39600", "UTC +11:00 Sakhalin"),
("39600", "UTC +11:00 Solomon Is., New Caledonia"),
("43200", "UTC +12:00 Anadyr, Petropavlosk-Kamchatsky"),
("43200", "UTC +12:00 Auckland, Wellington"),
("43200", "UTC +12:00 Coordinated Universal Time+12"),
("43200", "UTC +12:00 Fiji"),
("45900", "UTC +12:45 Chatham Islands"),
("46800", "UTC +13:00 Coordinated Universal Time+13"),
("46800", "UTC +13:00 Samoa"),
("46800", "UTC +13:00 Nuku'alofa, Samoa"),
("50400", "UTC +14:00 Kiritimati Island"),

)
""" 
.. warning:: This is DEPRECATED and is not maintained. Use pytz_ instead. 

A list of timezones and differences in seconds.

.. _pytz: http://pytz.sourceforge.net/

"""

