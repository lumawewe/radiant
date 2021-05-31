from app.models import db, Product

def seed_products():
  product1 = Product(
    product_name='Papaya Sorbet Smoothing Enzyme Cleansing Balm & Makeup Remover',
    brand_name='Glow Recipe',
    skincare_step='Cleanse',
    target='Dullness, Uneven Texture, Pores',
    description='A PEG-free cleansing balm that smooths the look of skin with natural papaya enzymes, while melting away stubborn makeup, dirt, oil, and SPF.',
    ingredients='Cetyl Ethylhexanoate, Sorbitan Oleate, Prunus Armeniaca (Apricot) Kernel Oil, Polyethylene, Aqua/Water/Eau, Camellia Japonica Seed Oil, Carica Papaya (Papaya) Seed Oil, Carica Papaya (Papaya) Fruit Extract, Papain, Vaccinium Angustifolium (Blueberry) Fruit Extract, Fragaria Ananassa (Strawberry) Fruit Extract, Alkanna Tinctoria Root Extract, Capsicum Annuum Fruit Extract, Maltodextrin, Caprylic/Capric Triglyceride, Levulinic Acid, Pentylene Glycol, Sodium Metabisulfite.',
    img_url='https://www.sephora.com/productimages/sku/s2371516-main-zoom.jpg?imwidth=1224'
  )

  product2 = Product(
    product_name='Green Clean Makeup Removing Cleansing Balm',
    brand_name='Farmacy',
    skincare_step='Cleanse',
    target='Dullness, Uneven Texture, Dryness',
    description='A makeup remover and face cleanser that virtually melts away all makeup, leaving skin hydrated and silky smooth.',
    ingredients='Cetyl Ethylhexanoate, Caprylic/Capric Triglyceride, Peg-20 Glyceryl Triisostearate, Peg-10 Isostearate, Polyethylene, Echinacea Purpurea Root Extract, Carica Papaya (Papaya) Fruit Extract, Moringa Pterygosperma Seed Extract, Moringa Oleifera Seed Oil, Zingiber Officinale (Ginger) Root Oil, Helianthus Annuus (Sunflower) Seed Oil, Sorbitan Sesquioleate, Citrus Aurantifolia (Lime) Oil, Citrus Aurantium Bergamia (Bergamot) Fruit Oil, Glycerin, Melia Azadirachta Leaf Extract, Melia Azadirachta Flower Extract, Corallina Officinalis Extract, Citrus Aurantium Dulcis (Orange) Peel Oil, Amber Powder, Cananga Odorata Flower Oil, Coccinia Indica Fruit Extract, Solanum Melongena (Eggplant) Fruit Extract, Curcuma Longa (Turmeric) Root Extract, Ocimum Sanctum Leaf Extract, Water, Butylene Glycol, Disodium Phosphate, Citric Acid, Phenoxyethanol, Citral, Limonene, Linalool.',
    img_url='https://www.sephora.com/productimages/sku/s1899103-main-zoom.jpg?imwidth=1224'
  )

  product3 = Product(
    product_name='The Rice Wash Skin-Softening Cleanser',
    brand_name='Tatcha',
    skincare_step='Cleanse',
    target='Dryness',
    description='A PH-neutral, daily cream cleanser that gently washes away impurities without stripping skin—leaving it hydrated, feeling soft, and looking luminous.',
    ingredients='Aqua/Water/Eau, Microcrystalline Cellulose, Propanediol, Sodium Cocoyl Glutamate, Glycerin, Acrylates Copolymer, Sodium Caproyl Methyltaurate, Coco-Betaine, Parfum/Fragrance, Saccharomyces/Camellia Sinensis Leaf/Cladosiphon Okamuranus/Rice Ferment Filtrate*, Oryza Sativa (Rice) Powder, Chondrus Crispus Extract, Sodium Hyaluronate, Betaphycus Gelatinum Extract, Lauryl Glucoside, Potassium Hydroxide, Polyquaternium-39, Disodium Edta, Phenoxyethanol, Ethylhexylglycerin, Sodium Benzoate, Sodium Carbonate, Alcohol.',
    img_url='https://www.sephora.com/productimages/sku/s2382232-main-zoom.jpg?imwidth=1224'
  )

  product5 = Product(
    product_name='Superfood Antioxidant Cleanser',
    brand_name='Youth To The People',
    skincare_step='Cleanse',
    target='Pores, Dullness, Blemishes',
    description='An award-winning face wash with cold-pressed antioxidants to remove makeup, prevent buildup in pores, and support skin’s pH balance.',
    ingredients='Water/Aqua/Eau, Cocamidopropyl Hydroxysultaine, Sodium Cocoyl Glutamate, Aloe Barbadensis(Aloe Vera) Leaf Juice, Sorbeth-230 Tetraoleate, Polysorbate 20, Brassica Oleracea Acephala(Kale) Extract, Spinacia Oleracea(Spinach) Leaf Extract, Camellia Sinensis(Green Tea) Leaf Extract, Medicago Sativa(Alfalfa) Extract, Chamomilla Recutita(Matricaria) Flower Extract, Tetrahexyldecyl Ascorbate(Vitamin C), Glycerin, Panthenol(Vitamin B5), Tocopheryl Acetate(Vitamin E), Decyl Glucoside, Sorbitan Laurate, Tetrasodium Glutamate Diacetate, Gluconolactone, Calcium Gluconate, Ethylhexylglycerin, Maltodextrin, Citric Acid, Phenoxyethanol, Potassium Sorbate, Sodium Benzoate, Chlorophyllin-Copper Complex(CI 75810), Gardenia Jasminoides(Jasmine) Fruit Extract, Fragrance/Parfum.',
    img_url='https://www.sephora.com/productimages/sku/s1863588-main-zoom.jpg?imwidth=1224'
  )

  product6 = Product(
    product_name='Soy Makeup Removing Face Wash',
    brand_name='fresh',
    skincare_step='Cleanse',
    target=' Dryness, Dullness, Uneven Texture',
    description='A bestselling pH-balanced face wash with amino acid–rich soy proteins that melt away makeup and the look of impurities for toned skin.',
    ingredients='',
    img_url='https://www.sephora.com/productimages/sku/s1863588-main-zoom.jpg?imwidth=1224'
  )

  product7 = Product(
    product_name='Glycolic Acid 7% Toning Solution',
    brand_name='The Ordinary',
    skincare_step='Treat',
    target='Dullness, Uneven Texture',
    description='An exfoliating toning solution with seven percent glycolic acid, amino acids, aloe vera, ginseng, and Tasmanian pepperberry.',
    precautions='alpha hydroxy acid (AHA)',
    ingredients='Aqua (Water), Glycolic Acid, Rosa damascena flower water, Centaurea cyanus flower water, Aloe Barbadensis Leaf Water, Propanediol, Glycerin, Triethanolamine, Aminomethyl Propanol, Panax Ginseng Root Extract, Tasmannia Lanceolata Fruit/Leaf Extract, Aspartic Acid, Alanine, Glycine, Serine, Valine, Isoleucine, Proline, Threonine, Histidine, Phenylalanine, Glutamic Acid, Arginine, PCA, Sodium PCA, Sodium Lactate, Fructose, Glucose, Sucrose, Urea, Hexyl Nicotinate, Dextrin, Citric Acid, Polysorbate 20, Gellan Gum, Trisodium Ethylenediamine Disuccinate, Sodium Chloride, Hexylene Glycol, Potassium Sorbate, Sodium Benzoate, 1,2-Hexanediol, Caprylyl Glycol.',
    img_url='https://www.sephora.com/productimages/sku/s2031508-main-zoom.jpg?imwidth=1224'
  )

  product8 = Product(
    product_name='10% Azelaic Acid Booster',
    brand_name='Paula\'s Choice',
    skincare_step='Treat',
    target='Redness, Uneven Texture, Acne and Blemishes',
    description='A potent azelaic-and-salicylic-acid cream that dramatically and visibly clarifies uneven skin tone, fades acne marks, and reduces redness.',
    ingredients='Water (Aqua), Azelaic Acid, C12-15 Alkyl Benzoate, Caprylic/Capric Triglyceride, Methyl Glucose Sesquistearate, Glycerin, Cetearyl Alcohol, Glyceryl Stearate, Dimethicone, Salicylic Acid, Adenosine, Glycyrrhiza Glabra (Licorice) Root Extract, Boerhavia Diffusa Root Extract, Allantoin, Bisabolol, Cyclopentasiloxane, Xanthan Gum, Sclerotium Gum, Propanediol, Butylene Glycol, Phenoxyethanol.',
    img_url='https://www.sephora.com/productimages/sku/s2421329-main-zoom.jpg?imwidth=1224',
  )

  product9 = Product(
      product_name='AHA 30% + BHA 2% Peeling Solution',
      brand_name='The Ordinary',
      skincare_step='Treat',
      target='Dullness, Uneven Texture, Acne and Blemishes',
      time_of_use='PM',
      description='An exfoliating solution to help fight visible blemishes and improve the look of skin texture and radiance.',
      precautions='Do not use on wet skin or leave on skin for longer than 10 minutes. Do not use more than twice a week.',
      ingredients='Glycolic Acid, Aqua (Water), Aloe Barbadensis Leaf Water, Sodium Hydroxide, Daucus Carota Sativa Extract, Propanediol, Cocamidopropyl Dimethylamine, Salicylic Acid, Potassium Citrate, Lactic Acid, Tartaric Acid, Citric Acid, Panthenol, Sodium Hyaluronate Crosspolymer, Tasmannia Lanceolata Fruit/Leaf Extract, Glycerin, Pentylene Glycol, Xanthan gum, Polysorbate 20, Trisodium Ethylenediamine Disuccinate, Potassium Sorbate, Sodium Benzoate, Ethylhexylglycerin, 1,2-Hexanediol, Caprylyl Glycol.',
      img_url='https://www.sephora.com/productimages/sku/s2210607-main-zoom.jpg?imwidth=1224'
  )

  product10 = Product(
    product_name='Cicapair™ Tiger Grass Camo Drops SPF 35',
    brand_name='Dr. Jart+',
    skincare_step='Treat',
    target='Dullness, Redness, Uneven Texture',
    time_of_use='AM',
    description='A lightweight revitalizing serum and color corrector that neutralize the look of redness and turn on skin\'s glow.',
    ingredients='Niacinamide, Centella asiatica Complex, Herbs Complex and Minerals Solution, Green Energy Complex.',
    img_url='https://www.sephora.com/productimages/sku/s2450856-main-zoom.jpg?imwidth=1224'
  )

  product11 = Product(
    product_name='Pharma BHA Acne Spot Treatment Gel 2% Salicylic Acid',
    brand_name='First Aid Beauty',
    skincare_step='Treat',
    target='Pores, Oiliness, Acne and Blemishes',
    description='A rapid-action formula with two percent salicylic acid to fight breakouts and visibly improve blemish-prone skin in as little as 24 hours.',
    precautions='Excessive drying of skin may occur. Start with one application daily, then gradually increase usage as needed.',
    ingredients='Salicylic Acid 2.0%, Water/Aqua/Eau, Butlyene Glycol, Hydroxyethylcellulose, Glycerin, Phenoxyethanol, Sodium Hydroxide, Glycolic Acid, Urea, Aloe Barbadensis Leaf Juice, Bisabolol, Colloidal Oatmeal, Maltodextrin, Carica Papaya (Papaya) Fruit Extract, Potassium Sorbate, Sodium Benzoate, Camellia Sinensis Leaf Extract, Chrysanthemum Parthenium (Feverfew) Extract, Glycyrrhiza Glabra (Licorice) Root Extract, Salix Nigra (Willow) Bark Extract, Disodium Phosphate, Polysorbate 60, Leuconostoc/Radish Root Ferment Filtrate, Sodium Phosphate, Citric Acid.',
    img_url='https://www.sephora.com/productimages/sku/s2382091-main-zoom.jpg?imwidth=1224'
  )

  product12 = Product(
    product_name='Fermented Soybean Firming Energy Essence',
    brand_name='innisfree',
    skincare_step='Nourish',
    target='Loss of Firmness and Elasticity, Dryness, Dullness, Uneven Texture',
    description='A hydrating essence that helps visibly improve the skin\'s firmness, brightness, tone, smoothness, dewiness and moisture barrier.',
    ingredients='Water, Propanediol, Bacillus/Soybean Ferment Extract, Arbutin, Polyglycerin-3, 1,2-Hexanediol, Ppg-13-Decyltetradeceth-24, Betaine, Sodium Polyacrylate, Avena Sativa (Oat) Kernel Extract, Ethylhexylglycerin, Disodium Edta, Adenosine, Hydroxypropyl Cyclodextrin, Phenoxyethanol.',
    img_url='https://www.sephora.com/productimages/sku/s2276491-main-zoom.jpg?imwidth=1224'
  )

  product13 = Product(
    product_name='Truth Serum®',
    brand_name='OLEHENRIKSEN',
    skincare_step='Nourish',
    target='Dryness, Dullness, Loss of Firmness and Elasticity',
    description='A powerful anti-aging serum formulated with vitamin C and collagen for brightening and all-day hydration.',
    precautions='Avoid contact with eyes. In case of contact with eyes, rinse immediately.',
    ingredients='Aqua/Water/Eau, Glycerin, Oleth-20, Sodium Ascorbyl Phosphate, Hydroxyethylcellulose, Phenoxyethanol, Caprylyl Glycol, Hexylene Glycol, Citric Acid, Parfum/Fragrance, Peg-12 Dimethicone, Tocopheryl Acetate, Aroma/Flavor, Collagen, Disodium Phosphate, Polysorbate 60, Yellow 6 (CI 15985), Aloe Barbadensis Leaf Extract, Citrus Aurantium Dulcis (Orange) Fruit Extract, Sodium Hyaluronate, Thioctic Acid, Calcium Ascorbate, Sodium Phosphate, Sorbitol, Citrus Grandis (Grapefruit) Seed Extract, Sodium Benzoate, Ascorbic Acid, Camellia Sinensis Leaf Extract, Euphrasia Officinalis Extract, Rosa Canina Fruit Extract, Leuconostoc/Radish Root Ferment Filtrate, Potassium Sorbate, Triacetin, Sodium Benzotriazolyl Butylphenol Sulfonate, Benzyl Benzoate, Limonene, Linalool.',
    img_url='https://www.sephora.com/productimages/sku/s2409159-main-zoom.jpg?imwidth=1224'
  )

  product14 = Product(
    product_name='C15 Vitamin C Super Booster',
    brand_name='Paula\'s Choice',
    skincare_step='Nourish',
    target='Dark Spots, Fine Lines and Wrinkles, Dullness',
    time_of_use='AM',
    description='A high-strength serum with 15 percent pure vitamin C to visibly improve skin’s brightness, firmness, stubborn discoloration, and dull and uneven tone.',
    ingredients='Water (Aqua), Ascorbic Acid, Butylene Glycol, Ethoxydiglycol, Glycerin, PPG-26-Buteth-26, PEG-40 Hydrogenated Castor Oil, Pentylene Glycol, Tocopherol (Vitamin E), Sodium Hyaluronate, Hexanoyl Dipeptide-3 Norleucine Acetate, Lecithin, Ferulic Acid, Panthenol, Bisabolol, Oryza Sativa (Rice) Bran Extract, Propyl Gallate, Sodium Gluconate, Sodium Hydroxide, Phenoxyethanol, Ethylhexylglycerin.',
    img_url='https://www.sephora.com/productimages/sku/s2421337-main-zoom.jpg?imwidth=1224'
  )

  product15 = Product(
    product_name='Niacinamide 10% + Zinc 1%',
    brand_name='The Ordinary',
    skincare_step='Nourish',
    target='Pores, Oiliness',
    description='A high-strength vitamin-and-mineral blemish formula with 10 percent pure niacinamide and one percent zinc PCA.',
    precautions='If topical vitamin C is used as part of skincare, it should be applied at alternate times with this formula in the AM. Otherwise, niacinamide can affect integrity of pure-form vitamin C.',
    ingredients='Aqua (Water), Niacinamide, Pentylene Glycol, Zinc PCA, Dimethyl Isosorbide, Tamarindus Indica Seed Gum, Xanthan gum, Isoceteth-20, Ethoxydiglycol, Phenoxyethanol, Chlorphenesin.',
    img_url='https://www.sephora.com/productimages/sku/s2031391-main-zoom.jpg?imwidth=1224'
  )

  product16 = Product(
    product_name='Ultra Repair® Hydrating Serum',
    brand_name='First Aid Beauty',
    skincare_step='Nourish',
    target='Dryness, Fine Lines and Wrinkles, Redness',
    description='A water-based serum that gives skin its daily dose of moisture for soft, smooth, youthful-looking skin.',
    ingredients='Aqua/Water/Eau, Glycerin, Soluble Collagen, Methyl Gluceth-20, Phenoxyethanol, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Hydroxyethylcellulose, Colloidal Oatmeal, Maltodextrin, Sodium Hydroxide, Aloe Barbadensis Leaf Juice, Panthenol, Hyaluronic Acid, Camellia Sinensis Leaf Extract, Sodium PCA, Chrysanthemum Parthenium (Feverfew) Extract, Potassium Sorbate, Sodium Benzoate, Glycyrrhiza Glabra (Licorice) Root Extract, Allantoin, Disodium Phosphate, Polysorbate 60, Sodium Phosphate, Tetrasodium EDTA.',
    img_url='https://www.sephora.com/productimages/sku/s2203958-main-zoom.jpg?imwidth=1224'
  )

  product17 = Product(
    product_name='Watermelon + AHA Glow Sleeping Mask',
    brand_name='Glow Recipe',
    skincare_step='Moisturize',
    target='Pores, Dryness, Oiliness',
    time_of_use='PM',
    description='A skin-smoothing, cult-favorite nightly sleeping mask with watermelon, hyaluronic acid, and AHAs that gently exfoliate and refine the look of pores.',
    ingredients='Water, Sodium Hyaluronate, Glycerin, Caulerpa Lentillifera (Seaweed) Extract, Simethicone, Citrullus Lanatus (Watermelon) Fruit, Silica, Propanediol, Glycolic Acid, Lactic Acid, Cucurbita Pepo (Pumpkin) Fruit Extract, Punica Granatum (Pomegranate) Fruit Extract, Musa Sapientum (Banana) Fruit Extract , Paeonia Suffruticosa (Peony) Root Extract, Glycyrrhiza Glabra (Licorice) Root Extract, Brassica Oleracea Capitata (Cabbage) Leaf Extract, Ipomoea Batatas (Sweet Potato) Root Extract, Betaine, Beta Glucan, Hydroxyethylcellulose, Xanthan Gum, Alcohol, Fragrance.',
    img_url='https://www.sephora.com/productimages/sku/s1955764-main-zoom.jpg?imwidth=1224'
  )

  product18 = Product(
    product_name='Water Sleeping Mask',
    brand_name='LANIEGE',
    skincare_step='Moisturize',
    target='Dryness, Dullness and Uneven Texture, Fine Lines and Wrinkles',
    time_of_use='PM',
    description='An overnight, moisture-recharging gel mask that quickly absorbs while you sleep to deeply hydrate skin.',
    precautions='Keep away from direct sunlight and avoid applying product on open wounds or skin inflammation.',
    ingredients='Water, Butylene Glycol, Cyclopentasiloxane, Glycerin, Cyclohexasiloxane, Trehalose, Sodium Hyaluronate, Oenothera Biennis (Evening Primrose) Root Extract, Prunus Armeniaca (Apricot) Fruit Extract, Beta-Glucan, Chenopodium Quinoa Seed Extract, Ascorbyl Glucoside, Magnesium Sulfate, Zinc Sulfate, Manganese Sulfate, Calcium Chloride, Potassium Alginate, Ammonium Acryloyldimethyltaurate / VP Copolymer, Polysorbate 20, Dimethicone, Dimethiconol, Dimethicone / Vinyl Dimethicone Crosspolymer, Propanediol, Ethylhexylglycerin, Stearyl Behenate, Polyglyceryl-3 Methylglucose Distearate, Hydroxypropyl Bispalmitamide MEA, Inulin Lauryl Carbamate, Alcohol, 1,2-Hexanediol, Caprylyl Glycol, Carbomer, Tromethamine, Disodium EDTA, Phenoxyethanol, Fragrance, Blue 1 (Ci 42090).',
    img_url='https://www.sephora.com/productimages/sku/s1966241-main-zoom.jpg?imwidth=1224'
  )

  product19 = Product(
    product_name='Ultra Facial Overnight Hydrating Mask',
    brand_name='Kiehl\'s Since 1851',
    skincare_step='Moisturize',
    target='Dryness, Dullness and Uneven Skin',
    time_of_use='PM',
    description='An overnight face mask softens the look of skin with intense hydration.',
    precautions='Use once or twice a week before bed.',
    ingredients='Water, Glycerin, Propylene Glycol, Squalane, Butyrospermum Parkii Butter/Shea Butter, Triethanolamine, Carbomer, Urea, Dimethicone, Hydroxyethylpiperazine Ethane Sulfonic Acid, Phenoxyethanol, Caprylyl Glycol, Imperata Cylindrica Root Extract, Ophiopogon Japonicus Root Extract, Sodium Citrate, Citric Acid, Aluminum Starch Octenylsuccinate, Chlorphenesin, Pseudoalteromonas Ferment Extract, Disodium EDTA, Acrylates/C10-30 Alkyl Acrylate Crosspolymer',
    img_url='https://www.sephora.com/productimages/sku/s1988583-main-zoom.jpg?imwidth=1224',
  )

  product20 = Product(
    product_name='Luminous Dewy Skin Night Concentrate',
    brand_name='Tatcha',
    skincare_step='Moisturize',
    target='Dryness, Dullness and Uneven Texture, Fine Lines and Wrinkles',
    time_of_use='PM',
    description='An ultra-hydrating concentrate of botanical oils and extracts that melt into skin for a youthful-looking glow in as little as one night.',
    ingredients='Water, Glycerin, Propanediol, Squalane, Cyclopentasiloxane, Triethylhexanoin, Panax Ginseng Root Extract, Origanum Majorana Leaf Extract, Ziziphus Jujuba Fruit Extract, Thymus Serpyllum Extract, Royal Jelly Extract, Stearyl Glycyrrhetinate, Camellia Sinensis Leaf Extract, Algae Extract, Scutellaria Baicalensis Root Extract, Oryza Sativa (Rice) Germ Oil, Camellia Japonica Seed Oil, Sericin, Inositol, Glyceryl Stearate Se, Polyglyceryl-2 Diisostearate, Ppg-5-Ceteth-10 Phosphate, Sodium Lauroyl Lactylate, Sorbitan Stearate, Trideceth-12, Ethylhexylglycerin, Peg-240/Hdi Copolymer Bis-Decyltetradeceth-20 Ether, Butylene Glycol, Behenyl Alcohol, Parfum/Fragrance, Alcohol, Phenoxyethanol.',
    img_url='https://www.sephora.com/productimages/sku/s1778851-main-zoom.jpg?imwidth=1224',
  )

  product21 = Product(
    product_name='The True Cream Aqua Bomb',
    brand_name='belif',
    skincare_step='Moisturize',
    target='Dryness, Dullness and Uneven Texture',
    description='A lightweight gel-cream that provides a burst of hydration for a healthy glow and acts as a cooling and refreshing "drink of water" for dull, dry skin.',
    ingredients='Water, Dipropylene Glycol, Glycerin, Methl Trimethicone, Alcohol Denat, Dimethicone, Cyclopentasiloxane, 1,2-Hexanediol, Malakite Extract, Caprylic/Capric Triglyceride, Pentaerythrityl Tetraethylhexanoate, PEG/PPG/Polybutylene Glycol-8/5/3 Glycerin, Alchemilla Vulgaris Leaf Extract*, Equisetum Arvense Leaf Extract*, Stellaria Media (Chickweed) Extract*, Urtica Dioica (Nettle) Leaf Extract*, Plantago Lanceolata Leaf Extract*, Avena Sativa (Oat) Kernel Extract**, Calendula Officinalis Flower Extract**, Nepeta Cataria Extract**, Rubus Idaeus (Raspberry) Leaf Extract**, Baptisia Tinctoria Root Extract**, Dimethiconol, Polymethylsilsesquioxane, Sodium Acrylate/Acryloyldimethyltaurate/Dimethylacrylamide Crosspolymer.',
    img_url='https://www.sephora.com/productimages/sku/s1686427-main-zoom.jpg?imwidth=1224'
  )

  product22 = Product(
    product_name='Natural Moisturizing Factors + HA',
    brand_name='The Ordinary',
    skincare_step='Moisturize',
    target='Dryness',
    description='This formula offers non-greasy hydration that acts as a direct topical supplement of natural moisturizing factor components with amino acids, dermal lipids, and hyaluronic acid.',
    ingredients='Water, Caprylic/Capric Triglyceride, Cetyl Alcohol, Propanediol, Stearyl Alcohol, Glycerin, Sodium Hyaluronate, Arginine, Aspartic Acid, Glycine, Alanine, Serine, Valine, Isoleucine, Proline, Threonine, Histidine, Phenylalanine, Glucose, Maltose, Fructose, Trehalose, Sodium PCA, PCA, Sodium Lactate, Urea, Allantoin, Linoleic Acid, Oleic Acid, Phytosteryl Canola Glycerides, Palmitic Acid, Stearic Acid, Lecithin, Triolein, Tocopherol, Carbomer, Isoceteth-20, Polysorbate 60, Sodium Chloride, Citric Acid, Trisodium Ethylenediamine Disuccinate, Pentylene Glycol, Triethanolamine, Sodium Hydroxide, Phenoxyethanol, Chlorphenesin.',
    img_url='https://www.sephora.com/productimages/sku/s2031425-main-zoom.jpg?imwidth=1224',
  )

  product23 = Product(
    product_name='Hydra Vizor Invisible Moisturizer Broad Spectrum SPF 30 Sunscreen',
    brand_name='Fenty',
    skincare_step='Protect',
    target='Dark Spots, Pores, and Dryness',
    time_of_use= 'AM',
    description='A refillable two-in-one sunscreen moisturizer that’s lightweight, oil free, noncomedogenic, and invisible—it targets dark spots, and is makeup-friendly.',
    ingredients='Water, Glycerin, Carthamus Tinctorius (Safflower) Oleosomes, Pentylene Glycol, Butylene Glycol, C12-15 Alkyl Benzoate, Niacinamide, Zea Mays (Corn) Starch, Hyaluronic Acid, Sodium Hyaluronate, Citrullus Lanatus (Watermelon) Seed Extract, Adansonia Digitata Pulp Extract, Barosma Betulina Leaf Extract, Aloe Barbadensis Leaf Juice, Tocopheryl Acetate, Gluconolactone, Sorbitan Oleate, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Sodium Acrylate/Sodium Acryloyldimethyl Taurate Copolymer, Dimethicone, Isohexadecane, Ethylhexyl Methoxycrylene, Polysorbate 80, Xanthan Gum, Sodium Hydroxide, Citric Acid, Potassium Hydroxide, Tocopherol, Trisodium Ethylenediamine Disuccinate, Ethylhexylglycerin, Sodium Benzoate, Potassium Sorbate, Phenoxyethanol, Fragrance, Benzyl Salicylate, Citral, Hexyl Cinnamal, Limonene, Linalool, Red 33.',
    img_url='https://www.sephora.com/productimages/sku/s2418879-main-zoom.jpg?imwidth=1224'
  )

  product24 = Product(
    product_name='Ultra Facial Cream SPF 30',
    brand_name='Kiehl\'s',
    skincare_step='Protect',
    target='Dryness, Loss of Firmness and Elasticity',
    time_of_use='AM',
    description='A 24-hour, light-textured daily hydrator with that helps protect against skin-damaging UVA and UVB rays with broad spectrum SPF 30.',
    ingredients='Water, Glycerin, Squalane, Dimethicone, Peg-100 Stearate, Glyceryl Stearate, Silica, Octyldodecanol, Stearic Acid, Phenoxyethanol, Palmitic Acid, Tocopherol, Dicaprylyl Carbonate, Steareth-100, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Ophiopogon Japonicus Root Extract, Carbomer, Chlorphenesin, Capryloyl Salicylic Acid, Caprylyl Glycol, Xanthan Gum, Dimethicone/Vinyl Dimethicone Crosspolymer, Disodium Edta, Sodium Hydroxide, Citrus Aurantium Dulcis (Orange) Peel Oil, Limonene, Ectoin, Hydrolyzed Hyaluronic Acid, Myristic Acid, Mentha Piperita (Peppermint) Oil, Pseudoalteromonas Ferment Extract, Ethylhexylglycerin, Linalool, Salicylic Acid.',
    img_url='https://www.sephora.com/productimages/sku/s1988625-main-zoom.jpg?imwidth=1224'
  )

  product25 = Product(
    product_name='CLEAR Ultra-Light Daily Hydrating Fluid SPF 30+',
    brand_name='Paula\'s Choice',
    skincare_step='Protect',
    target='Redness, Acne and Blemishes, Oiliness',
    time_of_use='AM',
    description='A sheer, shine-free fluid sunscreen for acne-prone skin that minimizes the look of pores, absorbs excess oil, and visibly calms redness caused by breakouts.',
    ingredients='Avobenzone 2%, Octinoxate 7.5%, Octisalate 5%, Octocrylene 2%, Water (Aqua), Glycerin, Silica, Dimethicone, Benzyl Alcohol, Tocopherol, Chamomilla Recutita (Matricaria) Flower Extract, Vitis Vinifera (Grape) Seed Extract, Camellia Sinensis (Green Tea) Leaf Extract, Camellia Oleifera (Green Tea) Leaf Extract, Peucedanum Graveolens (Dill) Extract, Sambucus Nigra (Black Elderberry) Fruit Extract, Avena Sativa (Oat) Bran Extract, Punica Granatum (Pomegranate) Extract, Lycium Barbarum (Goji) Fruit Extract, Hydrogenated Lecithin, Titanium Dioxide, Dimethicone/Vinyl Dimethicone Crosspolymer, Diethylhexyl Syringylidenemalonate, Hydroxyethyl Acrylate/Sodium Acryloyldimethyl Taurate Copolymer, Xanthan Gum, Sodium Carbomer, Benzyl Alcohol, Sodium Benzoate, Potassium Sorbate, Phenoxyethanol.',
    img_url='https://www.sephora.com/productimages/sku/s2421238-main-zoom.jpg?imwidth=1224'
  )

  product26 = Product(
    product_name='Daily UV Defense Sunscreen SPF 36',
    brand_name='innisfree',
    skincare_step='Protect',
    target='Dryness',
    time_of_use='AM',
    description='A lightweight, water-based SPF 36 sunscreen that delivers invisible sun protection while hydrating and soothing skin.',
    ingredients='Water/Aqua/Eau, Butylene Glycol, Cyclopentasiloxane, Butyloctyl Salicylate, Ethylhexyl Methoxycrylene, Arachidyl Alcohol, Behenyl Alcohol, Glyceryl Stearate, Peg-100 Stearate, 1,2-Hexanediol, Polymethylsilsesquioxane, Cetyl Alcohol, Arachidyl Glucoside, Phenoxyethanol, Propanediol, Polyacrylate Crosspolymer-6, Octyldodecanol, Fragrance / Parfum, Xanthan Gum, Centella Asiatica Extract, Portulaca Oleracea Extract, Echium Plantagineum Seed Oil, T-Butyl Alcohol, Camellia Sinensis Leaf Extract, Ethylhexylglycerin, Helianthus Annuus (Sunflower) Seed Oil Unsaponifiables, Cardiospermum Halicacabum Flower/Leaf/Vine Extract, Tocopherol, Helianthus Annuus (Sunflower) Seed Oil, Glycerin, Hamamelis Virginiana (Witch Hazel) Leaf Extract, Citrus Unshiu Peel Extract, Opuntia Coccinellifera Fruit Extract, Orchid Extract, Camellia Japonica Leaf Extract, Citric Acid, Sodium Benzoate, Potassium Sorbate.',
    img_url='https://www.sephora.com/productimages/sku/s2338325-main-zoom.jpg?imwidth=1224'
  )

  db.session.add(product1)
  db.session.add(product2)
  db.session.add(product3)
  db.session.add(product4)
  db.session.add(product5)
  db.session.add(product6)
  db.session.add(product7)
  db.session.add(product8)
  db.session.add(product9)
  db.session.add(product10)
  db.session.add(product11)
  db.session.add(product12)
  db.session.add(product13)
  db.session.add(product14)
  db.session.add(product15)
  db.session.add(product16)
  db.session.add(product17)
  db.session.add(product18)
  db.session.add(product19)
  db.session.add(product20)
  db.session.add(product21)
  db.session.add(product22)
  db.session.add(product23)
  db.session.add(product24)
  db.session.add(product25)
  db.session.add(product26)

  db.session.commit()


def undo_products():
  db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
  db.session.commit()
