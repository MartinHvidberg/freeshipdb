lst_mid = list()

def isallnums(str_in):
    if isinstance(str_in, str):
        bol_true = True
        lst_in = [s.strip() for s in str_in.strip().split(',')]
        for itm in lst_in:
            try:
                num_i = int(itm)
            except ValueError:
                bol_true = False
        return bol_true
    else:
        return False


with open("../data/mmsi_MID_country_codes.txt", "r") as ifile:
    for line in ifile:
        lst_tok = [tok.strip() for tok in line.strip().split('\t') if tok != '']
        #print(lst_tok)
        if len(lst_tok) == 2:
            lst_int = list()
            lst_str = list()
            for tok in lst_tok:
                try:
                    lst_int.append(int(tok))
                except ValueError:
                    lst_str.append(tok)
            if len(lst_int) == 1 and len(lst_str) == 1:
                lst_mid.append((int(lst_int[0]), lst_str[0]))
            else:
                #print("MUL: {}; {}".format(lst_int, lst_str))
                lst_nu = None
                str_st = None
                for itm in lst_str:
                    if isallnums(itm):
                        #print("isallnums: {}".format(itm))
                        lst_nu = [it.strip() for it in itm.strip().split(',')]
                    else:
                        #print("hopeforcn: {}".format(itm))
                        str_st = itm
                if lst_nu and str_st:
                    for nu in lst_nu:
                        lst_mid.append((int(nu), str_st))
        elif len(lst_tok) == 0:
            pass  # Silently skip blank lines
        else:
            print("Line have not 2 elements <{}> : {}".format(len(lst_tok), line.strip()))
del lst_tok, lst_int, lst_str

lst_mid = sorted(list(set(lst_mid)))

for mid in sorted(lst_mid):
    print(mid,',')

print("all: {} unq: {}".format(len(lst_mid), len(list(set([itm[0] for itm in lst_mid])))))

for n in range(len(lst_mid)):
    if n>0 and lst_mid[n][0] == lst_mid[n-1][0]:
        print(lst_mid[n], lst_mid[n-1])

