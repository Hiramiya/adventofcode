import re
input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input = r"@][mul(345,766);'(^mul(343,555)mul(532,723)'>mul(810,622)mul(163,901)select()@?who()select(643,43)'mul(598,56)#;do()from()~where()mul(905,791)select()/why()-when()~;mul(767,89)[#?&mul(874,668)!what(334,491):@@don't()#what()+{}who()mul(746,753)how()~+! -select(814,465)&mul(961,917)$!}?who()from(239,902)]mul(578,658);~' ]mul(693,262)~;mul(830,470)<%mul(310,717)what()when(392,442) :#${@mul(73,255)mul(673,551)+$[from(780,580)-mul(774,338)*:why()do()what(), >{* select()^mul(802,740)[#*mul(243,183)&don't()mul(806,801)from())where()(who()}>-mul(56,431):{,@/,<#mul(399,880)}how()what()~mul(512,540)}**,where()do()when()??what()>$*mul(365,444)who()]*where()> ^?%mul(114,504)what()who()~from()where()<select()^]why()mul(487,601)-from()>):who()how()<<:mul(953,560)mul(174,660)why()$#~mul(802,446)]from()?*%mul(306,304)who()where();mul(241,492)from()who()why()~from()&<?mul(299,824)]#>where()&[?+}who()mul(870,405)!mul(422,189)+]'what(588,411)select(58,996)mul(276,921)!why()#what(937,725)(where()mul(913,207){select() from()%[{}?;mul(818,262)&/]]what()'+?~&mul(440,835)?$)what()**(mul(347,140)%+mul(12,361) )what()@-mul(432,576)^@why()*#{*when()how()$do()@!*}:-'/~mul(310,592)&&&-:mul(492,471):{:mul(834,524)who()why()when()who())&$mul(234,340)[?<mul(891,396)/,what()when()&mul(142,532)&select()$what()!}^$from()mul(374,447)#+/>;where(){$~mul(155,220)&&mul(721,750)<*#mul(778,260)%,:$why()} what()select(){mul(777,312)@)what()~select();-mul(623,101))&:/]!-mul(127,361)[)%mul(139,822)mul(465,869)mul(677,898):{)'~mul(240,110)/who()mul(994,931)mul(449,745)?select()/what(),]/:mul(217,696)what()!mul(221,836)^^;where(481,276)mul(871,646)]^)(^select()!mul(649,851)why()>how()do()?;why()#what()how()mul(203,549)--^what())$:%~[mul(566,723)@,@when()@{mul(71,88)who()[{?mul(680,450)where()$select(838,381)?^from()mul(43,229))mul(715,689)what()*+who()%:select()mul(244,492)^what()!~ ([~[mul(114,868)what()~#when()+?mul(57,122)[?%[, mul(569,552)',<why()how()[mul(155,379)/how()#why()%]&mul(398,270)<#mul(249,749)who()mul(467,243)/!? >:don't()from()where()select()%who()!,[mul(760,25){~'<mul(993,817)#}(mul(884,716)#[%what()>?do();]]&when()who(439,358)how()mul(352,496)how(859,494)-<who()(-/?*don't()$)+'^*from(),how()$mul(412,194)/select()*mul(686,354)%what())^)from()$:select()don't()?;mul(452,313):mul(920,484){{who(437,704)what()#mul(751,237)^why(621,492)$;+when())mul(701,219)@{@who()mul(54,852))why(824,327)mul(117,489) why())'@<how()select()mul(763,475)%+where()@what()%>what()$,mul(986,853)((mul(43,897)who())+$;&mul(207,469)]^/mul(237,787))!when()'@+what()?]mul(542,157)mul(466,974)how()^+!!-[#[why()mul(678,165)[(:}#'*-!mul(616,117)select()mul(904,600)![why():)who(),$who(904,821)<mul(438,773):what()>/what(116,194)what()why()mul(720,13)mul(18?/^where()-mul(468,137)}$^(mul(990,391)mul(284,783)select()*how()%>mul(788,482)}#why()mul(211,898)where(24,695)-$mul(237,249):/@+@+mul(280,976)what()what(688,228)when()what()~from()?,/mul(920,121@?]^^mul(102,138)] :}when()&#~mul(171,496)-!mul(775,530)what(40,18)>[why()mul(178,21)mul(533,267)]&,<~-mul(576,4)*<@how()select()what():!mul(436,336)*what()where()>&who()$mul(463,367)mul(102,156)~mul(304,732)mul(970,264)({how()what(27,23)-'do()$*why()(what(932,987)#where()mul(807,956)&:((@()mul(773,746)-'where(); mul(445,526);who())why()^how()how()how()mul(420,885)]){mul(588,810&;how()!~don't()-&&)from()(<{from()%mul(138,683)$>why(707,353)<!mul^-from(),/select()*'$mul(479,204)!,,}%<mul(561,563)#mul(603,943)+({when()?(^ mul(406,737)how()>:how(){%+mul(152,58),((?!:+$ mul(43,304)+mul(715,799),what(),when()select()>select()mul(844,292)@:,'mul(900,791)[;#when()@]%mul(896-:'%>mul(123,811)when()where()why()*>]what(768,291)from()(/mul(612,112)mul(320,45))~&where()((who(68,102),mul(263,865)*why():><>%mul(628,402)don't(); $@how()!^: mul(947,979){-/(-mul(441,144)*;select(599,589)${why()-mul(103,568)}who()what() how()}how()<]mul(239,536)[*mul(537,157)how(640,298)how()@%)who()*mul(142,857) >from()!when()/*how(830,843)mul(199,630)select()do()*>/mul(63,689)$-/[;[when()why()mul(216,315)^where(),mul(181,124)why()%mul(696,385)~~;who()!][:}~mul+<mul(908,253)what()#mul(998,882)what(),+who()what(799,26)'%how()select(753,464)%mul(783,492)who()how();who()mul(863,499)when() ^~<;mul>*?[}{[?'mul(23,341)[select()}%what();who()-from():mul(655,135)^from()&~^how(),mulwhat()mul(661,325)mul(394,949)!$?&^where()'from()mul(564-*?$<do()/]@/!~'~mul(930,22)from(),[':who()who()&mul(891,111)#!#}do()mul(475,603)what():>-[mul(325,618);<from()&how(){<where()!mul(368,116)/mul(713,694)from()!^$}@~mul(231,596);]$/select()&mul(921,63)# %!mul(699,968)what()-]}where(909,380)what(529,893)mul(595,548)select()why()]?+why();~mul(863,866)mul(819,205)+why() ^~^do(){why()<^])where()when()<mul(947,557)what(841,423){mul(566!&'where()when()#how()*from()mul(595,561) ,<mul(766,730);?+?!mul(969,292);when())mul(808,242)where()($;>,]??mul(241,786)@!(,mul(395,180)(%)(%mulwhy(880,593)mul(543,182)!:'}why()what()from(75,377)/mul(242,439)^what() mul(211,696where()?@don't())how()/who()'how()~mul(487,649){{mul(761,854)?!mul(402,396)where()((who()why()don't()!:}{<+-mul(51,725)@where()from()>+{<%;-mul(471%/!from()$)-when()-;mul(468,893)mul(779,665)/what())&^-/mul(82,47)(/$how()[<<#@mul(966,718)]%mul(613,225);select()&%:~%&mul})[from(),[when(43,235)$}mul(635,416)?;%'~who()select(795,993)-mul(729,69)@[mul(754,156)>#]who()%from())what()mul(331,744))mul(536,505)>who() mul(270,727)from()+select()@mul(584,914)^what(188,788)what()mul(770,597)mul(566,371)<{{!}where()mul(431,257)~%{;/[don't()!mul(441,879))select()+~[why(206,654)+&mul(675,232)why(){who()+#how()where()when()mul(803,318){:mul(193,950)$when()?}}mul(850,957)<mul(280,994)@~}#from(642,549)mul(623,577)]why(156,208):mul(942,320)what():mul(795,192))who()'why()mul(602,200)){~!( <mul(429,600)-[where()when()!what()&{^do()<mul(60,862)&}select()-[what()mul(175,546)#how()+<&+mul(65,656)from()}-from()who(239,913)mul(367,375@-&mul(898,626)*&why(),~mulselect()%%when()^^;why()from()mul(705,654)~mul(188,25){')how()select()),who(){select()mul(456,326)who()how()[-<when()>*:~mul(481,93)mul(473,855)mul(714,653):&'mul(98#mul(23,988)who()mul(561,251),@^){?&&mul(315,596)!'why()?,  mul(151,933)]who()mul(883,474)$$#where())who()select())don't()why()where(),mul(41,669)! 'why()< mul(73,433)*[what(985,767)<]when()mul(258,921):}from(88,48)from()>~&:]mul(106,615)%(why();~what()[mul(278,729^'[^how()'<mul(963,821)@{$mul(828,159)#,?/mul(423,306)mul(455,647)how(){mul(551,989)]({}who(317,172)&<!mul){mul(785,154)when(734,601)+%^:when()mul(952,124>/!$ $don't() @-where()-$mul(748,984)when()#mul(366,193]where()$(#[mul(650,149); /when()${(mul(386,30)+,/$$$!^$don't() {how()mul(903,99)&/mul(992,909);}-/$'who()when()don't()from()~where())~mul;#who()why()mul(944,954):)#:> ]when()';mul(953,447{+]what()<mul(110,797)what(753,191)#how()don't(),;%[#$how(540,44):[mul(34,388)-%$mul(202,605)(where()where()*why()@)from()},do()#why():;why()mul(209,331)($&select(){don't()!)~what()select()+ }@*mul(132,620)select()}%;mul(555,449)<mul(187,685),~)mul(309,129):mul(152,923)mul(281,513)!~do()select(906,30)when()%/^},#who(18,247)mul(566,845)>-?'(')]when()mul(256,864)mul(359,893)mul(715,923,where()why()why()where(163,418)>^mul(550,432)&<mul(199,811)mul(293,689)()from()mul(298,628)>what()who()where()[@where()why()mul(412,403/{*;#-)&do()what():mul(228,774)&</<how()[<don't()}where()how()~}?<select()mul(351,71)&-from(714,406)@]where()when(416,192)&mul(427,424)!^$/!:mul(732,189):from(464,399)]where()'^#[why()-don't()how()@%':-mul(993,862)(mul(413,474)<-why()mul(388,540):@)/>[mul(386,547)+{from()mul(259,966) )#,/*select()+where()mul(59,320)!who()select()]mul(837,608)when()mul(862,367)where()where()*+)!:-:mul(639,867)?#-/from()<~do();!^@]>>mul(417,713)]why()*mul(751,602)%)mul(731,827)^(!mul(302,377)&!:)$>mul(814,103who()/]$mul(658,242)mul(393,286)(~{{who():-}[mul(143,747)$mul(654,923)when()when())@<-&from()mul(412,619)%'>mul(94,395)^where(36,302)mul(543,140)mul(894,717),where()who()~why()mul(194,32)( !where()how();^mul(952,751)*mul(564,368)&how(35,521)how()[::;:mul(578,119)^why(849,522)%when()?when()why()}mul(257,172)who()who()where()what()from()#>#what()mul(460,165)where()what()select()when()}select()when()!!select(258,759)mul(322,660)/]what()[%mul(341,188)<)(-^who()<mul(365,476) /what(100,508)}{)who(656,338)?mul(411,895)(*;> don't()%*mul(179,768)from()}>mul(633,949)&why()}mul(986,569)from()<select()select()+mul(562,736>(!why()select();mul(973,414)? 'from()how():@from()(mul(904,727)]why()]+mul(201,762)(how()who()what()how()(^mul(903,105)-+how()~?!+mul(344,148)##-mul(921,159)<$from()?--mul(885,837);,]why()from()*select()[who()/mul(542,794):{from()how() ^,mul(511,377)>:why():) when()}*when()mul(991,899)<(/+when())mul(244,653)%where(),where()why()(who()-mul(864,493)~where(645,381)who()where()mul*%)what()mul(585,982)](~mul(104,216)mul-]%select(573,835)>/-mul(888,953), ? !mul(969,193)who()how()^[when()who()%do()$,{%:()#mulwhy()%'+,}/how()-~when()mul(351,397)!;+ @^&mul(591,394)mul(581,992)from(){#)when()/ don't():}select()mul(833who(),when()how()*;when()mul(366,958)mul(41,963)mul(653,973);from()]-mul(902,82)mul(230,836)-when()[when()select()}mul(265,919);mul(748,89)!mul(3,621) ]](don't(){%:;,~&mul(378,465)}@>&mul(637,901)where()~@don't()[<;@>@<^mul(138,394)#!/usr/bin/perl]who();]})mul(356,794))*/}&{mul(151,94):who()!!!~mul(92,956)mul(188,489)!mul(52,932select(),where()select()$@@[;-do()#%]%:from()&why()mul(416,222)mul(78,182)%who()>{where()+;how()!@mul(456,135)('{how() ),~mul(469,864)$where()select()<#%?;mul(80,492)@][;<)?mul(970,872)-!~>$mul(989,699)where()<*~mul(998,127)mul(246,169)>,&,mul>(mul(564,254)?')from()-why()select()&mul(585,28){++select()who()who()!select()mul(105,926)~{)/@$#?mul(903,224)<where()%what()*!how()-mul(419,745)why()+-~:mul(555,225)mul(768,455){,~##? :how()mul(757,49)<do()>what()mulwho()<(mul(377,343),#+mul(731,518)/]~mul(104,159)<[ mul(864,248):^~[$;do()mul(671,810)from()(mul(373,295)-mul(612,243)*'why()'#mul(517,385)%-'mul(569,660)mul(149,268)why()mul(763,824)]^}!:[mul(432,368)mul(355,593)mul(325,34)%#,}(+mul:%select()-%%;why(),(mul(601,765)&%-//where()from()<don't()} >select()what(),;-mul(174,657~ where():when();&mul(818,690)%)  'how()mul(444,450)(mul(811,633)don't();~&/<from()!what()-mul(575,620)]what()&mul(785,442)'mul(728,359)mul(524/mul(837,37)~></[*;select()mul^$!/+#-{# mul(396,139)]<}[<mul(515,392)($$},{mul(390%%;what()[(*why(836,852)what()mul(209,850)@select(396,328)[select(95,951)who()do()$where(),select()';'& mul(566,669)/:,what()$; mul(859,210)what()/{where(285,363)?%mul(874,799):(]?,where(603,204)select()mul(757,524]'who()when()mul(328,112)]&~//^-!do()what()<#mul(576,717))/%#]$?(^!mul(985,658)*mul(437,756)~don't():(#where();}mul(328,143)?,$mul(861who()]'~*#when(383,63)]>mul(41,34)why()! } >,mul(657,550)mul(341,872) #when()>+/why()&what()don't()*mul(805,568)&}!(#>-@(&mul(938,730)-(,?mul(509,112)?select()+?how()mul(765,701)(-where() what()how(){mul(800,467)[]/mul(401,967)/ +<&*]mul(152,480)do()??why()select()select()&mul(367,114)-mul(857,679)%&@>#mul(710,252)how()<;select(71,168)(^[*mul(106,321)'<>/[what()mul(393,583)mul(733,744)<how(864,645)%;-when()who()when()mul(330,43)mul(79,29<:{%??})&mul(536,145)})where()mul(660,501)--/mul(859,387)'mul(548,10)from()/^,,}what(246,153){when()mul(199,787)how()^'do()' mul(197,500)#where()^/^{$? }mul(709,951)-!<;mul(225,263)^when()#select()what(246,578)^#mul}$from()-mul(771,673)what()<[what()when()%,:,mul(746,291)how(){'mul(887,752)mul(727,513)[ /+}where()?~'*mul(369,667)'{why()[,when()'))~mul(249,441)from()why()(&where()!])what()]mul(999,876)[^+]where()^<[?mul(186,379)mul(417!mul(806,263)#;how() mul(350,362):select());{{:don't()how()mul(426,218)&mul(976,892)-$ *who()from()mul(827<how())select(),;@~~select()>mul(731,76)]?what()$&select()mul(163,611)+})mul(44,657)%+}(when()mul(326,630)mul(316,4)mul(102,24)/^)when():~#%@{mul(586,357)*<;why()-where()~mul(830,113){#when()mul(854,851)-where()from()from()!',@mul(884,829)]-?$%-!who()mul(634,11)/when()mul(940,730)}who();+select()<<@mul(315,377)&:mul(947,179)}^<,&who(954,59)/'mul(354,837),select()from(266,967)['*mul(718,126)$ @*)why()mul(392,406)%*{select():from()[%why()mul(667,160)&%,(who(954,354)/where(){<why()mul(792,751)';+$mul(477,277)}how()@!mul(397,838)from()how(338,380)mul(354,318)from())]why()mul(856,992)mul(884,933)mul(772,762)-where()select()/why()?mul(231,313)#@/^>!^mul(673,986)>;what()$select()mul(782,955)!how()mul(922,151)?why()<??how()~#/mul(666,118)from()@]mul(805,688)+where()why():),who()[):do()% ^){+how():mul(429,343)why()mul(31,538),~what()<^when(),when()mul(707,82)/where()}'mul(299,492)!~mul(668,532)why()mul(292,49):,why(784,47)how()]>]-^from()mul(473,251)when()$';~?%<select():mul(999,765)/()when()~why()mul(177,860)>]what()?+;#{what()mul(488,503)^select()?do()from()when(),^!mul(85,942)-}}mul(227,390)mul(270,642) #where()#?-why()mul(843,712)mul(853,87)what()'!who(682,875);,mul(132,10)??when()select()[%mul(440,436)how()>>^mul(332,464)$':;]~>](from()mul(251,318)why()mul(540,277)who())where()' &}] mul(937,405)>->mul(898,676)what()<where()/@)+what(635,885)}<mul(775,987)]mul(48,384)]$,-&$+mul(204,140)'mul(376,711)(&#<]+,#//mul(149,506)(who(851,170)?)&$-@'mul(192,996)-,<~mul(880,535)@when()*~where()when()^(mul(423,263)mul(866,358)mul(797,13)why(614,141) ~*-how()where();when()&mul(826,995)who()/]what()-,@how()mul(59,148))?select()when()(from();%don't()}# ?mul(645,651)]->when() +)<>@mul(796,954)^;$$when(752,554){mul(28,311)@!;)what()>+don't() }%where()'>mul(903,227)+@??+!mul(624,625)/>from()<:-what()@mul(216,114)&>select()mul(743,469)?where(956,943):];%from()do()&when(){from()@why()how()mul(611,802)where()why()[mul(561,982)who() *@from()'(<(mul(207,619)]$+mul(846,461)what()what():mul(552)-how()^/why()mul(163,195)-)mul(753,176)what()~mul(910,478)mul(209,230)&:mul how()+)select()don't()where()mul(106,878)~how()how()^'+[who()mul(86,13),mul(200,412)mul(285,237)when(){/,how()!'@mul(308,309)(#?select()(>!who()who()&mul(880,171)where(264,559)where()>where()do()what()+[(}where(259,87):!mul(709,722)how()>{who()$*>mul(527,907)from()how();:mul(670,931)%)'mul(855,264)*,>~{mul(548,28)((mul(599,821),}where()from()from()when()]?<when()mul(878,559)why():+%{don't()},<) ;how()'why()mul(994,645)<!mul(209,67)$$^?when()#@how()*mul(349,78);?<{mul(225,901)# ;/when(949,975)$;>-mul(818,682) why()when()^#~ 'how()mul(152,639)@<why()'@when(),*do()mul(177,655)&%:/*mul(600,255);'how(663,924)& [/,mul(5,953)&select()who()'}-!$mul(900,307)from()%*>^from(216,399)~who()mul(441,246)?:'<+#mul(763,310)don't()-'mul(289,172)from()'(!don't()~]^(where()&mul(218,233)mul(390,203';mul(535,511)who():}mul(685')(mul(922,128)$$mul(451/from(758,307)#:]/#mul(203,808)-#,-what(535,949):do()from(917,83)[ why()from()why()mul(338,424);who()what()+mul(170,324)how()mul(895,778)<^ 'when() where()>what()%mul(591,815)~how()who()mul(11,111)(~why()<}:why()mul(416select(550,793)select()&@] #what()mul(229,407)don't()when()what()}from()+(;when()(mul(18,891)-*+{where()do()#mul(435,135),>what()^^~when()*?when(791,112)mul(368,920)$/select()where()#/&what()mul(351}&)%from()mul(930,157)how()where()>who()<])mulwhen()}mul(682,770)from()%/:](mul(537,172); },what();!{&mul(289,489)>@ ;] where()mul(576,338)?~*~%{mul(854,88)&what()mul(726,742)who(32,67)why()@(mul(768,203)@when(23,700)what()/mul(468,338)!-<%>>^/~!mul(543,650)[<*<((mul(528,681);?*$-when()> }%mul(746,92)from(327,471))mul(189,783)(:,(+how()@*mul(560,503):<mul(372,250)&*!<%why();when()mul(223,496)mul(975,639)!%*where()how()#{why()mul(457,568)when()]how()don't()!(?>&;$mul(324,880)why(){who()mul(70,798)~{mul(465,724)!+how())%~mul(85,858)why(520,207)from()&-when()[mul(951,807)'& !mul(678,463)?select(439,910)[%?mul(971,903)where()<~}){)*[mul(712,760)%how()*!!%mul(752,188)'when(729,35)mul(428,573){-~(,;why()mul(461,956)where()mul(456,895:,from())mul(353,754)<( *mul(141,974)why()why(){mul(497,471)]+~[why()mul(115,659)^@mul(662,675)$[}-?@&mul(34,6)why()mul(941,440)$what()%select()when()mul(103,793);why()>?when()what(){from()?why()mul(999,411)['}[~?& how()mul(487,886)  :how()@{mul(41,651)mul(392,297)mul(681,343)@&)/how(692,299)who()/*$do()$mul(326,461)-how()>when()(when()do()';~what()why()* *select(839,422)mul(747,631),when()what() )@*don't()what();from()mul(358,222)]mul(100,430)when()+select()(!:,{who()#mul(761,79)*^mul(701,138))from()?,how()mul(389,248)]:-(#?select()+how()}do()[?when())from()>(mul(403,415)why()don't()when())*mul(31,786){mul(219,86)mul(360,469)when()from()$}/why()mul(851,189)*from()()from()? :!who()mul(746,316)(what()~!+-[#select()when()mul(714,622)!:~select()how()#&when()mul(222,991),/<where()mul(830,780)from())mul(57,161)#select()]where()mul(306,589)mul(498,365)/{select(887,432)![select()why()from()when()mul(581,239)how() how()&-?-@what()]mul(238,608)+/!]why() how()what()-mul(951,639)how()?~what()how()~''/who()mul(932,194)what()/(mul(391,952)$(% when()when()$]mul(392,789)^select()+mul(851,332)'{why()&%!^:mul(925,423)}[mul(541,179)%&:what()who()mul(123,427)how()])mul(159,908),$mul(917,718)how()(@]/where()~<mul(140,59)&$+]'%)how(162,710)mul(433,609){:mul(133,858)+-who()??}$select()%#mul(367,417)mul(517,827):mul(128,355)@'@->where()select()mul(389,819)where()*<mul(408,435)>what()/do()<&^{$mul(218,540)select()how();& ~where();%mul(593,988)where()},mul(277,30)#]+}mul(896,116)mul(59,615)who())do()!-why()?:when()>>when()mul(367,136)why()##what()what()mul(185,184)$~)+[what() mul(225,500)*why()what()'+who())}mul(178,560)select() when()don't()why())>+}>why(),>,mul(514,558)'?< >-'?,mul(36,747){~-why()?)who()~:mul(287,362)&mul(32,838)how()from()#when()what()%;who()mul(62,989)mul(199,673){*~mul(315,155)!where()$why()?:mul(10,649))'-{'mul(629,27)&#)'[who())!mul(195,137)%,what()~#}who()mul(606,783)!mul(481,349){mul(28,389)mul(628,171)<!]~>why()mul(208,827)?}{~why():why()don't()&,from()why()/%mul(735,558)@<%; where()select()+mul(178,387)+:>~?#where()-how()^mul(565,609)#$,why()<{^+:mul(130,74)from(815,775)){/#what(60,600),>where()#mul(347,919)what():/mul(377,21)>>@'^where()@/mul(395,896)who()/~{what(347,8)#(mul(335,630)/<select()who()]mul(932,564):,*}mul(180,332)mul(988,195)/how()~~)($^:"

parsedish = [x.split(")")[0] for x in input.split("mul(")]

p1_total = 0

for val in parsedish:
    try:
        v1, v2 = map(int,val.split(",",1))
    except:
        continue

    p1_total += (v1 * v2)

print("p1", p1_total)


p2_total = 0
regex_ex = re.finditer(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", input)
newlist = list(map(re.Match.group, regex_ex))

should_skip = False
for command in newlist:
    if command.startswith("mul(") and not should_skip:
        v1, v2 = map(int, command.replace("mul(","").replace(")","").split(","))
        p2_total += (v1 * v2)
        continue
    
    if command == "don't()":
        should_skip = True
    elif command == "do()":
        should_skip = False

print("p2", p2_total)