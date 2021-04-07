export const occupationLabels = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces', '?'];
export const workClassLabels = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked', '?'];
export const educationLabels = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool', '?'];
export const maritalStatusLabels = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse', '?'];
export const relationshipLabels = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried', '?'];
export const raceLabels = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black', '?'];
export const sexLabels = ['Female', 'Male', '?'];
export const nativeCountrylabels = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands', '?'];

const getIndexMap = (labels) => {
    return labels.reduce((collection, curr, i) => {
        return { [curr]: i, ...collection }
    }, {});
};

export function getCounts(data, selector, indexMap) {
    const counts = Object.keys(indexMap).map(lbl => 0);
    data.forEach(point => {
        const index = indexMap[point[selector]]
        if (index !== undefined) counts[index] += 1;
    });
    return counts;
}

export const columns = [
    'workClass',
    'education',
    'maritalStatus',
    'occupation',
    'relationship',
    'race',
    'sex',
    'nativeCountry'
]

export const columnLabelsMap = {
    occupation: occupationLabels,
    workClass: workClassLabels,
    education: educationLabels,
    maritalStatus: maritalStatusLabels,
    relationship: relationshipLabels,
    race: raceLabels,
    sex: sexLabels,
    nativeCountry: nativeCountrylabels
}

export function getCountsData(data, column) {
    return getCounts(data, column, getIndexMap(columnLabelsMap[column]));
}

export function getCountsDataMap(under50k, over50k) {
    const obj = {};
    Object.keys(columnLabelsMap).forEach(key => {
        obj[key] = {
            getData: () => {
                return {
                    under50k: getCountsData(under50k, key),
                    over50k: getCountsData(over50k, key)
                }
            },
            labels: columnLabelsMap[key],
            title: `${key} totals`
        }
    });
    return obj;
}