""" /usr/bin/python3 /home/martin/PycharmProjects/freeshipdb/src/mmsi_mdi_code_sorter.py
(201, 'Albania (Republic of)')
(202, 'Andorra (Principality of)')
(203, 'Austria')
(204, 'Azores')
(205, 'Belgium')
(206, 'Belarus (Republic of)')
(207, 'Bulgaria (Republic of)')
(208, 'Vatican City State')
(209, 'Cyprus (Republic of)')
(210, 'Cyprus (Republic of)')
(211, 'Germany (Federal Republic of)')
(212, 'Cyprus (Republic of)')
(213, 'Georgia')
(214, 'Moldova (Republic of)')
(215, 'Malta')
(216, 'Armenia (Republic of)')
(218, 'Germany (Federal Republic of)')
(219, 'Denmark')
(220, 'Denmark')
(224, 'Spain')
(225, 'Spain')
(226, 'France')
(227, 'France')
(228, 'France')
(230, 'Finland')
(231, 'Faroe Islands')
(232, 'United Kingdom of Great Britain and Northern Ireland')
(233, 'United Kingdom of Great Britain and Northern Ireland')
(234, 'United Kingdom of Great Britain and Northern Ireland')
(235, 'United Kingdom of Great Britain and Northern Ireland')
(236, 'Gibraltar')
(237, 'Greece')
(238, 'Croatia (Republic of)')
(239, 'Greece')
(240, 'Greece')
(241, 'Greece')
(242, 'Morocco (Kingdom of)')
(243, 'Hungary (Republic of)')
(244, 'Netherlands (Kingdom of the)')
(245, 'Netherlands (Kingdom of the)')
(246, 'Netherlands (Kingdom of the)')
(247, 'Italy')
(248, 'Malta')
(249, 'Malta')
(250, 'Ireland')
(251, 'Iceland')
(252, 'Liechtenstein (Principality of)')
(253, 'Luxembourg')
(254, 'Monaco (Principality of)')
(255, 'Madeira')
(256, 'Malta')
(257, 'Norway')
(258, 'Norway')
(259, 'Norway')
(261, 'Poland (Republic of)')
(262, 'Montenegro')
(262, 'Montenegro (Republic of)')
(263, 'Portugal')
(264, 'Romania')
(265, 'Sweden')
(266, 'Sweden')
(267, 'Slovak Republic')
(268, 'San Marino (Republic of)')
(269, 'Switzerland (Confederation of)')
(270, 'Czech Republic')
(271, 'Turkey')
(272, 'Ukraine')
(273, 'Russian Federation')
(274, 'The Former Yugoslav Republic of Macedonia')
(275, 'Latvia (Republic of)')
(276, 'Estonia (Republic of)')
(277, 'Lithuania (Republic of)')
(278, 'Slovenia (Republic of)')
(279, 'Serbia (Republic of)')
(301, 'Anguilla')
(303, 'Alaska (State of)')
(304, 'Antigua and Barbuda')
(305, 'Antigua and Barbuda')
(306, 'Netherlands Antilles')
(307, 'Aruba')
(308, 'Bahamas (Commonwealth of the)')
(309, 'Bahamas (Commonwealth of the)')
(310, 'Bermuda')
(311, 'Bahamas (Commonwealth of the)')
(312, 'Belize')
(314, 'Barbados')
(316, 'Canada')
(319, 'Cayman Islands')
(321, 'Costa Rica')
(323, 'Cuba')
(325, 'Dominica (Commonwealth of)')
(327, 'Dominican Republic')
(329, 'Guadeloupe (French Department of)')
(330, 'Grenada')
(331, 'Greenland')
(332, 'Guatemala (Republic of)')
(334, 'Honduras (Republic of)')
(336, 'Haiti (Republic of)')
(338, 'United States of America')
(339, 'Jamaica')
(341, 'Saint Kitts and Nevis (Federation of)')
(343, 'Saint Lucia')
(345, 'Mexico')
(347, 'Martinique (French Department of)')
(348, 'Montserrat')
(350, 'Nicaragua')
(351, 'Panama (Republic of)')
(352, 'Panama (Republic of)')
(353, 'Panama (Republic of)')
(354, 'Panama (Republic of)')
(355, 'Panama (Republic of)')
(356, 'Panama (Republic of)')
(357, 'Panama (Republic of)')
(358, 'Puerto Rico')
(359, 'El Salvador (Republic of)')
(361, 'Saint Pierre and Miquelon (Territorial Collectivity of)')
(362, 'Trinidad and Tobago')
(364, 'Turks and Caicos Islands')
(366, 'United States of America')
(367, 'United States of America')
(368, 'United States of America')
(369, 'United States of America')
(370, 'Panama (Republic of)')
(371, 'Panama (Republic of)')
(372, 'Panama (Republic of)')
(375, 'Saint Vincent and the Grenadines')
(376, 'Saint Vincent and the Grenadines')
(377, 'Saint Vincent and the Grenadines')
(378, 'British Virgin Islands')
(379, 'United States Virgin Islands')
(401, 'Afghanistan')
(403, 'Saudi Arabia (Kingdom of)')
(405, "Bangladesh (People's Republic of)")
(408, 'Bahrain (Kingdom of)')
(410, 'Bhutan (Kingdom of)')
(412, "China (People's Republic of)")
(413, "China (People's Republic of)")
(416, 'Taiwan (Province of China)')
(417, 'Sri Lanka (Democratic Socialist Republic of)')
(419, 'India (Republic of)')
(422, 'Iran (Islamic Republic of)')
(423, 'Azerbaijani Republic')
(425, 'Iraq (Republic of)')
(428, 'Israel (State of)')
(431, 'Japan')
(432, 'Japan')
(434, 'Turkmenistan')
(436, 'Kazakhstan (Republic of)')
(437, 'Uzbekistan (Republic of)')
(438, 'Jordan (Hashemite Kingdom of)')
(440, 'Korea (Republic of)')
(441, 'Korea (Republic of)')
(443, 'Palestine (In accordance with Resolution 99 Rev. Antalya, 2006)')
(445, "Democratic People's Republic of Korea")
(447, 'Kuwait (State of)')
(450, 'Lebanon')
(451, 'Kyrgyz Republic')
(453, 'Macao (Special Administrative Region of China)')
(455, 'Maldives (Republic of)')
(457, 'Mongolia')
(459, 'Nepal')
(459, 'Nepal (Federal Democratic Republic of)')
(461, 'Oman (Sultanate of)')
(463, 'Pakistan (Islamic Republic of)')
(466, 'Qatar (State of)')
(468, 'Syrian Arab Republic')
(470, 'United Arab Emirates')
(473, 'Yemen (Republic of)')
(475, 'Yemen (Republic of)')
(477, 'Hong Kong (Special Administrative Region of China)')
(478, 'Bosnia and Herzegovina')
(501, 'Adelie Land')
(503, 'Australia')
(506, 'Myanmar (Union of)')
(508, 'Brunei Darussalam')
(510, 'Micronesia (Federated States of)')
(511, 'Palau (Republic of)')
(512, 'New Zealand')
(514, 'Cambodia (Kingdom of)')
(515, 'Cambodia (Kingdom of)')
(516, 'Christmas Island (Indian Ocean)')
(518, 'Cook Islands')
(520, 'Fiji (Republic of)')
(523, 'Cocos (Keeling) Islands')
(525, 'Indonesia (Republic of)')
(529, 'Kiribati (Republic of)')
(531, "Lao People's Democratic Republic")
(533, 'Malaysia')
(536, 'Northern Mariana Islands (Commonwealth of the)')
(538, 'Marshall Islands (Republic of the)')
(540, 'New Caledonia')
(542, 'Niue')
(544, 'Nauru (Republic of)')
(546, 'French Polynesia')
(548, 'Philippines (Republic of the)')
(553, 'Papua New Guinea')
(555, 'Pitcairn Island')
(557, 'Solomon Islands')
(559, 'American Samoa')
(561, 'Samoa (Independent State of)')
(563, 'Singapore (Republic of)')
(564, 'Singapore (Republic of)')
(565, 'Singapore (Republic of)')
(567, 'Thailand')
(570, 'Tonga (Kingdom of)')
(572, 'Tuvalu')
(574, 'Viet Nam (Socialist Republic of)')
(576, 'Vanuatu (Republic of)')
(578, 'Wallis and Futuna Islands')
(601, 'South Africa (Republic of)')
(603, 'Angola (Republic of)')
(605, "Algeria (People's Democratic Republic of)")
(607, 'Saint Paul and Amsterdam Islands')
(608, 'Ascension Island')
(609, 'Burundi (Republic of)')
(610, 'Benin (Republic of)')
(611, 'Botswana (Republic of)')
(612, 'Central African Republic')
(613, 'Cameroon (Republic of)')
(615, 'Congo (Republic of the)')
(616, 'Comoros (Union of the)')
(617, 'Cape Verde (Republic of)')
(618, 'Crozet Archipelago')
(619, "Côte d'Ivoire (Republic of)")
(621, 'Djibouti (Republic of)')
(622, 'Egypt (Arab Republic of)')
(624, 'Ethiopia (Federal Democratic Republic of)')
(625, 'Eritrea')
(626, 'Gabonese Republic')
(627, 'Ghana')
(629, 'Gambia (Republic of the)')
(630, 'Guinea-Bissau (Republic of)')
(631, 'Equatorial Guinea (Republic of)')
(632, 'Guinea (Republic of)')
(633, 'Burkina Faso')
(634, 'Kenya (Republic of)')
(635, 'Kerguelen Islands')
(636, 'Liberia (Republic of)')
(637, 'Liberia (Republic of)')
(642, "Socialist People's Libyan Arab Jamahiriya")
(644, 'Lesotho (Kingdom of)')
(645, 'Mauritius (Republic of)')
(647, 'Madagascar (Republic of)')
(649, 'Mali (Republic of)')
(650, 'Mozambique (Republic of)')
(654, 'Mauritania (Islamic Republic of)')
(655, 'Malawi')
(656, 'Niger (Republic of the)')
(657, 'Nigeria (Federal Republic of)')
(659, 'Namibia (Republic of)')
(660, 'Reunion (French Department of)')
(661, 'Rwanda (Republic of)')
(662, 'Sudan (Republic of the)')
(663, 'Senegal (Republic of)')
(664, 'Seychelles (Republic of)')
(665, 'Saint Helena')
(666, 'Somali Democratic Republic')
(667, 'Sierra Leone')
(668, 'Sao Tome and Principe (Democratic Republic of)')
(669, 'Swaziland (Kingdom of)')
(670, 'Chad (Republic of)')
(671, 'Togolese Republic')
(672, 'Tunisia')
(674, 'Tanzania (United Republic of)')
(675, 'Uganda (Republic of)')
(676, 'Democratic Republic of the Congo')
(677, 'Tanzania (United Republic of)')
(678, 'Zambia (Republic of)')
(679, 'Zimbabwe (Republic of)')
(701, 'Argentine Republic')
(710, 'Brazil (Federative Republic of)')
(720, 'Bolivia (Plurinational State of)')
(720, 'Bolivia (Republic of)')
(725, 'Chile')
(730, 'Colombia (Republic of)')
(735, 'Ecuador')
(740, 'Falkland Islands (Malvinas)')
(745, 'Guiana (French Department of)')
(750, 'Guyana')
(755, 'Paraguay (Republic of)')
(760, 'Peru')
(765, 'Suriname (Republic of)')
(770, 'Uruguay (Eastern Republic of)')
(775, 'Venezuela (Bolivarian Republic of)')
(970, 'Search and Rescue Transmitter')
"""