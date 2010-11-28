* $Id: submicron.inc,v 1.1 2010/05/03 01:33:10 john_doty Exp $
*
*   Copyright (C) 2010 John P. Doty            	 *
*                                                                        *
*   This program is free software; you can redistribute it and/or modify *
*   it under the terms of the GNU General Public License as published by *
*   the Free Software Foundation; either version 2 of the License, or    *
*   (at your option) any later version.                                  *
*                                                                        *
*   This program is distributed in the hope that it will be useful,      *
*   but WITHOUT ANY WARRANTY; without even the implied warranty of       *
*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        *
*   GNU General Public License for more details.                         *
*                                                                        *
*   You should have received a copy of the GNU General Public License    *
*   along with this program; if not, write to the                        *
*   Free Software Foundation, Inc.,                                      *
*   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.            *
*
* Rough model parameters for getting representive results 
* from ngspice using openIP
*
.model nch nmos ( level=51 vth0=0.5 tox=1e-8 cj=1e-3 )
.model pch pmos ( level=51 vth0=-1 tox=1e-8 cj=1e-3 )
* $Log: submicron.inc,v $
* Revision 1.1  2010/05/03 01:33:10  john_doty
* Open-IP models.
*
